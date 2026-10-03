---
skill_name: launch-planning
display_name: Launch Planning Skill
category: business
version: 1.0.0
status: Draft   # Draft / Active / Deprecated
owner: "@samkaz15"
created: 2026-10-03
updated: 2026-10-03
related_agents: [business-launch, ceo, product-manager, growth]
related_phases: [0, 1, 18]
tags: [launch, wbs, budget-actual, kpi, monthly-review]
---

# Launch Planning Skill

## 1. Skill Identity

| 項目 | 内容 |
|---|---|
| **Skill Name** | `launch-planning` |
| **Version** | `1.0.0` |
| **Category** | `business`（[`Skill_Architecture.md`](../../../00_System/Skill_Architecture.md) の7カテゴリに対応。Launch Track は [`launch/README.md`](../../../launch/README.md)） |
| **Purpose** | 立ち上げ全工程のWBS、月次の予実管理表（余日管理表）、KPI-KGIを作成・更新し、開業後は予実差異とKPIから改善施策案を出す能力。 |
| **Scope** | WBS（フェーズ行・タスク行・開始日／完了日・Duration・進捗・ガント。雛形は `wbs-template.xlsx`）、余日管理表（月次の目標・実質値・費用・ROAS。雛形は `yojitsu-template.xlsx`）、KPI-KGIのファネル逆算、月次レビュー |
| **Related Domain** | プロジェクト管理（WBS・クリティカルパス）、予算管理（予実差異分析）、KPI設計 |

```yaml
identity:
  skill_name: "launch-planning"
  category: "business"
  purpose: "Create and maintain the launch WBS, monthly budget-vs-actual tracker and KPI/KGI sheet, and propose improvement actions from variances after launch."
```

---

## 2. Capability

### このSkillでできること
- 立ち上げ全工程のWBSを作る（開始日・完了日を入れるとガントのバーと Duration が自動で入る。前後関係はタスクの並びと定義欄で管理する）
- 余日管理表の雛形で、売上目標と実質値（実績）・成長率・手数料／物流・販管費・広告のROI・ROAS を月別に管理する
- KGIからファネルを逆算し（顧客数→問い合わせ→アクセス→IMP→投稿数）、LTV/CAC を算出する
- 月次レビューで差異の要因を事実と仮説に分けて整理し、改善施策案を出す
- 期限が近いタスク・手続のリスクを抽出する

### できないこと

| できないこと | 理由 / 代替 |
|---|---|
| 予算・目標の決定 | Owner が決定する |
| 施策の実行決定 | 人間が決定する |
| 会計上の正式な数値の確定 | 会計ツール・税理士 |
| 開業後のグロース施策の実行・A/Bテスト | `growth` Agent |

### 前提条件
- [ ] プロジェクト開始日が決まっている
- [ ] ビジネスモデルと資金繰り（`cashflow-plan.csv`）がある
- [ ] KGI（月次の売上目標など）の仮置きがある

### 適用条件
- Launch Track L0（WBS作成）〜L8（月次運用）。事業計画・体制が変わるとき
- **適用しない状況**: プロダクト開発側のWBS（`Development_Workflow.md` が正本）

### 制約事項
- 数値は例であり、実績で更新する
- 祝日は考慮していない（必要なら手で調整する）
- 成長率は「売上実質値」を入力した月から計算される。未入力の月は空欄または0になる

---

## 3. Required Knowledge

| 種別 | 内容 |
|---|---|
| **理論** | WBS（作業分解）・クリティカルパス、予実差異分析、KGI–KPIツリー |
| **ベストプラクティス** | 前工程の完了日を次工程の開始日に反映する／差異は事実と仮説を分けて原因を考える／月次で固定の日にレビューする／Gate 未通過で次工程に進めない |
| **フレームワーク** | `wbs-incorporation.xlsx`、`yojitsu-template.xlsx`、`kpi-kgi.csv`、月次レビュー記録 |
| **業界標準** | （該当する標準規格なし。プロジェクト管理の一般的な WBS の考え方を参照） |
| **参考ガイドライン** | [`launch/README.md` — 管理表の雛形（トレース元）](../../../launch/README.md#管理表の雛形トレース元) |

法令・料率・制度の**具体的な数値は固定知識にしない**。使う都度、公式の一次情報で確認し、出典URLと確認日を記録する（[`launch/README.md` — 情報の鮮度ルール](../../../launch/README.md#情報の鮮度ルール)）。

---

## 4. Inputs

### 必須入力

| 入力 | 形式 | 説明 |
|---|---|---|
| プロジェクト開始日 | 日付 | WBSの起点 |
| 資金繰り計画 | CSV | `cashflow-plan.csv`。予算の根拠 |
| KGIと転換率の仮置き | 数値 | ファネル逆算の入力 |

### 任意入力
- 実績データ（会計・SNSアナリティクス）
- 担当者・稼働時間
- 優先したいGate・マイルストーン

### Context / 前工程成果物 / 設定値

| 種別 | 内容 |
|---|---|
| **Context** | Launch Track L0〜L8。月次レビューは開業後 |
| **前工程成果物** | `cashflow-plan.csv`、`sns-content-calendar.csv`、各成果物の期限 |
| **設定値** | WBSの開始日（`C3`）、余日管理表の開始月（`F3`）、売上係数、KPI目標 |

**入力不足の場合**: 推測で補完せず、不足項目を明示して呼び出し元（Agent/人間）に差し戻す（[Section 9 Error Handling](#9-error-handling)）。

---

## 5. Execution Framework

標準の実行フロー（Analyze → Plan → Execute → Validate → Optimize → Finalize）は [`Skill_Base_Template.md — Section 5`](../../../00_System/Skill_Base_Template.md#5-execution-framework) に従う。このSkillでの具体化は次のとおり。

| ステージ | このSkillでの型 |
|---|---|
| **Analyze** | どの工程が依存し、どこが期限リスクか。予算の根拠は何か |
| **Plan** | WBS → 予算確定 → KPI逆算 → 運用ルール（更新頻度・担当）の順で進める |
| **Execute** | CSV をスプレッドシートに取り込み、開始日・開始月・目標を入力して数式を確認する |
| **Validate** | 依存・期限・Gate が整合しているか／数式が壊れていないか／予算が資金繰りと一致しているか |
| **Optimize** | 実績が入ってからは、勝ち/負けパターンに効く指標だけを見る |
| **Finalize** | 管理表3点と月次レビュー記録を確定する |

**運用ルール**: Validate で未達の場合は Plan に戻る（手法選定から見直す）。3回繰り返しても未達の場合は [Section 9](#9-error-handling) のエスカレーションに従う。

---

## 6. Outputs

### 成果物

| 出力形式 | 用途 | 出力先 |
|---|---|---|
| **XLSX** | WBS | `strategy/launch/sheets/wbs-incorporation.xlsx`（空の雛形は `wbs-template.xlsx`） |
| **XLSX** | 余日管理表（月次の目標・実質値・費用・ROAS） | `strategy/launch/sheets/yojitsu-template.xlsx` |
| **CSV** | KPI-KGI（ファネル逆算） | `strategy/launch/sheets/kpi-kgi.csv` |
| **Report** | 月次レビュー（差異要因・KPI・施策案） | `strategy/launch/monthly-review-YYYY-MM.md` |

このSkillが実際に生成するのは: XLSX（WBS・余日管理表）、CSV（KPI-KGI）、Report（月次レビュー）

---

## 7. Quality Criteria

### 完成条件（Definition of Done）
- [ ] WBS の開始日・完了日・Gate・担当区分（AI/協働/人間/士業）が整合している
- [ ] 余日管理表の売上目標・費用が資金繰りと一致し、実質値（実績）の入力担当と頻度が決まっている
- [ ] KPI-KGI の逆算結果が事業の現実と照らして妥当か確認されている
- [ ] 月次レビューでは差異の要因が事実と仮説に分けられている
- [ ] Decision Log（判断根拠）が記録されている
- [ ] [Section 6 Outputs](#6-outputs)の形式に準拠している

### 品質基準
[`Quality_Standard.md`](../../../00_System/Quality_Standard.md) の共通5基準（明瞭さ・簡潔さ・一貫性・検証可能性・誠実さ）を適用する。このSkillでは特に **一貫性（資金繰り・WBS・KPIの整合）と検証可能性（実績データ）** を重視する。

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
- [ ] **倫理**: KPI達成のためのダークパターン・誇大表現を施策案に含めない
- [ ] **法務**: （該当は限定的。会計上の数値の確定は税理士）
- [ ] **最終意思決定**: 予算・KGI・施策の決定、Gate の通過、撤退・見直し
- [ ] 月次レビューで提案した施策の実行決定とリソース配分

---

## 9. Error Handling

| 状況 | 対応 |
|---|---|
| **入力不足** | 推測で補完せず、[Section 4 Inputs](#4-inputs)の不足項目を明示して差し戻す |
| **条件不足**（[Section 2 適用条件](#2-capability)を満たさない） | 実行を中断し、条件不足である旨と必要条件を報告する |
| **競合**（他Skill・専門家の見解と矛盾） | 専門家の見解と一次情報を優先し、対立をDecision Logに記録。解決しなければ呼び出し元Agentに判断を委ねる |
| **リスク**（[Section 8 Human Judgment](#8-human-judgment)に該当する結果に至った） | 確定させず、選択肢＋推奨案として提示する |
| **一次情報で確認できない** | 「未確認」と明記し、Confidence を Low にして専門家または人間へ回す。二次情報で埋めない |
| **再実行** | [Section 5 Execution Framework](#5-execution-framework)のPlanに戻る。最大3回。同じ手法を繰り返さない（毎回変更点を記録） |
| **エスカレーション** | 3回の再実行でも未達、またはCritical相当のリスク（法令違反の疑い・資金ショート確定・認証情報の漏えいの疑い）を検出した場合、呼び出し元Agent経由で人間に引き上げる |

---

## 10. Performance

| 指標 | 定義 | 目標 |
|---|---|---|
| **Accuracy** | 初回実行でのPASS率 | ≧ 80%（[`Quality_Standard.md`](../../../00_System/Quality_Standard.md) 品質KPI準拠） |
| **Speed** | 実行の所要時間（タスク規模あたり） | WBS・予実・KPIの初期作成は1セッション以内。月次レビューは1回あたり短時間 |
| **Cost** | 実行あたりのトークン・検索コスト | 調査は一次情報に絞り、同じ情報を重複取得しない |
| **Token Efficiency** | 不要なコンテキストを持ち込まない | 必要な知識・入力・テンプレートのみ参照する |
| **Scalability** | 業種・地域が変わっても品質が劣化しないか | 業種・地域固有の情報は Input で注入し、Skill本体は非依存に保つ |

---

## 11. Reusability

| 項目 | 内容 |
|---|---|
| **利用可能Agent** | 主利用: `business-launch` ／ 副利用: `ceo`、`product-manager`、`growth` |
| **関連Skill** | `kpi-design`、`capital-planning`、`sns-marketing-framework` |
| **依存Skill** | `capital-planning`（資金繰り・予算の根拠） |

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
