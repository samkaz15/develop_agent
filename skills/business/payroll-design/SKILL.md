---
skill_name: payroll-design
display_name: Payroll Design Skill
category: business
version: 1.0.0
status: Draft   # Draft / Active / Deprecated
owner: "@samkaz15"
created: 2026-10-03
updated: 2026-10-03
related_agents: [business-launch, ceo]
related_phases: [0, 1]
tags: [launch, payroll, salary, executive-compensation, simulation]
---

# Payroll Design Skill

## 1. Skill Identity

| 項目 | 内容 |
|---|---|
| **Skill Name** | `payroll-design` |
| **Version** | `1.0.0` |
| **Category** | `business`（[`Skill_Architecture.md`](../../../00_System/Skill_Architecture.md) の7カテゴリに対応。Launch Track は [`launch/README.md`](../../../launch/README.md)） |
| **Purpose** | 役員報酬・従業員給与をシナリオ別に、手取り・会社総コスト・法定福利費・損益分岐を最新料率で試算し、適正な給与水準の選択肢と根拠を提示する能力。 |
| **Scope** | 立ち上げ期の給与設計の試算（役員報酬・従業員給与・総人件費・最低賃金チェック・料率の更新管理） |
| **Related Domain** | 人件費管理、損益分岐点分析、社会保険・労働保険・税制の基礎 |

```yaml
identity:
  skill_name: "payroll-design"
  category: "business"
  purpose: "Simulate executive and employee pay by scenario (take-home, total company cost, statutory benefits, break-even) and present options with evidence."
```

---

## 2. Capability

### このSkillでできること
- 最低限・標準・成長の3シナリオで手取りと会社総コストを比較する
- 健康保険・介護保険・厚生年金・雇用保険・労災の概算を試算する
- 時給換算による地域別最低賃金のチェックを行う
- その給与を賄うために必要な月次粗利（損益分岐の目安）を示す
- 定期同額給与など、決定前に税理士へ確認すべき論点を提示する
- 料率パラメータに出典URL・確認日を付けて更新管理する

### できないこと

| できないこと | 理由 / 代替 |
|---|---|
| 源泉所得税・住民税・社会保険料の確定額の算出 | 標準報酬月額・個別事情で決まる。社労士・税理士・給与計算ツールで確定する |
| 役員報酬の損金算入・節税の最終判断 | 税理士に確認する |
| 給与額の決定 | Owner が決定する |
| 雇用手続・規程の設計 | `labor-management` Skill |

### 前提条件
- [ ] 所在地（都道府県）と対象年度が分かっている
- [ ] 役員か従業員か、雇用形態が分かっている
- [ ] 月次の支払能力の見込み（粗利）の仮置きがある

### 適用条件
- Launch Track L1。役員報酬の決定前、採用の前、給与改定時
- **適用しない状況**: 源泉徴収・年末調整の確定計算（給与計算ツール・税理士）

### 制約事項
- 料率は年度・都道府県で変わるため、例示値のまま意思決定に使わない（確認日が空なら FAIL）
- 標準報酬月額の等級による差があるため試算は概算と明記する

---

## 3. Required Knowledge

| 種別 | 内容 |
|---|---|
| **理論** | 総額人件費（額面＋法定福利費）、損益分岐点分析 |
| **ベストプラクティス** | 生活費の必要額・会社の支払能力・手取りの3視点で比較する／料率は更新日を記録する／役員報酬は決める前に税理士へ確認する |
| **フレームワーク** | `payroll-simulation.csv`（パラメータ表＋3シナリオ）、会社総コスト＝額面＋法定福利費、時給換算チェック |
| **業界標準** | 健康保険法・厚生年金保険法・雇用保険法・労働者災害補償保険法・最低賃金法・法人税法（定期同額給与の考え方） |
| **参考ガイドライン** | 協会けんぽの都道府県別保険料額表、日本年金機構、厚生労働省（雇用保険料率・最低賃金）、国税庁（源泉徴収税額表）、[`launch/templates/labor-setup-plan.md`](../../../launch/templates/labor-setup-plan.md) |

法令・料率・制度の**具体的な数値は固定知識にしない**。使う都度、公式の一次情報で確認し、出典URLと確認日を記録する（[`launch/README.md` — 情報の鮮度ルール](../../../launch/README.md#情報の鮮度ルール)）。

---

## 4. Inputs

### 必須入力

| 入力 | 形式 | 説明 |
|---|---|---|
| 所在地・対象年度 | Markdown | 料率・最低賃金の参照先を決める |
| 対象者の区分と人数 | Markdown | 役員／従業員、40歳以上の有無 |
| 生活費の必要額・支払能力の仮置き | Markdown | シナリオ設定の根拠 |

### 任意入力
- 賞与・手当の方針
- 副業・扶養の事情（本人が確認）
- 希望手取り額

### Context / 前工程成果物 / 設定値

| 種別 | 内容 |
|---|---|
| **Context** | Launch Track L1。`capital-planning` と往復して整合させる |
| **前工程成果物** | `cashflow-plan.csv`（粗利見込）、`labor-setup-plan.md` |
| **設定値** | 都道府県、年度、社会保険の事業主負担割合、月所定労働時間、地域別最低賃金 |

**入力不足の場合**: 推測で補完せず、不足項目を明示して呼び出し元（Agent/人間）に差し戻す（[Section 9 Error Handling](#9-error-handling)）。

---

## 5. Execution Framework

標準の実行フロー（Analyze → Plan → Execute → Validate → Optimize → Finalize）は [`Skill_Base_Template.md — Section 5`](../../../00_System/Skill_Base_Template.md#5-execution-framework) に従う。このSkillでの具体化は次のとおり。

| ステージ | このSkillでの型 |
|---|---|
| **Analyze** | 誰の給与を、どの条件で、何のために決めるのか。支払能力はどの程度か |
| **Plan** | 料率の確認・更新 → シナリオ設定 → 試算 → 損益分岐の接続の順で進める |
| **Execute** | 最新の公表値でパラメータを更新し、確認日と出典を記録して `payroll-simulation.csv` を計算する |
| **Validate** | 料率の確認日が記入されているか／最低賃金を満たすか／資金繰りと整合するか |
| **Optimize** | シナリオを3つに絞り、判断に効く差分（手取り・総コスト・必要粗利）だけを示す |
| **Finalize** | `payroll-simulation.csv` と、`cashflow-plan.csv` への連携値を確定する |

**運用ルール**: Validate で未達の場合は Plan に戻る（手法選定から見直す）。3回繰り返しても未達の場合は [Section 9](#9-error-handling) のエスカレーションに従う。

---

## 6. Outputs

### 成果物

| 出力形式 | 用途 | 出力先 |
|---|---|---|
| **CSV** | 適正給料シミュレーション（パラメータ表＋3シナリオ） | `strategy/launch/sheets/payroll-simulation.csv` |
| **Recommendation** | 給与水準の選択肢と推奨・税理士/社労士への確認事項 | `labor-setup-plan.md` §4・Handoff Note |

このSkillが実際に生成するのは: CSV（給与シミュレーション）と Recommendation

---

## 7. Quality Criteria

### 完成条件（Definition of Done）
- [ ] 全パラメータに出典URLと確認日があり、例示値が最新値に更新されている
- [ ] 3シナリオの手取り・会社総コスト・必要な月次粗利が出ている
- [ ] 最低賃金チェックが実施されている（従業員の場合）
- [ ] 税理士・社労士に確認すべき論点が列挙されている
- [ ] Decision Log（判断根拠）が記録されている
- [ ] [Section 6 Outputs](#6-outputs)の形式に準拠している

### 品質基準
[`Quality_Standard.md`](../../../00_System/Quality_Standard.md) の共通5基準（明瞭さ・簡潔さ・一貫性・検証可能性・誠実さ）を適用する。このSkillでは特に **検証可能性（料率の出典・確認日）と正確性（例示値の更新）** を重視する。

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
- [ ] **倫理**: 最低賃金未満・不当な賃金控除・未払いを前提にした設計をしない
- [ ] **法務**: 役員報酬の損金算入、社会保険の加入要否・負担は税理士・社労士の確認を経る
- [ ] **最終意思決定**: 役員報酬・給与水準の決定／採用の可否
- [ ] 生活費の必要額と会社の支払能力のトレードオフ

---

## 9. Error Handling

| 状況 | 対応 |
|---|---|
| **入力不足** | 推測で補完せず、[Section 4 Inputs](#4-inputs)の不足項目を明示して差し戻す |
| **条件不足**（[Section 2 適用条件](#2-capability)を満たさない） | 実行を中断し、条件不足である旨と必要条件を報告する |
| **競合**（他Skill・専門家の見解と矛盾） | 専門家の見解と一次情報を優先し、対立をDecision Logに記録。解決しなければ呼び出し元Agentに判断を委ねる |
| **リスク**（[Section 8 Human Judgment](#8-human-judgment)に該当する結果に至った） | 確定させず、選択肢＋推奨案として提示する |
| **一次情報で確認できない** | 「未確認」と明記し、Confidence を Low にして専門家または人間へ回す。二次情報で埋めない |
| **料率の確認日が空欄・古い** | 例示値のまま意思決定に使わない。最新の公表値で更新するまで FAIL とし、更新後に再実行する |
| **再実行** | [Section 5 Execution Framework](#5-execution-framework)のPlanに戻る。最大3回。同じ手法を繰り返さない（毎回変更点を記録） |
| **エスカレーション** | 3回の再実行でも未達、またはCritical相当のリスク（法令違反の疑い・資金ショート確定・認証情報の漏えいの疑い）を検出した場合、呼び出し元Agent経由で人間に引き上げる |

---

## 10. Performance

| 指標 | 定義 | 目標 |
|---|---|---|
| **Accuracy** | 初回実行でのPASS率 | ≧ 80%（[`Quality_Standard.md`](../../../00_System/Quality_Standard.md) 品質KPI準拠） |
| **Speed** | 実行の所要時間（タスク規模あたり） | 1セッション以内 |
| **Cost** | 実行あたりのトークン・検索コスト | 調査は一次情報に絞り、同じ情報を重複取得しない |
| **Token Efficiency** | 不要なコンテキストを持ち込まない | 必要な知識・入力・テンプレートのみ参照する |
| **Scalability** | 業種・地域が変わっても品質が劣化しないか | 業種・地域固有の情報は Input で注入し、Skill本体は非依存に保つ |

---

## 11. Reusability

| 項目 | 内容 |
|---|---|
| **利用可能Agent** | 主利用: `business-launch` ／ 副利用: `ceo` |
| **関連Skill** | `labor-management`、`capital-planning`、`incorporation-legal` |
| **依存Skill** | `capital-planning`（粗利見込）、`labor-management`（雇用形態） |

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
