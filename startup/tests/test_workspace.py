import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("workspace", ROOT / "startup/tools/workspace.py")
ws = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ws)


class RegistryTests(unittest.TestCase):
    def setUp(self):
        self.data = ws.read(ROOT / "startup/examples/demo-registry.json")

    def row(self, kind):
        return next(r for r in self.data["records"] if r["type"] == kind)

    def test_initial_data_has_no_fabricated_metrics(self):
        data = ws.read(ROOT / "startup/data/initial-business/registry.json")
        self.assertEqual(ws.validate(data), [])
        kpi = next(r for r in data["records"] if r["type"] == "kpi")
        self.assertIsNone(kpi["actual"])
        self.assertTrue(ws.review(data, date(2026, 9, 29))["warnings"])

    def test_duplicate_and_missing_references(self):
        self.data["records"].append(copy.deepcopy(self.row("company")))
        self.row("task")["kpi_ids"] = ["missing-kpi"]
        errors = ws.validate(self.data)
        self.assertTrue(any("duplicate" in e for e in errors))
        self.assertTrue(any("missing-kpi" in e for e in errors))

    def test_wrong_reference_type(self):
        self.row("task")["kpi_ids"] = ["company-marketing"]
        self.assertTrue(any("wrong reference type" in e for e in ws.validate(self.data)))

    def test_cycles(self):
        self.row("task")["depends_on"] = ["task-improve"]
        self.assertTrue(any("cycle" in e for e in ws.validate(self.data)))

    def test_invalid_dates_numbers_and_completion(self):
        task = self.row("task")
        task.update(due_date="2026-02-30", progress=101, actual_hours=-1, status="done")
        errors = ws.validate(self.data)
        for expected in ("YYYY-MM-DD", "exceeds", "non-negative", "done requires"):
            self.assertTrue(any(expected in e for e in errors), errors)

    def test_ready_requires_owner_and_kpi(self):
        self.row("task").update(owner=None, kpi_ids=[])
        errors = ws.validate(self.data)
        self.assertTrue(any("requires owner" in e for e in errors))
        self.assertTrue(any("requires kpi_ids" in e for e in errors))

    def test_actual_needs_measurement_date(self):
        self.row("kpi")["measured_on"] = None
        self.assertTrue(any("measured_on" in e for e in ws.validate(self.data)))

    def test_experiment_requires_result(self):
        self.row("experiment")["result"] = None
        self.assertTrue(any("requires result" in e for e in ws.validate(self.data)))

    def test_buffer_boundaries(self):
        project = self.row("project")
        for forecast, expected in [("2026-10-04", "GREEN"), ("2026-10-08", "YELLOW"),
                                   ("2026-10-10", "RED"), ("2026-10-11", "CRITICAL")]:
            project["forecast"] = forecast
            self.assertEqual(ws.buffer(project)["status"], expected)
        project["required_finish"] = project["deadline"]
        self.assertEqual(ws.buffer(project)["status"], "CRITICAL")
        project["forecast"] = None
        self.assertEqual(ws.buffer(project)["status"], "UNKNOWN")

    def test_review_detects_overdue_and_finished_experiment(self):
        self.row("task")["due_date"] = "2026-09-28"
        self.row("experiment")["status"] = "running"
        warnings = ws.review(self.data, date(2026, 9, 29))["warnings"]
        self.assertTrue(any("overdue" in w for w in warnings))
        self.assertTrue(any("experiment ended" in w for w in warnings))

    def test_invalid_update_leaves_original_bytes(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "registry.json"
            ws.save(path, self.data, overwrite=False)
            original = path.read_bytes()
            bad = copy.deepcopy(self.row("task"))
            bad["project_ids"] = ["absent"]
            with self.assertRaises(ValueError):
                ws.upsert(path, [bad], "tester", "invalid update")
            self.assertEqual(path.read_bytes(), original)

    def test_e2e_init_upsert_review_and_audit(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "registry.json"
            cli = [sys.executable, str(ROOT / "startup/tools/workspace.py")]
            result = subprocess.run(cli + ["init", str(path), "--name", "demo", "--actor", "tester"],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue(ws.upsert(path, self.data["records"], "tester", "full workflow"))
            saved = ws.read(path)
            self.assertEqual(ws.validate(saved), [])
            self.assertEqual(len(saved["audit"]), 2)
            self.assertFalse(ws.upsert(path, self.data["records"], "tester", "repeat request"))
            self.assertEqual(len(ws.read(path)["audit"]), 2)
            report = ws.review(saved, date(2026, 9, 29))
            self.assertEqual(report["buffers"]["project-first-hp"]["remaining_days"], 2)
            knowledge = next(r for r in saved["records"] if r["type"] == "knowledge")
            self.assertEqual(knowledge["experiment_ids"], ["experiment-demo"])

    def test_init_does_not_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "registry.json"
            ws.save(path, self.data, overwrite=False)
            with self.assertRaises(ValueError):
                ws.save(path, self.data, overwrite=False)

    def test_non_finite_number_is_rejected(self):
        self.row("kpi")["actual"] = float("nan")
        self.assertTrue(any("finite" in e for e in ws.validate(self.data)))

    def test_bad_relation_container_is_handled(self):
        self.row("task")["depends_on"] = {"unexpected": "shape"}
        self.assertTrue(any("array of ids" in e for e in ws.validate(self.data)))


if __name__ == "__main__":
    unittest.main()
