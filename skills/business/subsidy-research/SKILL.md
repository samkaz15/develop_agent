---
skill_name: subsidy-research
display_name: Subsidy Research Skill
category: business
version: 1.0.0
status: Draft   # Draft / Active / Deprecated
owner: "@samkaz15"
created: 2026-10-03
updated: 2026-10-03
related_agents: [business-launch, ceo, market-research]
related_phases: [0, 1]
tags: [launch, subsidy, grant, loan, regional]
---

# Subsidy Research Skill

## 1. Skill Identity

| 項目 | 内容 |
|---|---|
| **Skill Name** | `subsidy-research` |
| **Version** | `1.0.0` |
| **Category** | `business`（[`Skill_Architecture.md`](../../../00_System/Skill_Architecture.md) の7カテゴリに対応。Launch Track は [`launch/README.md`](../../../launch/README.md)） |
| **Purpose** | 国・都道府県・市区町村・支援機関の補助金・助成金・融資・税制を公式の一次情報で収集し、要件適合度・想定受給額・期限・リスクを評価して申請判断の材料にする能力。 |
| **Scope** | 地域階層（国→都道府県→市区町村→支援機関）での制度収集・適合度評価・申請カレンダー・台帳更新 |
| **Related Domain** | 公的支援制度の実務、創業支援・雇用関連助成金の基礎 |

```yaml
identity:
  skill_name: "subsidy-research"
  category: "business"
  purpose: "Collect subsidies, grants, loans and tax incentives from official sources by region and evaluate fit, amount, deadline and risk for the application decision."
```

---

## 2. Capability

### このSkillでできること
- 地域階層ごとに制度を収集し、公式の公募要領で要件・補助率・上限・公募期間・申請方法を確認する
- 適合度（要件・想定受給額・準備の労力・期限）を High/Mid/Low で評価する
- 交付決定前の着手の可否・支払方式（後払い）・実績報告の義務を抽出する
- 申請カレンダーと準備期限を作る
- 新着の定点調査で台帳を更新する

### できないこと

| できないこと | 理由 / 代替 |
|---|---|
| 採択・受給の保証 | 実施機関の審査による。見込みは確度として示す |
| 申請の実行・申請書の最終確認 | 人間が実行し、申請書は専門家・支援機関がレビューする |
| 要件の最終解釈 | 実施機関・相談窓口に確認する |
| 非公式情報（まとめサイト・SNS等）を根拠にした案内 | 手がかりとしてのみ使い、必ず公式の一次情報で裏取りする |

### 前提条件
- [ ] 本店所在地（都道府県・市区町村）の想定がある（未定なら全国制度のみ調査し、地域別は保留）
- [ ] 事業内容・業種、設立予定日、雇用予定、投資予定（対象経費）が分かっている

### 適用条件
- Launch Track L6。設立前から着手する（設立前でないと使えない制度・交付決定前の発注禁止があるため）
- **適用しない状況**: 申請書の作成・提出の実行

### 制約事項
- 公募期間・要件・予算の状況は**使う都度**公式で確認する（過去情報で案内しない）
- 出典は国・自治体・支援機関の公式サイトのみ
- 交付決定前の発注・契約・支払を促さない

---

## 3. Required Knowledge

| 種別 | 内容 |
|---|---|
| **理論** | 公的支援制度の類型（補助金・助成金・融資・保証・税制）と、それぞれの受給の仕組み |
| **ベストプラクティス** | 公募要領を読む／交付決定前に発注しない／後払いにはつなぎ資金を用意する／雇用関連助成金は雇う前に計画届が必要な場合がある／自治体の創業支援（特定創業支援等事業など）を受けると登録免許税の軽減等が受けられる場合がある（要確認） |
| **フレームワーク** | 地域階層（国→都道府県→市区町村→支援機関）、適合度スコア、申請カレンダー、`subsidy-tracker.csv` |
| **業界標準** | 各制度の公募要領・交付要綱、補助金等に係る予算の執行の適正化に関する法律（基本） |
| **参考ガイドライン** | 国の補助金の電子申請・公募ポータル、中小企業向け支援情報ポータル、厚生労働省（雇用関連助成金）、日本政策金融公庫、信用保証協会、自治体の産業振興（創業支援）窓口、商工会議所・商工会、よろず支援拠点、[`launch/README.md` — 補助金・助成金の地域別収集ルール](../../../launch/README.md#補助金助成金の地域別収集ルール) |

法令・料率・制度の**具体的な数値は固定知識にしない**。使う都度、公式の一次情報で確認し、出典URLと確認日を記録する（[`launch/README.md` — 情報の鮮度ルール](../../../launch/README.md#情報の鮮度ルール)）。

---

## 4. Inputs

### 必須入力

| 入力 | 形式 | 説明 |
|---|---|---|
| 本店所在地の想定 | Markdown | 都道府県・市区町村 |
| 事業内容・業種 | Markdown | 対象要件の判断 |
| 設立予定日・雇用予定・投資予定 | Markdown | 対象期間・対象経費の判断 |

### 任意入力
- 代表者の属性（創業予定者など）
- 既に相談している窓口
- 希望する受給時期

### Context / 前工程成果物 / 設定値

| 種別 | 内容 |
|---|---|
| **Context** | Launch Track L6。`capital-planning` と連携（入金時期を資金繰りに反映） |
| **前工程成果物** | `launch-brief.md` §0・§1、`capital-plan.md` |
| **設定値** | 調査地域、調査日（確認日）、評価の重み |

**入力不足の場合**: 推測で補完せず、不足項目を明示して呼び出し元（Agent/人間）に差し戻す（[Section 9 Error Handling](#9-error-handling)）。

---

## 5. Execution Framework

標準の実行フロー（Analyze → Plan → Execute → Validate → Optimize → Finalize）は [`Skill_Base_Template.md — Section 5`](../../../00_System/Skill_Base_Template.md#5-execution-framework) に従う。このSkillでの具体化は次のとおり。

| ステージ | このSkillでの型 |
|---|---|
| **Analyze** | どの地域・業種・時期で使える制度があり得るか。設立前に動くべきものは何か |
| **Plan** | 地域階層ごとの調査 → 公募要領の確認 → 適合度評価 → カレンダー化の順で進める |
| **Execute** | 公式サイトで制度を確認し、出典URLと確認日を付けて台帳に記録する |
| **Validate** | 公式情報のみか／交付決定前の着手可否・支払方式が記載されているか／期限が最新か |
| **Optimize** | 適合度の高い制度に絞り、準備の優先順位を付ける |
| **Finalize** | `subsidy-tracker.csv` と、資金繰りへの入金見込みを確定する |

**運用ルール**: Validate で未達の場合は Plan に戻る（手法選定から見直す）。3回繰り返しても未達の場合は [Section 9](#9-error-handling) のエスカレーションに従う。

---

## 6. Outputs

### 成果物

| 出力形式 | 用途 | 出力先 |
|---|---|---|
| **CSV** | 補助金・助成金・融資 リサーチ台帳 | `strategy/launch/sheets/subsidy-tracker.csv` |
| **Report** | 調査メモ（地域別・出典付き） | `strategy/launch/` 配下 |
| **Recommendation** | 申請候補の優先順位と、申請判断の材料 | 成果物内 |

このSkillが実際に生成するのは: CSV（リサーチ台帳）、Report（調査メモ）、Recommendation（申請候補）

---

## 7. Quality Criteria

### 完成条件（Definition of Done）
- [ ] 国・都道府県・市区町村・支援機関の各階層を調べた（または保留の理由がある）
- [ ] 全制度に公式の出典URLと確認日がある
- [ ] 交付決定前の着手可否・支払方式・実績報告が記載されている
- [ ] 適合度と準備期限が付き、申請カレンダーがある
- [ ] Decision Log（判断根拠）が記録されている
- [ ] [Section 6 Outputs](#6-outputs)の形式に準拠している

### 品質基準
[`Quality_Standard.md`](../../../00_System/Quality_Standard.md) の共通5基準（明瞭さ・簡潔さ・一貫性・検証可能性・誠実さ）を適用する。このSkillでは特に **検証可能性（公式の一次情報・確認日）と誠実さ（受給を保証しない）** を重視する。

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
- [ ] **倫理**: 目的外使用・虚偽申請・水増しにつながる設計をしない
- [ ] **法務**: 申請内容・誓約事項の確認は専門家・支援機関へ
- [ ] **最終意思決定**: 申請するか／補助事業のために投資するか
- [ ] 交付決定前の発注・契約・支払をしてよいか（原則しない）

---

## 9. Error Handling

| 状況 | 対応 |
|---|---|
| **入力不足** | 推測で補完せず、[Section 4 Inputs](#4-inputs)の不足項目を明示して差し戻す |
| **条件不足**（[Section 2 適用条件](#2-capability)を満たさない） | 実行を中断し、条件不足である旨と必要条件を報告する |
| **競合**（他Skill・専門家の見解と矛盾） | 専門家の見解と一次情報を優先し、対立をDecision Logに記録。解決しなければ呼び出し元Agentに判断を委ねる |
| **リスク**（[Section 8 Human Judgment](#8-human-judgment)に該当する結果に至った） | 確定させず、選択肢＋推奨案として提示する |
| **一次情報で確認できない** | 「未確認」と明記し、Confidence を Low にして専門家または人間へ回す。二次情報で埋めない |
| **公募が終了・予算消化・要件変更** | 最新の状況で台帳を更新し、次回公募の見込みを「未確認」として記録する |
| **再実行** | [Section 5 Execution Framework](#5-execution-framework)のPlanに戻る。最大3回。同じ手法を繰り返さない（毎回変更点を記録） |
| **エスカレーション** | 3回の再実行でも未達、またはCritical相当のリスク（法令違反の疑い・資金ショート確定・認証情報の漏えいの疑い）を検出した場合、呼び出し元Agent経由で人間に引き上げる |

---

## 10. Performance

| 指標 | 定義 | 目標 |
|---|---|---|
| **Accuracy** | 初回実行でのPASS率 | ≧ 80%（[`Quality_Standard.md`](../../../00_System/Quality_Standard.md) 品質KPI準拠） |
| **Speed** | 実行の所要時間（タスク規模あたり） | 1地域あたり1セッション以内（定点調査は短時間） |
| **Cost** | 実行あたりのトークン・検索コスト | 調査は一次情報に絞り、同じ情報を重複取得しない |
| **Token Efficiency** | 不要なコンテキストを持ち込まない | 必要な知識・入力・テンプレートのみ参照する |
| **Scalability** | 業種・地域が変わっても品質が劣化しないか | 業種・地域固有の情報は Input で注入し、Skill本体は非依存に保つ |

---

## 11. Reusability

| 項目 | 内容 |
|---|---|
| **利用可能Agent** | 主利用: `business-launch` ／ 副利用: `ceo`、`market-research` |
| **関連Skill** | `capital-planning`、`incorporation-legal`、`labor-management` |
| **依存Skill** | なし |

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
