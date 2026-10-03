---
skill_name: sns-marketing-framework
display_name: SNS Marketing Framework Skill
category: growth
version: 1.0.0
status: Draft   # Draft / Active / Deprecated
owner: "@samkaz15"
created: 2026-10-03
updated: 2026-10-03
related_agents: [business-launch, growth]
related_phases: [1, 16, 18]
tags: [launch, sns, marketing, content, funnel]
---

# SNS Marketing Framework Skill

## 1. Skill Identity

| 項目 | 内容 |
|---|---|
| **Skill Name** | `sns-marketing-framework` |
| **Version** | `1.0.0` |
| **Category** | `growth`（[`Skill_Architecture.md`](../../../00_System/Skill_Architecture.md) の7カテゴリに対応。Launch Track は [`launch/README.md`](../../../launch/README.md)） |
| **Purpose** | 目的と数値目標から逆算し、ターゲット・チャネル・コンテンツ・ファネル・計測・運用ルールを設計し、投稿計画（カレンダー）と週次の改善ループに落とし込む能力。 |
| **Scope** | 立ち上げ期のSNSマーケティング設計（X・TikTok・Instagram・YouTube・ブログ・LINE等）。有料広告の運用は対象外 |
| **Related Domain** | デジタルマーケティング、行動経済学、コンテンツ設計 |

```yaml
identity:
  skill_name: "sns-marketing-framework"
  category: "growth"
  purpose: "Design target, channels, content, funnel, measurement and operating rules from goals, and turn them into a content calendar with a weekly improvement loop."
```

---

## 2. Capability

### このSkillでできること
- ターゲットとジョブ（JTBD）、提供価値、競合との違いを整理する
- チャネルを役割（認知・信頼・転換）と相性で選定する
- コンテンツピラー、フックの型、心理効果タグ、台本構成を設計する
- KGIからファネルKPIを逆算し、UTM規約を決める
- コンテンツカレンダーを作り、W1の数値で勝ち/負けパターンを判定する週次レビューを設計する
- 公開前のコンプライアンス（広告表示・誇大表現・権利・規約）をチェックする

### できないこと

| できないこと | 理由 / 代替 |
|---|---|
| 投稿・公開の最終承認 | 人間が承認する |
| ブランドの世界観・トーンの最終決定 | 人間が決定する |
| 再生数・成果の保証 | 仮説と検証で改善する。保証しない |
| 広告規制の最終判断（業法を含む） | 弁護士・所管官庁のガイドラインで確認する |
| 他者のコンテンツの丸写し | 型だけを学ぶ。著作権・権利を守る |
| 有料広告の運用・最適化 | `growth` Agent の施策として別途 |

### 前提条件
- [ ] ビジネスモデル（顧客・提供価値）がある
- [ ] KGI（月次売上・顧客数など）の仮置きがある
- [ ] 運用に使える時間（週あたり）が分かっている

### 適用条件
- Launch Track L7。方針・ターゲットが変わるとき、月次の見直し
- **適用しない状況**: 有料広告の出稿・最適化、プロダクト内のグロース施策（→ `growth` Agent）

### 制約事項
- 心理効果は誠実に使う（誇大・虚偽・不安の過度な煽り・ダークパターンは使わない）
- 実在の人物・顧客事例は同意と事実確認を取る
- 生成AIの出力は人間が確認してから公開する

---

## 3. Required Knowledge

| 種別 | 内容 |
|---|---|
| **理論** | AARRR とファネル分析、行動経済学（社会的証明・希少性・損失回避・権威性の使い方と倫理）、ストーリーテリング |
| **ベストプラクティス** | 借りた場（SNS）で認知を取り、自分の場（サイト・メール/LINE）に顧客リストを蓄積する／型を学び丸写しはしない／公開後1週間（W1）の数値で判定する／ファネルは逆算で設計する |
| **フレームワーク** | ファネル逆算（`kpi-kgi.csv`）、コンテンツピラー×フック型、台本構成（フック→共感→価値→行動）、UTM規約、`sns-content-calendar.csv` |
| **業界標準** | 景品表示法（ステマ規制を含む）、特定商取引法、個人情報保護法、著作権法、各SNSの規約・広告ポリシー |
| **参考ガイドライン** | 各SNSの公式アナリティクス・規約、消費者庁の景品表示法・ステマ規制の資料、[`launch/templates/sns-marketing-framework.md`](../../../launch/templates/sns-marketing-framework.md) |

法令・料率・制度の**具体的な数値は固定知識にしない**。使う都度、公式の一次情報で確認し、出典URLと確認日を記録する（[`launch/README.md` — 情報の鮮度ルール](../../../launch/README.md#情報の鮮度ルール)）。

---

## 4. Inputs

### 必須入力

| 入力 | 形式 | 説明 |
|---|---|---|
| ビジネスモデル（顧客・提供価値・価格） | Markdown | メッセージとチャネルの根拠 |
| KGI と転換率の仮置き | 数値 | ファネル逆算の入力 |
| 運用リソース（週あたり時間・担当） | Markdown | 投稿頻度の上限 |

### 任意入力
- 競合のSNS分析（`company-analysis`）
- 既存アカウント・実績データ
- ベンチマークとなる投稿・動画のリスト

### Context / 前工程成果物 / 設定値

| 種別 | 内容 |
|---|---|
| **Context** | Launch Track L7。開業後は週次・月次レビューで更新 |
| **前工程成果物** | `launch-brief.md` §1、`company-analysis.md`、`kpi-kgi.csv` |
| **設定値** | 対象チャネル、投稿頻度、対象期間、W1の評価指標 |

**入力不足の場合**: 推測で補完せず、不足項目を明示して呼び出し元（Agent/人間）に差し戻す（[Section 9 Error Handling](#9-error-handling)）。

---

## 5. Execution Framework

標準の実行フロー（Analyze → Plan → Execute → Validate → Optimize → Finalize）は [`Skill_Base_Template.md — Section 5`](../../../00_System/Skill_Base_Template.md#5-execution-framework) に従う。このSkillでの具体化は次のとおり。

| ステージ | このSkillでの型 |
|---|---|
| **Analyze** | 誰に何を届け、どの行動（問い合わせ・購入）を得たいか。使える時間はどれだけか |
| **Plan** | 目的/KGI → ターゲット → チャネル → コンテンツ → ファネル → 運用ルール → コンプライアンスの順で進める |
| **Execute** | フレームワークとカレンダーを作成し、`kpi-kgi.csv` でファネルを逆算する |
| **Validate** | KGIとの整合／運用時間で回せるか／公開前チェックを通るか／ダークパターンがないか |
| **Optimize** | チャネルとピラーを絞り、勝ち筋を再現できる型にする |
| **Finalize** | `sns-marketing-framework.md` と `sns-content-calendar.csv` を確定する |

**運用ルール**: Validate で未達の場合は Plan に戻る（手法選定から見直す）。3回繰り返しても未達の場合は [Section 9](#9-error-handling) のエスカレーションに従う。

---

## 6. Outputs

### 成果物

| 出力形式 | 用途 | 出力先 |
|---|---|---|
| **Markdown** | SNSマーケティング フレームワーク | `strategy/launch/sns-marketing-framework.md` |
| **CSV** | SNSコンテンツカレンダー | `strategy/launch/sheets/sns-content-calendar.csv` |
| **Report** | 週次レビュー（勝ち/負けパターンと次の打ち手） | 成果物内 |

このSkillが実際に生成するのは: Markdown（フレームワーク）、CSV（カレンダー）、Report（週次レビュー）

---

## 7. Quality Criteria

### 完成条件（Definition of Done）
- [ ] KGIからファネルKPIが逆算され、月次の必要投稿数が算出されている
- [ ] チャネルの役割と採否の理由がある
- [ ] ピラー・フック・台本構成・心理効果タグが定義されている
- [ ] 公開前コンプライアンスのチェックリストが運用されている
- [ ] 運用時間で回せる投稿頻度になっている
- [ ] Decision Log（判断根拠）が記録されている
- [ ] [Section 6 Outputs](#6-outputs)の形式に準拠している

### 品質基準
[`Quality_Standard.md`](../../../00_System/Quality_Standard.md) の共通5基準（明瞭さ・簡潔さ・一貫性・検証可能性・誠実さ）を適用する。このSkillでは特に **誠実さ（誇大・ダークパターンの排除）と一貫性（KGI・ファネル・カレンダーの整合）** を重視する。

### 判定基準

| 判定 | 条件 |
|---|---|
| ✅ **PASS** | 完成条件・品質基準を全て満たし証拠添付済み |
| ⚠️ **WARNING** | 必須は満たすが軽微な懸念あり（Open Issues登録・持ち越し2工程まで） |
| ❌ **FAIL** | 完成条件未達、または重大指摘あり（出典のない数値・専門家領域の断定・認証情報の混入 など） |

---

## 8. Human Judgment

このSkillの実行結果が以下に該当する場合、判断を確定させず選択肢＋推奨案として人間に提示する（[`Review_Process.md — Human Decision Framework`](../../../00_System/Review_Process.md#human-decision-framework) に加えて）:

- [ ] **ブランド**: 発信する人格・トーン・世界観の最終決定
- [ ] **倫理**: 心理効果の使い方（誇大・虚偽・不安の過度な煽り・解約妨害などを使わない）
- [ ] **法務**: 広告表示（景表法・ステマ規制）、業法の広告規制、権利（著作権・肖像権・商標）は必要に応じて弁護士へ
- [ ] **最終意思決定**: 公開の承認／予算・稼働の配分／チャネルの追加・撤退
- [ ] 炎上・クレーム対応の方針（人間が対応）

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
| **Speed** | 実行の所要時間（タスク規模あたり） | 1セッション以内（フレームワーク＋初月のカレンダー） |
| **Cost** | 実行あたりのトークン・検索コスト | 調査は一次情報に絞り、同じ情報を重複取得しない |
| **Token Efficiency** | 不要なコンテキストを持ち込まない | 必要な知識・入力・テンプレートのみ参照する |
| **Scalability** | 業種・地域が変わっても品質が劣化しないか | 業種・地域固有の情報は Input で注入し、Skill本体は非依存に保つ |

---

## 11. Reusability

| 項目 | 内容 |
|---|---|
| **利用可能Agent** | 主利用: `business-launch` ／ 副利用: `growth` |
| **関連Skill** | `marketing`、`cro`、`kpi-design`、`company-analysis`、`launch-planning` |
| **依存Skill** | `business-strategy`（顧客・提供価値）、`launch-planning`（KPI逆算の連携） |

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
