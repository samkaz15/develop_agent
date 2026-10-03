---
skill_name: capital-planning
display_name: Capital Planning Skill
category: business
version: 1.0.0
status: Draft   # Draft / Active / Deprecated
owner: "@samkaz15"
created: 2026-10-03
updated: 2026-10-03
related_agents: [business-launch, ceo]
related_phases: [0, 1]
tags: [launch, finance, capital, cashflow, runway]
---

# Capital Planning Skill

## 1. Skill Identity

| 項目 | 内容 |
|---|---|
| **Skill Name** | `capital-planning` |
| **Version** | `1.0.0` |
| **Category** | `business`（[`Skill_Architecture.md`](../../../00_System/Skill_Architecture.md) の7カテゴリに対応。Launch Track は [`launch/README.md`](../../../launch/README.md)） |
| **Purpose** | 事業計画から必要資金を逆算し、資本金・自己資金・借入・補助金の構成を、根拠付きの推奨レンジと感度分析で提示する能力。 |
| **Scope** | 設立費用・初期投資・運転資金・調達構成・月次資金繰り（24か月・3シナリオ）・創業計画書の骨子。外部投資家向けの資本政策・企業価値評価は対象外 |
| **Related Domain** | 管理会計、キャッシュフロー管理、創業融資実務 |

```yaml
identity:
  skill_name: "capital-planning"
  category: "business"
  purpose: "Back-calculate required funds from the business plan and recommend capital/loan/subsidy mix with evidence and sensitivity analysis."
```

---

## 2. Capability

### このSkillでできること
- 設立費用・初期投資・運転資金・予備費を積み上げて必要資金を算出する
- 24か月の月次資金繰りを Worst/Base/Best で試算し、資金ショート月とランウェイを特定する
- 資本金を判断軸（資金繰り・信用・融資・許認可・税務・将来の調達・手元資金）で比較し、推奨レンジを示す
- 補助金の後払いなど、入金時期のずれを資金繰りに反映する
- 融資申込用の創業計画書の骨子を作る

### できないこと

| できないこと | 理由 / 代替 |
|---|---|
| 資本金・調達構成の決定 | Owner が決定する（Gate L2）。本Skillは推奨と根拠まで |
| 融資・補助金の可否や受給の保証 | 実施機関の審査による。見込みは「確度」として示す |
| 税務上の判断（資本金額と税の関係） | 税理士に確認する |
| 融資の自己資金要件など制度要件の断定 | 制度は改定されるため、使う都度一次情報で確認する |
| 投資家向けの資本政策・企業価値評価 | 別途専門家（本Skillの範囲外） |

### 前提条件
- [ ] ビジネスモデル（収益モデル・価格の仮説）がある
- [ ] Intake の資金情報（自己資金・借入可能額・生活防衛資金）がある

### 適用条件
- Launch Track L1（資本設計）、融資申込前、事業計画が変わったとき
- **適用しない状況**: 開業後の予実管理（→ `launch-planning`）

### 制約事項
- 数値は仮説として扱い、根拠と確度を併記する
- 生活防衛資金は事業資金と別枠で確保する
- 制度要件・税の扱いは確認日付きで記録する

---

## 3. Required Knowledge

| 種別 | 内容 |
|---|---|
| **理論** | キャッシュフロー管理、損益分岐点分析、ユニットエコノミクス（LTV/CAC） |
| **ベストプラクティス** | Worst シナリオでも最低ランウェイ（目安6〜12か月）を満たす／予備費は10〜20%を目安に確保／補助金は後払い前提でつなぎ資金を持つ／生活防衛資金は別枠 |
| **フレームワーク** | 必要資金の積み上げ表、3シナリオ感度分析、資本金の判断軸①〜⑦、月次資金繰り表（`cashflow-plan.csv`） |
| **業界標準** | 会社法（資本金の概念）、法人税・法人住民税・消費税における資本金基準（取扱いは税理士に確認） |
| **参考ガイドライン** | 日本政策金融公庫・商工会議所の創業計画書様式、[`launch/templates/capital-plan.md`](../../../launch/templates/capital-plan.md) |

法令・料率・制度の**具体的な数値は固定知識にしない**。使う都度、公式の一次情報で確認し、出典URLと確認日を記録する（[`launch/README.md` — 情報の鮮度ルール](../../../launch/README.md#情報の鮮度ルール)）。

---

## 4. Inputs

### 必須入力

| 入力 | 形式 | 説明 |
|---|---|---|
| ビジネスモデル（価格・収益モデル・集客） | Markdown | 売上見込みの根拠 |
| 初期費用・固定費・変動費の見積 | Markdown / CSV | 見積書・相場の根拠付き |
| Intake の資金情報 | Markdown | 自己資金・借入可能額・生活防衛資金 |
| 役員報酬案 | CSV | `payroll-design` の成果物 |

### 任意入力
- 補助金・助成金の想定（`subsidy-research`）
- 取引先の支払条件（入金サイト）
- 設備・開発の見積書

### Context / 前工程成果物 / 設定値

| 種別 | 内容 |
|---|---|
| **Context** | Launch Track L1。Gate L2 の前に実行する |
| **前工程成果物** | `launch-brief.md` §1、`payroll-simulation.csv`、`subsidy-tracker.csv` |
| **設定値** | シナリオの売上係数（Worst=0.5／Base=1.0／Best=1.3 の目安）、予備費率、確保したいランウェイ月数 |

**入力不足の場合**: 推測で補完せず、不足項目を明示して呼び出し元（Agent/人間）に差し戻す（[Section 9 Error Handling](#9-error-handling)）。

---

## 5. Execution Framework

標準の実行フロー（Analyze → Plan → Execute → Validate → Optimize → Finalize）は [`Skill_Base_Template.md — Section 5`](../../../00_System/Skill_Base_Template.md#5-execution-framework) に従う。このSkillでの具体化は次のとおり。

| ステージ | このSkillでの型 |
|---|---|
| **Analyze** | 売上が立つまでの期間と固定費は。資金が尽きる条件は何か |
| **Plan** | 必要資金の積み上げ → 資金繰り（3シナリオ）→ 判断軸での資本金比較 → 調達構成の順で進める |
| **Execute** | `cashflow-plan.csv` に入力し、資金ショート月・ランウェイを算出。判断軸①〜⑦を埋める |
| **Validate** | Worst でも最低ランウェイを満たすか／根拠のない数値がないか／生活防衛資金を含めていないか |
| **Optimize** | 推奨レンジを絞り、「前提が崩れる条件」を明記する |
| **Finalize** | `capital-plan.md`・`cashflow-plan.csv`・創業計画書の骨子を確定する |

**運用ルール**: Validate で未達の場合は Plan に戻る（手法選定から見直す）。3回繰り返しても未達の場合は [Section 9](#9-error-handling) のエスカレーションに従う。

---

## 6. Outputs

### 成果物

| 出力形式 | 用途 | 出力先 |
|---|---|---|
| **Markdown** | 資本金・自己資金 設計書（必要資金・調達構成・判断軸・推奨と感度分析） | `strategy/launch/capital-plan.md` |
| **CSV** | 月次資金繰り（24か月） | `strategy/launch/sheets/cashflow-plan.csv` |
| **Recommendation** | 資本金・調達構成の選択肢と推奨（Gate L2 向け） | 成果物内 |

このSkillが実際に生成するのは: Markdown（設計書）、CSV（資金繰り）、Recommendation（Gate L2 向け）

---

## 7. Quality Criteria

### 完成条件（Definition of Done）
- [ ] 必要資金の各項目に根拠と確度がある
- [ ] Worst/Base/Best の3シナリオで資金ショート月とランウェイが出ている
- [ ] 判断軸①〜⑦が埋まり、推奨レンジと選ばなかった案が示されている
- [ ] 前提が崩れる条件（再計算のトリガー）が明記されている
- [ ] 制度要件・税の扱いに出典URLと確認日がある
- [ ] Decision Log（判断根拠）が記録されている
- [ ] [Section 6 Outputs](#6-outputs)の形式に準拠している

### 品質基準
[`Quality_Standard.md`](../../../00_System/Quality_Standard.md) の共通5基準（明瞭さ・簡潔さ・一貫性・検証可能性・誠実さ）を適用する。このSkillでは特に **検証可能性（根拠と確認日）と誠実さ（確度の明示）** を重視する。

### 判定基準

| 判定 | 条件 |
|---|---|
| ✅ **PASS** | 完成条件・品質基準を全て満たし証拠添付済み |
| ⚠️ **WARNING** | 必須は満たすが軽微な懸念あり（Open Issues登録・持ち越し2工程まで） |
| ❌ **FAIL** | 完成条件未達、または重大指摘あり（出典のない数値・専門家領域の断定・認証情報の混入 など） |

---

## 8. Human Judgment

このSkillの実行結果が以下に該当する場合、判断を確定させず選択肢＋推奨案として人間に提示する（[`Review_Process.md — Human Decision Framework`](../../../00_System/Review_Process.md#human-decision-framework) に加えて）:

- [ ] **ブランド**: （該当は限定的）
- [ ] **倫理**: 自己資金の実態以上に見せるなど、融資・補助金の審査に対する虚偽の説明をしない
- [ ] **法務**: 役員借入金・出資・融資契約の条件（個人保証を含む）は専門家へ。税務は税理士へ
- [ ] **最終意思決定**: 資本金額・調達構成（Gate L2）／借入の可否と個人保証の受容／事業規模の見直し
- [ ] 資金ショートが解消できない場合の事業規模・価格の見直し

---

## 9. Error Handling

| 状況 | 対応 |
|---|---|
| **入力不足** | 推測で補完せず、[Section 4 Inputs](#4-inputs)の不足項目を明示して差し戻す |
| **条件不足**（[Section 2 適用条件](#2-capability)を満たさない） | 実行を中断し、条件不足である旨と必要条件を報告する |
| **競合**（他Skill・専門家の見解と矛盾） | 専門家の見解と一次情報を優先し、対立をDecision Logに記録。解決しなければ呼び出し元Agentに判断を委ねる |
| **リスク**（[Section 8 Human Judgment](#8-human-judgment)に該当する結果に至った） | 確定させず、選択肢＋推奨案として提示する |
| **一次情報で確認できない** | 「未確認」と明記し、Confidence を Low にして専門家または人間へ回す。二次情報で埋めない |
| **資金ショートが解消できない** | Gate L2 を止め、事業規模・価格・調達構成の見直し案を提示して人間に判断を仰ぐ |
| **再実行** | [Section 5 Execution Framework](#5-execution-framework)のPlanに戻る。最大3回。同じ手法を繰り返さない（毎回変更点を記録） |
| **エスカレーション** | 3回の再実行でも未達、またはCritical相当のリスク（法令違反の疑い・資金ショート確定・認証情報の漏えいの疑い）を検出した場合、呼び出し元Agent経由で人間に引き上げる |

---

## 10. Performance

| 指標 | 定義 | 目標 |
|---|---|---|
| **Accuracy** | 初回実行でのPASS率 | ≧ 80%（[`Quality_Standard.md`](../../../00_System/Quality_Standard.md) 品質KPI準拠） |
| **Speed** | 実行の所要時間（タスク規模あたり） | 1セッション以内（3シナリオ・24か月） |
| **Cost** | 実行あたりのトークン・検索コスト | 調査は一次情報に絞り、同じ情報を重複取得しない |
| **Token Efficiency** | 不要なコンテキストを持ち込まない | 必要な知識・入力・テンプレートのみ参照する |
| **Scalability** | 業種・地域が変わっても品質が劣化しないか | 業種・地域固有の情報は Input で注入し、Skill本体は非依存に保つ |

---

## 11. Reusability

| 項目 | 内容 |
|---|---|
| **利用可能Agent** | 主利用: `business-launch` ／ 副利用: `ceo` |
| **関連Skill** | `payroll-design`、`subsidy-research`、`launch-planning`、`kpi-design` |
| **依存Skill** | `business-strategy`（収益モデル）、`payroll-design`（役員報酬案） |

### 継承ルール
- サブカテゴリへの分割時、共通のCapability・Required Knowledgeは親Skillに残し、子Skillは差分のみを記述する
- 依存Skillのバージョンが上がった場合、このSkillの互換性を [Skill Versioning](../../../00_System/Skill_Base_Template.md#skill-versioning) に従い確認する

---

## 12. Documentation

| ファイル | 必須/任意 | 内容 |
|---|---|---|
| `SKILL.md` | 必須 | 本定義 |
| `CHANGELOG.md` | 必須 | 変更履歴 |
| `references/` | 任意 | フレームワーク詳細・チェックリスト・外部資料の要約 |
| `examples/` | 推奨 | 実案件での良例・失敗例（運用後に蓄積） |
