#!/usr/bin/env python3
"""Local startup registry. Python 3.10+, standard library only; no network actions."""
import argparse
import copy
import hashlib
import json
import math
import os
import re
import sys
import tempfile
from datetime import date, datetime, timezone
from pathlib import Path

PACKAGE = Path(__file__).resolve().parents[1]
MODEL = json.loads((PACKAGE / "schemas/model.json").read_text(encoding="utf-8"))


def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def digest(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True, ensure_ascii=False,
                                     allow_nan=False).encode()).hexdigest()


def validate(data):
    errors = []
    if not isinstance(data, dict):
        return ["registry must be an object"]
    if set(data) != {"schema_version", "workspace", "records", "audit"}:
        errors.append("registry keys must be schema_version, workspace, records, audit")
    if data.get("schema_version") != 1:
        errors.append("unsupported schema_version")
    if not isinstance(data.get("workspace"), str) or not data["workspace"].strip():
        errors.append("workspace must be a non-empty string")
    if not isinstance(data.get("records"), list) or not isinstance(data.get("audit"), list):
        return errors + ["records and audit must be arrays"]
    by_id = {}
    for row in data["records"]:
        if not isinstance(row, dict):
            errors.append("record must be an object")
            continue
        rid = row.get("id")
        if not isinstance(rid, str) or not re.fullmatch(r"[a-z][a-z0-9-]*", rid):
            errors.append("record id must be lowercase kebab-case")
            continue
        if rid in by_id:
            errors.append(f"{rid}: duplicate id")
        by_id[rid] = row
        kind = row.get("type")
        if not isinstance(kind, str) or kind not in MODEL["types"]:
            errors.append(f"{rid}: unknown type")
            continue
        required = MODEL["common_required"] + MODEL["types"][kind]["required"]
        for key in required:
            if key not in row:
                errors.append(f"{rid}: missing {key}")
        for key in ("title", "source", "status"):
            if not isinstance(row.get(key), str) or not row[key].strip():
                errors.append(f"{rid}: {key} must be non-empty")
        if row.get("evidence") not in MODEL["evidence"]:
            errors.append(f"{rid}: invalid evidence")
        if kind == "task":
            if row.get("status") not in ("draft", "ready", "in_progress", "blocked", "done", "cancelled"):
                errors.append(f"{rid}: invalid task status")
            if row.get("priority") not in ("P0", "P1", "P2", "P3"):
                errors.append(f"{rid}: invalid priority")
        for key in ("owner", "reviewer", "definition_of_done", "deliverable"):
            if row.get(key) is not None and not isinstance(row[key], str):
                errors.append(f"{rid}: {key} must be string or null")
        for key in MODEL["date_fields"]:
            val = row.get(key)
            if val is not None:
                try:
                    if not isinstance(val, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", val):
                        raise ValueError()
                    date.fromisoformat(val)
                except (ValueError, TypeError):
                    errors.append(f"{rid}: {key} must be YYYY-MM-DD or null")
        for key in MODEL["number_fields"]:
            val = row.get(key)
            if val is not None and (isinstance(val, bool) or not isinstance(val, (int, float))
                                    or not math.isfinite(val) or val < 0):
                errors.append(f"{rid}: {key} must be finite, non-negative or null")
        if isinstance(row.get("progress"), (int, float)) and row["progress"] > 100:
            errors.append(f"{rid}: progress exceeds 100")
        if kind == "kpi":
            if row.get("direction") not in ("higher", "lower"):
                errors.append(f"{rid}: direction must be higher or lower")
            if row.get("actual") is not None and not row.get("measured_on"):
                errors.append(f"{rid}: actual needs measured_on")
        if kind == "task" and row.get("status") == "done":
            if row.get("progress") != 100 or not row.get("deliverable"):
                errors.append(f"{rid}: done requires progress=100 and deliverable")
        if kind == "experiment":
            if row.get("decision") not in (None, "scale", "continue", "modify", "stop"):
                errors.append(f"{rid}: invalid experiment decision")
            if row.get("status") == "completed" and (not row.get("result") or not row.get("decision")):
                errors.append(f"{rid}: completed experiment requires result and decision")
        for start, end in (("start_date", "due_date"), ("start_date", "end_date"),
                           ("required_finish", "deadline")):
            a, b = row.get(start), row.get(end)
            if isinstance(a, str) and isinstance(b, str) and a > b:
                errors.append(f"{rid}: {start} is after {end}")
    for rid, row in by_id.items():
        for field, allowed in MODEL["relations"].items():
            refs = row.get(field)
            if refs is None:
                continue
            if not isinstance(refs, list) or any(not isinstance(x, str) for x in refs):
                errors.append(f"{rid}: {field} must be an array of ids")
                continue
            for ref in refs:
                if ref not in by_id:
                    errors.append(f"{rid}: {field} references missing {ref}")
                elif by_id[ref].get("type") not in allowed:
                    errors.append(f"{rid}: wrong reference type for {field}: {ref}")
        if row.get("type") == "task" and row.get("status") in ("ready", "in_progress", "done"):
            for key in ("owner", "reviewer", "due_date", "definition_of_done", "project_ids", "kpi_ids"):
                if not row.get(key):
                    errors.append(f"{rid}: ready task requires {key}")
    visiting, visited = set(), set()

    def visit(rid):
        if rid in visiting:
            errors.append(f"{rid}: dependency cycle")
            return
        if rid in visited:
            return
        visiting.add(rid)
        refs = by_id[rid].get("depends_on", [])
        if isinstance(refs, list):
            for ref in refs:
                if isinstance(ref, str) and ref in by_id:
                    visit(ref)
        visiting.remove(rid)
        visited.add(rid)

    for rid in by_id:
        visit(rid)
    for i, entry in enumerate(data["audit"]):
        if not isinstance(entry, dict) or not all(entry.get(k) for k in
                                                  ("at", "actor", "reason", "operation", "after")):
            errors.append(f"audit[{i}]: incomplete entry")
    return errors


def checked(data):
    errors = validate(data)
    if errors:
        raise ValueError("\n".join(errors))


def save(path, data, *, overwrite):
    """Exclusive writer lock, same-directory temp file and atomic replace."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    lock = path.with_suffix(path.suffix + ".lock")
    descriptor = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    temp = None
    try:
        os.close(descriptor)
        if path.exists() and not overwrite:
            raise ValueError(f"already exists: {path}")
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent,
                                         delete=False) as stream:
            temp = Path(stream.name)
            json.dump(data, stream, ensure_ascii=False, indent=2, allow_nan=False)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp, path)
    finally:
        if temp and temp.exists():
            temp.unlink()
        lock.unlink()


def buffer(project):
    fields = [project.get(x) for x in ("deadline", "required_finish", "forecast")]
    if not all(fields):
        return {"status": "UNKNOWN", "remaining_days": None, "consumed_pct": None}
    deadline, required, forecast = map(date.fromisoformat, fields)
    planned = (deadline - required).days
    remaining = (deadline - forecast).days
    consumed = max(0, (forecast - required).days)
    ratio = consumed / planned if planned > 0 else (1 if remaining <= 0 else 0)
    status = ("CRITICAL" if remaining < 0 else "RED" if remaining == 0 or ratio >= 1
              else "YELLOW" if ratio >= .5 else "GREEN")
    return {"status": status, "remaining_days": remaining,
            "consumed_pct": round(ratio * 100, 1)}


def review(data, today):
    checked(data)
    warnings = []
    projects = {}
    for row in data["records"]:
        rid, kind = row["id"], row["type"]
        if kind == "task" and row["status"] not in ("done", "cancelled"):
            if row.get("due_date") and date.fromisoformat(row["due_date"]) < today:
                warnings.append(f"{rid}: overdue")
            if row["status"] == "blocked":
                warnings.append(f"{rid}: blocked; resolve dependency/owner")
            if not row.get("owner") or not row.get("due_date"):
                warnings.append(f"{rid}: owner/deadline unconfirmed")
            if not row.get("kpi_ids"):
                warnings.append(f"{rid}: KPI not linked")
        if kind == "kpi":
            actual, target = row.get("actual"), row.get("target")
            if actual is None or target is None:
                warnings.append(f"{rid}: actual/target unknown")
            elif (actual < target if row["direction"] == "higher" else actual > target):
                warnings.append(f"{rid}: target gap ({actual} vs {target}); diagnose before changing creative")
        if kind == "project":
            projects[rid] = buffer(row)
            if projects[rid]["status"] != "GREEN":
                warnings.append(f"{rid}: buffer {projects[rid]['status']}")
        if kind == "experiment" and row["status"] != "completed" and row.get("end_date"):
            if date.fromisoformat(row["end_date"]) < today:
                warnings.append(f"{rid}: experiment ended; record result and learning")
    return {"workspace": data["workspace"], "as_of": today.isoformat(),
            "record_count": len(data["records"]), "warnings": warnings, "buffers": projects,
            "note": "Read-only diagnostic; priorities, budgets and publication require human decisions."}


def upsert(path, records, actor, reason):
    """All records in one request validate together; input file is never partially applied."""
    if not actor.strip() or not reason.strip():
        raise ValueError("actor and reason must be non-empty")
    path = Path(path)
    # Hold the transaction lock across read, validate and write to prevent lost updates.
    lock = path.with_suffix(path.suffix + ".transaction.lock")
    fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    try:
        os.close(fd)
        data = read(path)
        checked(data)
        before = digest(data["records"])
        if not isinstance(records, list) or not records:
            raise ValueError("input must be a non-empty JSON array of complete records")
        ids = [r.get("id") if isinstance(r, dict) else None for r in records]
        if any(not isinstance(rid, str) for rid in ids) or len(set(ids)) != len(ids):
            raise ValueError("input ids must be strings and unique")
        merged = {r["id"]: r for r in data["records"]}
        merged.update({r["id"]: r for r in records})
        data["records"] = list(merged.values())
        checked(data)
        after = digest(data["records"])
        if before == after:
            return False
        data["audit"].append({"at": datetime.now(timezone.utc).isoformat(), "actor": actor,
                              "reason": reason, "operation": "upsert", "ids": ids,
                              "before": before, "after": after})
        save(path, data, overwrite=True)
        return True
    finally:
        lock.unlink()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    init = sub.add_parser("init")
    init.add_argument("registry", type=Path)
    init.add_argument("--name", required=True)
    init.add_argument("--actor", required=True)
    for name in ("validate", "review", "upsert"):
        cmd = sub.add_parser(name)
        cmd.add_argument("registry", type=Path)
        if name == "review":
            cmd.add_argument("--today", type=date.fromisoformat, default=date.today())
        if name == "upsert":
            cmd.add_argument("input", type=Path)
            cmd.add_argument("--actor", required=True)
            cmd.add_argument("--reason", required=True)
    args = parser.parse_args()
    try:
        if args.command == "init":
            if not args.actor.strip():
                raise ValueError("actor must be non-empty")
            data = copy.deepcopy(read(PACKAGE / "templates/registry.json"))
            data["workspace"] = args.name
            data["audit"].append({"at": datetime.now(timezone.utc).isoformat(), "actor": args.actor,
                                  "operation": "init", "reason": "Initialize workspace",
                                  "after": digest(data["records"])})
            checked(data)
            save(args.registry, data, overwrite=False)
            print(f"Initialized: {args.registry}")
        elif args.command == "upsert":
            changed = upsert(args.registry, read(args.input), args.actor, args.reason)
            print("Updated with audit entry" if changed else "Unchanged (idempotent)")
        elif args.command == "validate":
            checked(read(args.registry))
            print("VALID")
        else:
            print(json.dumps(review(read(args.registry), args.today), ensure_ascii=False, indent=2))
    except (ValueError, OSError, RecursionError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
