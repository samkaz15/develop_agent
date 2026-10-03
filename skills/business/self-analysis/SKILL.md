---
skill_name: self-analysis
display_name: Self Analysis Skill
category: business
version: 1.0.0
status: Draft   # Draft / Active / Deprecated
owner: "@samkaz15"
created: 2026-10-03
updated: 2026-10-03
related_agents: [business-launch, ceo]
related_phases: [0, 1]
tags: [launch, analysis, founder, swot, vrio]
---

# Self Analysis Skill

## 1. Skill Identity

| 項目 | 内容 |
|---|---|
| **Skill Name** | `self-analysis` |
| **Version** | `1.0.0` |
| **Category** | `business`（[`Skill_Architecture.md`](../../../00_System/Skill_Architecture.md) の7カテゴリに対応。Launch Track は [`launch/README.md`](../../../launch/README.md)） |
| **Purpose** | 創業者・初期組織の保有資源・強み・制約を証拠付きで棚卸しし、事業との適合度とギャップの補い方を提示する能力。 |
| **Scope** | 創業者・共同創業者・初期組織の内部分析（資源の棚卸し・VRIO・SWOT/クロスSWOT・事業適合度・ギャップ補完） |
| **Related Domain** | 経営戦略（資源ベース理論）、行動経済学（自己評価バイアス） |

```yaml
identity:
  skill_name: "self-analysis"
  category: "business"
  purpose: "Inventory founder/organization resources with evidence, assess fit with the business, and propose how to close gaps."
```

---

## 2. Capability

### このSkillでできること
- スキル・経験・人脈・資金・時間・発信力の棚卸しと、根拠（実績・数値・第三者の声）の確認
- VRIO による競争優位の有無の判定
- SWOT とクロスSWOT による戦略案の導出
- 事業適合度（Founder–Market Fit）のスコア化
- 足りない能力の補い方（外注・採用・士業・ツール・学習）とコストの提示
- 兼業規定・生活防衛資金・キーパーソン依存など、本人確認が必要な論点の抽出

### できないこと

| できないこと | 理由 / 代替 |
|---|---|
| 個人の能力・適性の断定的な評価 | 根拠（実績・第三者の声）が示す範囲に限定する。断定せず仮説として扱う |
| 兼業の可否など法的な判断 | 本人が勤務先の規程・契約を確認する。必要に応じて社労士・弁護士へ |
| 健康・心理状態の診断 | 医療・専門家の領域。論点の指摘に留める |
| 他社・競合の分析 | `company-analysis` Skill |

### 前提条件
- [ ] Intake（やりたいこと・資金・時間・本店所在地の想定）が完了している
- [ ] 創業者本人（または代理）が事実を提供できる

### 適用条件
- 事業の方向性を決める前（Launch Track L0）、共同創業者の追加時、事業の方針を変えるとき
- **適用しない状況**: 他社の分析（→ `company-analysis`）、市場全体の調査（→ `market-research`）

### 制約事項
- 自己申告は過信・過小評価に偏るため、根拠のない項目は評価に含めない
- 個人情報は最小限だけ扱い、成果物に住所・家族の詳細などを書かない

---

## 3. Required Knowledge

| 種別 | 内容 |
|---|---|
| **理論** | 資源ベース理論（RBV）、確証バイアス・過信バイアス（自己評価の偏り） |
| **ベストプラクティス** | 自己評価は根拠（実績・数値・第三者の声）とセットで記録する／強みは「顧客にとっての価値」まで言い換える／弱みは補い方まで書く |
| **フレームワーク** | VRIO、SWOT／クロスSWOT、Founder–Market Fit（5観点×5段階）、リソース棚卸し表 |
| **業界標準** | （該当する標準規格なし） |
| **参考ガイドライン** | [`launch/templates/self-analysis.md`](../../../launch/templates/self-analysis.md) |

法令・料率・制度の**具体的な数値は固定知識にしない**。使う都度、公式の一次情報で確認し、出典URLと確認日を記録する（[`launch/README.md` — 情報の鮮度ルール](../../../launch/README.md#情報の鮮度ルール)）。

---

## 4. Inputs

### 必須入力

| 入力 | 形式 | 説明 |
|---|---|---|
| Intake | Markdown | 目的・資金・時間・スキル・所在地の想定 |
| 創業者の経歴・実績・スキル | Markdown | 証拠（実績・成果物・第三者の声）とともに |
| 事業仮説（やりたいこと） | Markdown | 適合度を測る対象 |

### 任意入力
- 第三者の評価・推薦・顧客の声
- 財務状況（個人資産は概算で可）
- 共同創業者の同等情報

### Context / 前工程成果物 / 設定値

| 種別 | 内容 |
|---|---|
| **Context** | Launch Track L0。呼び出し元は `business-launch` Agent |
| **前工程成果物** | `launch-brief.md` §0（Intake） |
| **設定値** | 分析対象（創業者のみ／共同創業者を含む）、評価の厳しさ（保守的に） |

**入力不足の場合**: 推測で補完せず、不足項目を明示して呼び出し元（Agent/人間）に差し戻す（[Section 9 Error Handling](#9-error-handling)）。

---

## 5. Execution Framework

標準の実行フロー（Analyze → Plan → Execute → Validate → Optimize → Finalize）は [`Skill_Base_Template.md — Section 5`](../../../00_System/Skill_Base_Template.md#5-execution-framework) に従う。このSkillでの具体化は次のとおり。

| ステージ | このSkillでの型 |
|---|---|
| **Analyze** | 事業仮説に必要な資源は何か。入力のうち根拠付きの情報はどれか |
| **Plan** | 棚卸し → VRIO → SWOT → 適合度 → ギャップ補完の順で進める。根拠が不足する項目は質問に回す |
| **Execute** | 各項目に根拠を紐づけて記入し、VRIO・SWOT・適合度を判定する |
| **Validate** | 根拠のない評価が残っていないか／強みが顧客価値まで言い換えられているか |
| **Optimize** | 冗長な項目を削り、事業の成否に効く3〜5点に絞る |
| **Finalize** | `self-analysis.md` と、他Skill（資本・労務・ツール）への引き渡し事項を確定する |

**運用ルール**: Validate で未達の場合は Plan に戻る（手法選定から見直す）。3回繰り返しても未達の場合は [Section 9](#9-error-handling) のエスカレーションに従う。

---

## 6. Outputs

### 成果物

| 出力形式 | 用途 | 出力先 |
|---|---|---|
| **Markdown** | 自社分析（棚卸し・VRIO・SWOT・適合度・ギャップ補完・個人固有リスク） | `strategy/launch/self-analysis.md` |
| **Recommendation** | ギャップの補い方（外注・採用・士業・ツール）の選択肢と推奨 | 成果物内・Handoff Note |

このSkillが実際に生成するのは: Markdown（自社分析）と Recommendation（ギャップの補い方）

---

## 7. Quality Criteria

### 完成条件（Definition of Done）
- [ ] 資源の各項目に根拠（実績・数値・第三者の声）が付いている
- [ ] VRIO の判定（持続的/一時的/なし）が出ている
- [ ] 適合度スコアと、低い観点の補い方が示されている
- [ ] 本人確認が必要な個人固有リスクが「未確認」として列挙されている
- [ ] Decision Log（判断根拠）が記録されている
- [ ] [Section 6 Outputs](#6-outputs)の形式に準拠している

### 品質基準
[`Quality_Standard.md`](../../../00_System/Quality_Standard.md) の共通5基準（明瞭さ・簡潔さ・一貫性・検証可能性・誠実さ）を適用する。このSkillでは特に **検証可能性（根拠）と誠実さ（過信・過小評価の排除）** を重視する。

### 判定基準

| 判定 | 条件 |
|---|---|
| ✅ **PASS** | 完成条件・品質基準を全て満たし証拠添付済み |
| ⚠️ **WARNING** | 必須は満たすが軽微な懸念あり（Open Issues登録・持ち越し2工程まで） |
| ❌ **FAIL** | 完成条件未達、または重大指摘あり（出典のない数値・専門家領域の断定・認証情報の混入 など） |

---

## 8. Human Judgment

このSkillの実行結果が以下に該当する場合、判断を確定させず選択肢＋推奨案として人間に提示する（[`Review_Process.md — Human Decision Framework`](../../../00_System/Review_Process.md#human-decision-framework) に加えて）:

- [ ] **ブランド**: 創業者が打ち出す人格・世界観の方向づけ
- [ ] **倫理**: 本人の健康・家族・生活に関わる判断は本人のみが行う
- [ ] **法務**: 兼業・競業避止・前職との関係は、本人が規程・契約を確認し、必要なら専門家へ
- [ ] **最終意思決定**: 事業を続行・見直しするか／共同創業者の選定と役割分担
- [ ] 適合度スコアの解釈（リソース補強で進めるか、事業を見直すか）

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
| **Speed** | 実行の所要時間（タスク規模あたり） | 1セッション以内（Intake済みの場合） |
| **Cost** | 実行あたりのトークン・検索コスト | 調査は一次情報に絞り、同じ情報を重複取得しない |
| **Token Efficiency** | 不要なコンテキストを持ち込まない | 必要な知識・入力・テンプレートのみ参照する |
| **Scalability** | 業種・地域が変わっても品質が劣化しないか | 業種・地域固有の情報は Input で注入し、Skill本体は非依存に保つ |

---

## 11. Reusability

| 項目 | 内容 |
|---|---|
| **利用可能Agent** | 主利用: `business-launch` ／ 副利用: `ceo` |
| **関連Skill** | `company-analysis`（他社）、`business-strategy`（事業モデル）、`capital-planning`（資金の補完） |
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
