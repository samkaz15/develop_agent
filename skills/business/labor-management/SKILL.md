---
skill_name: labor-management
display_name: Labor Management Skill
category: business
version: 1.0.0
status: Draft   # Draft / Active / Deprecated
owner: "@samkaz15"
created: 2026-10-03
updated: 2026-10-03
related_agents: [business-launch, ceo]
related_phases: [0, 16]
tags: [launch, labor, hr, social-insurance, regulations]
---

# Labor Management Skill

## 1. Skill Identity

| 項目 | 内容 |
|---|---|
| **Skill Name** | `labor-management` |
| **Version** | `1.0.0` |
| **Category** | `business`（[`Skill_Architecture.md`](../../../00_System/Skill_Architecture.md) の7カテゴリに対応。Launch Track は [`launch/README.md`](../../../launch/README.md)） |
| **Purpose** | 雇用・社会保険/労働保険・書面・規程・運用カレンダーを整理し、社労士に確認すべき論点と手続の期限に落とし込む能力。 |
| **Scope** | 立ち上げ期の労務（雇用形態・保険の適用論点・必要書面と規程・月次/年次運用・雇用開始チェック）。給与の試算は `payroll-design` |
| **Related Domain** | 労働法の基礎、社会保険・労働保険の実務 |

```yaml
identity:
  skill_name: "labor-management"
  category: "business"
  purpose: "Organize employment, insurance enrollment, documents, internal rules and operating calendar into items for labor-expert review and filing deadlines."
```

---

## 2. Capability

### このSkillでできること
- 役員・従業員・業務委託・副業人材の関わり方を整理し、注意点を指摘する
- 社会保険・労働保険の適用判断の論点を表にする
- 必要な書面・規程（労働条件通知書・就業規則・36協定 など）の要否と状態を管理する
- 月次・年次の労務運用カレンダーを作る
- 採用・雇用開始時のチェックリストを作る
- 雇用関連の助成金との接続点（雇う前に確認すべきこと）を指摘する

### できないこと

| できないこと | 理由 / 代替 |
|---|---|
| 手続の代理（資格取得・適用事業所の届出 など） | 社会保険労務士の業務。人間または社労士が実施する |
| 労働者性の最終判断（業務委託か雇用か） | 社労士・弁護士に確認する |
| 就業規則・契約書の最終確定 | 社労士・弁護士が確認する |
| 労務紛争の対応 | 弁護士・社労士 |
| 給与・社保料の試算 | `payroll-design` Skill |

### 前提条件
- [ ] 雇用予定（人数・時期・形態）が分かっている
- [ ] 事業内容と本店所在地の想定がある

### 適用条件
- Launch Track L4〜L5。最初の雇用の前、働き方・人数が変わるとき
- **適用しない状況**: 給与額の試算（→ `payroll-design`）、法人設立そのもの（→ `incorporation-legal`）

### 制約事項
- 要件・期限・料率は確認日付きで記録する
- 実態と書面を一致させる（実態に合わない規程は作らない）

---

## 3. Required Knowledge

| 種別 | 内容 |
|---|---|
| **理論** | 労働法の基本構造（労働条件の明示・労働時間・賃金・社会保険/労働保険の適用） |
| **ベストプラクティス** | 雇う前に労働条件を書面で確定する／手続期限は台帳で管理する／規程は実態に合わせる／偽装請負・不利益な運用を設計しない |
| **フレームワーク** | 保険適用判断表、書面・規程チェックリスト、運用カレンダー、雇用開始チェック |
| **業界標準** | 労働基準法・労働契約法・最低賃金法・労働安全衛生法・健康保険法・厚生年金保険法・労働保険徴収法・雇用保険法・育児介護休業法・フリーランス保護法 等（要件は一次情報で確認） |
| **参考ガイドライン** | 厚生労働省・労働基準監督署・ハローワーク・日本年金機構の公式情報、[`launch/templates/labor-setup-plan.md`](../../../launch/templates/labor-setup-plan.md) |

法令・料率・制度の**具体的な数値は固定知識にしない**。使う都度、公式の一次情報で確認し、出典URLと確認日を記録する（[`launch/README.md` — 情報の鮮度ルール](../../../launch/README.md#情報の鮮度ルール)）。

---

## 4. Inputs

### 必須入力

| 入力 | 形式 | 説明 |
|---|---|---|
| 雇用予定（人数・時期・形態） | Markdown | 役員のみ／従業員／業務委託 |
| 事業内容・所在地 | Markdown | 業種・都道府県で扱いが変わる |
| 役員報酬案・給与案 | CSV | `payroll-simulation.csv` |

### 任意入力
- 勤務時間・残業の見込み
- 副業人材・フリーランスの予定
- 希望する社労士・ツール

### Context / 前工程成果物 / 設定値

| 種別 | 内容 |
|---|---|
| **Context** | Launch Track L4〜L5 |
| **前工程成果物** | `legal-procedure-tracker.csv`、`payroll-simulation.csv` |
| **設定値** | 従業員雇用日（期限台帳の起算日）、所定労働時間 |

**入力不足の場合**: 推測で補完せず、不足項目を明示して呼び出し元（Agent/人間）に差し戻す（[Section 9 Error Handling](#9-error-handling)）。

---

## 5. Execution Framework

標準の実行フロー（Analyze → Plan → Execute → Validate → Optimize → Finalize）は [`Skill_Base_Template.md — Section 5`](../../../00_System/Skill_Base_Template.md#5-execution-framework) に従う。このSkillでの具体化は次のとおり。

| ステージ | このSkillでの型 |
|---|---|
| **Analyze** | 誰をどの形態で関わらせるか。適用される保険・必要な書面は何か |
| **Plan** | 形態整理 → 適用判断 → 書面・規程 → 運用カレンダー → 採用チェックの順で進める |
| **Execute** | 公式の一次情報で要件を確認し、出典URLと確認日を付けて表に記録する |
| **Validate** | 断定していないか／社労士確認待ちが明示されているか／期限が台帳と整合しているか |
| **Optimize** | 今必要な書面・規程に絞り、将来必要になるものは時期付きで後送りにする |
| **Finalize** | `labor-setup-plan.md` と台帳への反映事項を確定する |

**運用ルール**: Validate で未達の場合は Plan に戻る（手法選定から見直す）。3回繰り返しても未達の場合は [Section 9](#9-error-handling) のエスカレーションに従う。

---

## 6. Outputs

### 成果物

| 出力形式 | 用途 | 出力先 |
|---|---|---|
| **Markdown** | 労務・給与 セットアッププラン | `strategy/launch/labor-setup-plan.md` |
| **Checklist** | 雇用開始チェック・書面と規程の状態 | 成果物内 |
| **Recommendation** | 雇用形態・規程整備の優先順位 | 成果物内 |

このSkillが実際に生成するのは: Markdown（プラン）、Checklist、Recommendation

---

## 7. Quality Criteria

### 完成条件（Definition of Done）
- [ ] 雇用形態ごとの注意点が整理されている
- [ ] 保険の適用論点が表になり、確認先が明記されている
- [ ] 必要な書面・規程の要否と担当が一覧になっている
- [ ] 運用カレンダーが月次・年次で作られている
- [ ] 専門家確認が必要な項目に「社労士確認待ち」が付いている
- [ ] Decision Log（判断根拠）が記録されている
- [ ] [Section 6 Outputs](#6-outputs)の形式に準拠している

### 品質基準
[`Quality_Standard.md`](../../../00_System/Quality_Standard.md) の共通5基準（明瞭さ・簡潔さ・一貫性・検証可能性・誠実さ）を適用する。このSkillでは特に **検証可能性（出典・確認日）と誠実さ（断定しない）** を重視する。

### 判定基準

| 判定 | 条件 |
|---|---|
| ✅ **PASS** | 完成条件・品質基準を全て満たし証拠添付済み |
| ⚠️ **WARNING** | 必須は満たすが軽微な懸念あり（Open Issues登録・持ち越し2工程まで） |
| ❌ **FAIL** | 完成条件未達、または重大指摘あり（出典のない数値・専門家領域の断定・認証情報の混入 など） |

---

## 8. Human Judgment

このSkillの実行結果が以下に該当する場合、判断を確定させず選択肢＋推奨案として人間に提示する（[`Review_Process.md — Human Decision Framework`](../../../00_System/Review_Process.md#human-decision-framework) に加えて）:

- [ ] **ブランド**: 働き方・組織文化の方針
- [ ] **倫理**: 偽装請負、長時間労働を前提とした設計、不利益な労働条件を設計しない
- [ ] **法務**: 雇用契約・就業規則・36協定・労働者性・保険の適用は、社労士・弁護士の確認を経て確定する
- [ ] **最終意思決定**: 雇用の採否・雇用条件・規程の内容
- [ ] 雇用関連助成金を使う場合の雇用計画（雇う前の確認）

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
| **Speed** | 実行の所要時間（タスク規模あたり） | 1セッション以内 |
| **Cost** | 実行あたりのトークン・検索コスト | 調査は一次情報に絞り、同じ情報を重複取得しない |
| **Token Efficiency** | 不要なコンテキストを持ち込まない | 必要な知識・入力・テンプレートのみ参照する |
| **Scalability** | 業種・地域が変わっても品質が劣化しないか | 業種・地域固有の情報は Input で注入し、Skill本体は非依存に保つ |

---

## 11. Reusability

| 項目 | 内容 |
|---|---|
| **利用可能Agent** | 主利用: `business-launch` ／ 副利用: `ceo` |
| **関連Skill** | `payroll-design`、`incorporation-legal`、`back-office-design`、`subsidy-research` |
| **依存Skill** | `incorporation-legal`（設立日・届出台帳） |

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
