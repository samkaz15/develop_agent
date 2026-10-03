---
skill_name: incorporation-legal
display_name: Incorporation & Legal Setup Skill
category: business
version: 1.0.0
status: Draft   # Draft / Active / Deprecated
owner: "@samkaz15"
created: 2026-10-03
updated: 2026-10-03
related_agents: [business-launch, ceo, security]
related_phases: [0, 1]
tags: [launch, legal, incorporation, compliance, filing]
---

# Incorporation & Legal Setup Skill

## 1. Skill Identity

| 項目 | 内容 |
|---|---|
| **Skill Name** | `incorporation-legal` |
| **Version** | `1.0.0` |
| **Category** | `business`（[`Skill_Architecture.md`](../../../00_System/Skill_Architecture.md) の7カテゴリに対応。Launch Track は [`launch/README.md`](../../../launch/README.md)） |
| **Purpose** | 法人形態の比較から設立手順・許認可・税務/社会保険の届出・契約/表示の論点までを出典付きで整理し、士業へ確認すべき論点と期限台帳に落とし込む能力。 |
| **Scope** | 日本国内の株式会社・合同会社の設立と開業までの法務・届出の整理（個人事業・海外法人・特殊法人は対象外） |
| **Related Domain** | 会社法・商業登記の実務、税務・社会保険の届出実務、広告・取引・個人情報に関する規制の基礎 |

```yaml
identity:
  skill_name: "incorporation-legal"
  category: "business"
  purpose: "Organize entity choice, incorporation steps, permits, filings and contract/disclosure issues with sources, and turn them into expert-review items and a deadline ledger."
```

---

## 2. Capability

### このSkillでできること
- 法人形態の比較表と、推奨・却下案の根拠を作る
- 商号・本店・事業目的・役員・事業年度などの基本事項を整理する
- 設立フロー・必要書類・WBS との対応を作る
- 許認可の要否の候補と、確認先（所管）を洗い出す
- 設立日・雇用日起算で期限が自動計算される届出台帳を作る
- 契約・規約・広告表示（特商法・景表法・個人情報保護）の論点を抽出する
- 士業への確認依頼文と、書類のドラフト案を作る

### できないこと

| できないこと | 理由 / 代替 |
|---|---|
| 法的・税務的な結論の断定 | 弁護士・税理士等が確認する。本Skillは論点整理と案まで |
| 登記・税務・社会保険・労働保険・許認可の申請代理 | 司法書士・税理士・社労士・行政書士の業務（独占業務を含む）。本人が自分で申請する場合も内容は専門家または公式の手引で確認する |
| 許認可の要否の断定 | 所管官庁・行政書士に確認する |
| 契約・規約の最終確定 | 弁護士が確認し、締結は人間が行う |
| 労務の詳細設計・給与の試算 | `labor-management`、`payroll-design` |

### 前提条件
- [ ] 事業内容、資本金案、本店所在地の想定、役員の案がある
- [ ] 対象が日本国内の株式会社・合同会社である

### 適用条件
- Launch Track L2〜L4、L7（法務表示）。事業目的・資本金・役員が変わるとき
- **適用しない状況**: 海外法人・NPO・特殊法人の設立、個別の紛争対応

### 制約事項
- 期限・費用・要件は目安として扱い、出典URLと確認日を付ける
- 自治体ごとに期限・様式が異なる項目は「自治体HPで確認」と明記する
- 専門家確認が済んでいない内容は確定扱いにしない

---

## 3. Required Knowledge

| 種別 | 内容 |
|---|---|
| **理論** | 会社法の基本構造（機関設計・定款の記載事項）、手続の時間軸（設立日起算・雇用日起算） |
| **ベストプラクティス** | 設立前に商号・事業目的・許認可を精査する／事業目的は将来事業も見据える／届出は期限台帳で管理する／専門家には論点を具体的に渡す |
| **フレームワーク** | 法人形態比較表、設立フロー、届出期限台帳（`legal-procedure-tracker.csv`）、士業の役割分担表 |
| **業界標準** | 会社法・商業登記法・法人税法・消費税法・健康保険法・厚生年金保険法・労働保険徴収法・雇用保険法・景品表示法・特定商取引法・個人情報保護法（条文・要件は一次情報で確認） |
| **参考ガイドライン** | 法務局・公証役場・国税庁・日本年金機構・厚生労働省・消費者庁・個人情報保護委員会の公式情報、[`launch/templates/legal-setup-plan.md`](../../../launch/templates/legal-setup-plan.md) |

法令・料率・制度の**具体的な数値は固定知識にしない**。使う都度、公式の一次情報で確認し、出典URLと確認日を記録する（[`launch/README.md` — 情報の鮮度ルール](../../../launch/README.md#情報の鮮度ルール)）。

---

## 4. Inputs

### 必須入力

| 入力 | 形式 | 説明 |
|---|---|---|
| 事業内容の説明 | Markdown | 許認可の要否判断の材料 |
| 資本金案・役員案・本店所在地の想定 | Markdown | `capital-planning` の結果を含む |
| 事業年度・設立希望時期 | Markdown | 期限台帳の起点 |

### 任意入力
- 雇用予定（時期・人数）
- 既に決まっている商号候補
- 希望する士業・予算

### Context / 前工程成果物 / 設定値

| 種別 | 内容 |
|---|---|
| **Context** | Launch Track L2〜L4。Gate L3 の前に専門家レビューを経る |
| **前工程成果物** | `launch-brief.md` §1・§4、`capital-plan.md` |
| **設定値** | 設立日・事業開始日・初回給与支払日・従業員雇用日（期限台帳の起算日） |

**入力不足の場合**: 推測で補完せず、不足項目を明示して呼び出し元（Agent/人間）に差し戻す（[Section 9 Error Handling](#9-error-handling)）。

---

## 5. Execution Framework

標準の実行フロー（Analyze → Plan → Execute → Validate → Optimize → Finalize）は [`Skill_Base_Template.md — Section 5`](../../../00_System/Skill_Base_Template.md#5-execution-framework) に従う。このSkillでの具体化は次のとおり。

| ステージ | このSkillでの型 |
|---|---|
| **Analyze** | 事業は許認可・特別な規制に関わるか。法人形態の選定に効く条件は何か |
| **Plan** | 形態比較 → 基本事項 → 手順 → 許認可 → 届出台帳 → 契約・表示の順。専門家に渡す論点を同時に抽出する |
| **Execute** | 公式の一次情報で要件・期限・費用を確認し、出典URLと確認日を付けて記録する |
| **Validate** | 断定していないか／専門家確認待ちが明示されているか／期限の起算点が正しいか |
| **Optimize** | 論点を「専門家に聞くこと」に絞り、依頼文を簡潔にする |
| **Finalize** | `legal-setup-plan.md`・`legal-procedure-tracker.csv`・確認依頼文を確定する |

**運用ルール**: Validate で未達の場合は Plan に戻る（手法選定から見直す）。3回繰り返しても未達の場合は [Section 9](#9-error-handling) のエスカレーションに従う。

---

## 6. Outputs

### 成果物

| 出力形式 | 用途 | 出力先 |
|---|---|---|
| **Markdown** | 法人設立・法務 セットアッププラン | `strategy/launch/legal-setup-plan.md` |
| **CSV** | 法務・届出 手続台帳（期限自動計算） | `strategy/launch/sheets/legal-procedure-tracker.csv` |
| **Checklist** | 設立〜開業チェック、専門家確認 | 成果物内、[`launch/checklists/`](../../../launch/checklists/) |
| **Recommendation** | 法人形態・資本金・許認可対応の選択肢と推奨 | 成果物内 |

このSkillが実際に生成するのは: Markdown（プラン）、CSV（手続台帳）、Checklist、Recommendation

---

## 7. Quality Criteria

### 完成条件（Definition of Done）
- [ ] 法人形態の比較と推奨・却下案の根拠がある
- [ ] 基本事項の表が埋まり、確定/未確定が分かる
- [ ] 届出台帳の全行に担当・起算点・期限（または確認先）がある
- [ ] 全ての要件・期限・費用に出典URLと確認日がある
- [ ] 専門家確認が必要な項目に「専門家確認待ち」が付いている
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

- [ ] **ブランド**: 商号・屋号の最終決定
- [ ] **倫理**: 実質的支配者の申告など、虚偽のない正確な記載（虚偽記載をAIが促さない）
- [ ] **法務**: **全て**。法人形態・商号・事業目的・役員・定款・許認可・契約・規約・広告表示は専門家確認を経て人間が確定する
- [ ] **最終意思決定**: 法人形態・設立内容の確定（Gate L3）／士業の選定・依頼
- [ ] 課税事業者の選択・インボイス登録の判断（税理士確認）

---

## 9. Error Handling

| 状況 | 対応 |
|---|---|
| **入力不足** | 推測で補完せず、[Section 4 Inputs](#4-inputs)の不足項目を明示して差し戻す |
| **条件不足**（[Section 2 適用条件](#2-capability)を満たさない） | 実行を中断し、条件不足である旨と必要条件を報告する |
| **競合**（他Skill・専門家の見解と矛盾） | 専門家の見解と一次情報を優先し、対立をDecision Logに記録。解決しなければ呼び出し元Agentに判断を委ねる |
| **リスク**（[Section 8 Human Judgment](#8-human-judgment)に該当する結果に至った） | 確定させず、選択肢＋推奨案として提示する |
| **一次情報で確認できない** | 「未確認」と明記し、Confidence を Low にして専門家または人間へ回す。二次情報で埋めない |
| **期限切れ・期限直前の手続** | 期限日・影響・対応案を即座に人間と該当の専門家へ報告する |
| **再実行** | [Section 5 Execution Framework](#5-execution-framework)のPlanに戻る。最大3回。同じ手法を繰り返さない（毎回変更点を記録） |
| **エスカレーション** | 3回の再実行でも未達、またはCritical相当のリスク（法令違反の疑い・資金ショート確定・認証情報の漏えいの疑い）を検出した場合、呼び出し元Agent経由で人間に引き上げる |

---

## 10. Performance

| 指標 | 定義 | 目標 |
|---|---|---|
| **Accuracy** | 初回実行でのPASS率 | ≧ 80%（[`Quality_Standard.md`](../../../00_System/Quality_Standard.md) 品質KPI準拠） |
| **Speed** | 実行の所要時間（タスク規模あたり） | 1セッション以内（形態比較〜台帳） |
| **Cost** | 実行あたりのトークン・検索コスト | 調査は一次情報に絞り、同じ情報を重複取得しない |
| **Token Efficiency** | 不要なコンテキストを持ち込まない | 必要な知識・入力・テンプレートのみ参照する |
| **Scalability** | 業種・地域が変わっても品質が劣化しないか | 業種・地域固有の情報は Input で注入し、Skill本体は非依存に保つ |

---

## 11. Reusability

| 項目 | 内容 |
|---|---|
| **利用可能Agent** | 主利用: `business-launch` ／ 副利用: `ceo`、`security` |
| **関連Skill** | `labor-management`、`capital-planning`、`back-office-design`、`business-strategy` |
| **依存Skill** | `capital-planning`（資本金案） |

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
