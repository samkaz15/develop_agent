---
skill_name: company-analysis
display_name: Company Analysis Skill
category: business
version: 1.0.0
status: Draft   # Draft / Active / Deprecated
owner: "@samkaz15"
created: 2026-10-03
updated: 2026-10-03
related_agents: [business-launch, ceo, market-research, growth]
related_phases: [0, 1]
tags: [launch, analysis, competitor, benchmark]
---

# Company Analysis Skill

## 1. Skill Identity

| 項目 | 内容 |
|---|---|
| **Skill Name** | `company-analysis` |
| **Version** | `1.0.0` |
| **Category** | `business`（[`Skill_Architecture.md`](../../../00_System/Skill_Architecture.md) の7カテゴリに対応。Launch Track は [`launch/README.md`](../../../launch/README.md)） |
| **Purpose** | 競合・ベンチマーク企業の事業・収益・集客・組織を事実と解釈に分けて分析し、自社への示唆（取り入れる／避ける／検証する）に変換する能力。 |
| **Scope** | 個別企業の深掘り（最低3社）・比較表・ポジショニング・SWOT。市場全体の調査は `market-research` |
| **Related Domain** | 競争戦略、ビジネスモデル分析、デジタルマーケティング |

```yaml
identity:
  skill_name: "company-analysis"
  category: "business"
  purpose: "Analyze competitor/benchmark companies separating fact from insight and convert findings into implications for our business."
```

---

## 2. Capability

### このSkillでできること
- 公開情報から事業・価格・収益モデル・集客・SNS運用・強み弱みを整理する
- 最低3社の比較表と、個社の深掘りを作成する
- ポジショニングマップで空白地帯を特定する
- レビュー・口コミから不満（ペイン）を抽出する
- 事実（Fact）と解釈（Insight）を分け、自社への So What に変換する

### できないこと

| できないこと | 理由 / 代替 |
|---|---|
| 非公開情報の入手・不正な情報収集 | 公開情報のみ。利用規約・著作権・不正競争防止法に反する収集は行わない |
| 財務数値の推測を事実として記載すること | 公開されていない数値は「推定」と明記し根拠を示す。確認できなければ「未確認」 |
| 市場規模の推計・トレンド分析 | `market-research` Skill / Agent |
| 他社への誹謗・事実無根の評価 | 出典のある事実のみ記載する |

### 前提条件
- [ ] 調査目的（答えるべき問い）が定義されている
- [ ] 対象企業のリスト、または選定基準がある

### 適用条件
- ビジネスモデル・価格・SNS戦略を設計する前（Launch Track L0, L7）
- **適用しない状況**: 自社（創業者）の分析（→ `self-analysis`）

### 制約事項
- 一次情報（公式サイト・開示資料）を優先し、二次情報は手がかりに留める
- 各情報に出典URLと確認日を付ける
- サイトの利用規約・著作権に従う（引用の範囲を守る）

---

## 3. Required Knowledge

| 種別 | 内容 |
|---|---|
| **理論** | 競争戦略（ファイブフォース分析）、ビジネスモデル分析 |
| **ベストプラクティス** | 事実と解釈を分離する／一次情報を優先する／比較は同じ観点・同じ時点で行う／「真似る型」と「避ける型」を分ける |
| **フレームワーク** | 3C、SWOT、ポジショニングマップ、ビジネスモデルキャンバスの比較、レビューマイニング |
| **業界標準** | 公開情報の取扱い（著作権法・不正競争防止法・各サイトの利用規約）。迷う場合は弁護士に確認 |
| **参考ガイドライン** | 各社の公式サイト・開示資料・公的統計、[`launch/templates/company-analysis.md`](../../../launch/templates/company-analysis.md) |

法令・料率・制度の**具体的な数値は固定知識にしない**。使う都度、公式の一次情報で確認し、出典URLと確認日を記録する（[`launch/README.md` — 情報の鮮度ルール](../../../launch/README.md#情報の鮮度ルール)）。

---

## 4. Inputs

### 必須入力

| 入力 | 形式 | 説明 |
|---|---|---|
| 調査目的（答えるべき問い） | Markdown | 1〜3個に絞る |
| 対象企業リスト／選定基準 | Markdown | 直接競合・代替・ベンチマーク |
| 事業仮説（自社の想定） | Markdown | 比較の基準となる |

### 任意入力
- 市場調査の結果（`market-research`）
- 予算・期限
- 重点的に見たい観点（価格・SNS・採用 など）

### Context / 前工程成果物 / 設定値

| 種別 | 内容 |
|---|---|
| **Context** | Launch Track L0（事業モデル設計前）、L7（SNS設計前） |
| **前工程成果物** | `launch-brief.md` §1（事業仮説）、`market-research` の結果（あれば） |
| **設定値** | 対象社数（既定3社以上）、観点（既定5観点以上） |

**入力不足の場合**: 推測で補完せず、不足項目を明示して呼び出し元（Agent/人間）に差し戻す（[Section 9 Error Handling](#9-error-handling)）。

---

## 5. Execution Framework

標準の実行フロー（Analyze → Plan → Execute → Validate → Optimize → Finalize）は [`Skill_Base_Template.md — Section 5`](../../../00_System/Skill_Base_Template.md#5-execution-framework) に従う。このSkillでの具体化は次のとおり。

| ステージ | このSkillでの型 |
|---|---|
| **Analyze** | 答えるべき問いは何か。どの企業をどの観点で比べるか |
| **Plan** | 選定 → 情報源の特定 → 比較表の観点決定 → 深掘りの順。公式情報→開示資料→第三者情報の優先順位で収集する |
| **Execute** | 出典URLと確認日を付けて Fact を収集し、Insight を別欄に書く |
| **Validate** | 全ての Fact に出典があるか／推測を事実として書いていないか／3社・5観点を満たすか |
| **Optimize** | 示唆に効かない情報を削り、So What を3〜5点に絞る |
| **Finalize** | `company-analysis.md` と、Phase 01 引き渡し用の競合要約を確定する |

**運用ルール**: Validate で未達の場合は Plan に戻る（手法選定から見直す）。3回繰り返しても未達の場合は [Section 9](#9-error-handling) のエスカレーションに従う。

---

## 6. Outputs

### 成果物

| 出力形式 | 用途 | 出力先 |
|---|---|---|
| **Markdown** | 企業分析（比較表・個社の深掘り・ポジショニング・SWOT・So What・出典一覧） | `strategy/launch/company-analysis.md` |
| **Report** | 競合要約（Phase 01 への引き渡し） | `strategy/competitor-analysis.md` |

このSkillが実際に生成するのは: Markdown（企業分析）と Report（競合要約）

---

## 7. Quality Criteria

### 完成条件（Definition of Done）
- [ ] 対象が3社以上で、5観点以上で比較されている
- [ ] 全ての Fact に出典URLと確認日がある
- [ ] Fact と Insight が分離されている
- [ ] 各発見が自社への示唆（取り入れる／避ける／検証する）に変換されている
- [ ] Decision Log（判断根拠）が記録されている
- [ ] [Section 6 Outputs](#6-outputs)の形式に準拠している

### 品質基準
[`Quality_Standard.md`](../../../00_System/Quality_Standard.md) の共通5基準（明瞭さ・簡潔さ・一貫性・検証可能性・誠実さ）を適用する。このSkillでは特に **検証可能性（出典）と一貫性（同条件での比較）** を重視する。

### 判定基準

| 判定 | 条件 |
|---|---|
| ✅ **PASS** | 完成条件・品質基準を全て満たし証拠添付済み |
| ⚠️ **WARNING** | 必須は満たすが軽微な懸念あり（Open Issues登録・持ち越し2工程まで） |
| ❌ **FAIL** | 完成条件未達、または重大指摘あり（出典のない数値・専門家領域の断定・認証情報の混入 など） |

---

## 8. Human Judgment

このSkillの実行結果が以下に該当する場合、判断を確定させず選択肢＋推奨案として人間に提示する（[`Review_Process.md — Human Decision Framework`](../../../00_System/Review_Process.md#human-decision-framework) に加えて）:

- [ ] **ブランド**: 競合との差別化の方向性（ブランドの打ち出し方）
- [ ] **倫理**: 競合の非公開情報を不正に入手しない／誹謗・誤解を招く比較をしない
- [ ] **法務**: 他社の表現・商標・著作物の扱い（引用の範囲）は必要に応じて弁護士へ
- [ ] **最終意思決定**: どの競合を意識するか／価格・ポジショニングの決定
- [ ] 有料の調査データ・ツールの購入

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
| **Speed** | 実行の所要時間（タスク規模あたり） | 対象3社で1セッション以内 |
| **Cost** | 実行あたりのトークン・検索コスト | 調査は一次情報に絞り、同じ情報を重複取得しない |
| **Token Efficiency** | 不要なコンテキストを持ち込まない | 必要な知識・入力・テンプレートのみ参照する |
| **Scalability** | 業種・地域が変わっても品質が劣化しないか | 業種・地域固有の情報は Input で注入し、Skill本体は非依存に保つ |

---

## 11. Reusability

| 項目 | 内容 |
|---|---|
| **利用可能Agent** | 主利用: `business-launch`、`market-research` ／ 副利用: `ceo`、`growth` |
| **関連Skill** | `market-research`（市場全体）、`self-analysis`（自社）、`business-strategy` |
| **依存Skill** | なし（`market-research` の結果があれば入力として使う） |

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
