---
skill_name: back-office-design
display_name: Back-office Design Skill
category: business
version: 1.0.0
status: Draft   # Draft / Active / Deprecated
owner: "@samkaz15"
created: 2026-10-03
updated: 2026-10-03
related_agents: [business-launch, ceo, security]
related_phases: [0, 16]
tags: [launch, back-office, tools, automation, accounting]
---

# Back-office Design Skill

## 1. Skill Identity

| 項目 | 内容 |
|---|---|
| **Skill Name** | `back-office-design` |
| **Version** | `1.0.0` |
| **Category** | `business`（[`Skill_Architecture.md`](../../../00_System/Skill_Architecture.md) の7カテゴリに対応。Launch Track は [`launch/README.md`](../../../launch/README.md)） |
| **Purpose** | 経理・請求・経費精算・労務・契約・書類管理のバックオフィス運用を設計し、必要情報ツールを比較・選定し、AIで自動化する範囲と人間の承認点を決める能力。 |
| **Scope** | 立ち上げ期のバックオフィス（会計・請求・経費・支払・労務・勤怠・契約・書類）の運用設計とツール選定、AI業務自動化の範囲、権限・秘密管理 |
| **Related Domain** | バックオフィス業務設計、内部統制の基礎、SaaS選定 |

```yaml
identity:
  skill_name: "back-office-design"
  category: "business"
  purpose: "Design back-office operations and select information tools, defining which tasks are automated by AI and where human approval is required."
```

---

## 2. Capability

### このSkillでできること
- 業務を洗い出し、運用フロー（誰が・いつ・何を・どのツールで）を設計する
- ツールを最低2候補で比較する（公式の料金・機能・確認日、士業との連携可否、データのエクスポート可否）
- 必須・推奨・後回しに仕分け、導入ロードマップと月額累計を示す
- 業務をAI／協働／人間に仕分け、人間の承認点を明記する（自動化一覧）
- 権限・認証情報・2段階認証・退職時の無効化の方針を設計する

### できないこと

| できないこと | 理由 / 代替 |
|---|---|
| ツールの契約・課金の実行 | 人間が実行する |
| ツールの機能・料金の保証 | 公式の最新情報で確認し、確認日を記録する |
| 会計処理・税務の最終判断 | 税理士に確認する |
| セキュリティ監査 | `security` Agent |

### 前提条件
- [ ] ビジネスモデル（取引形態・決済方法）が分かっている
- [ ] ツール予算の上限、または確認の予定がある

### 適用条件
- Launch Track L5（バックオフィス構築）。事業・人数・取引形態が変わるとき
- **適用しない状況**: プロダクトの技術選定（→ Backend Engineer Agent）

### 制約事項
- 必要になる直前に導入する（先回りで契約しない）
- 認証情報は専用の管理手段に保管し、シート・リポジトリに書かない
- 価格・機能は公式の最新情報と確認日を添える

---

## 3. Required Knowledge

| 種別 | 内容 |
|---|---|
| **理論** | 内部統制の基本（職務分掌・承認・証跡）、業務自動化の設計 |
| **ベストプラクティス** | 必要になる直前に導入／エクスポート可否と連携を確認／税理士・社労士が使えるツールを選ぶ／認証情報は専用管理＋2段階認証／最小権限 |
| **フレームワーク** | ツール選定表（目的・候補・基準・月額・必要度・導入時期）、AI業務自動化一覧（自動化レベル×人間の承認点）、権限設計表 |
| **業界標準** | 電子帳簿保存法、インボイス制度、個人情報保護法（要件は一次情報で確認） |
| **参考ガイドライン** | 各ツールの公式料金・機能ページ（会計・請求・経費精算・労務・契約・書類管理・LayerX「バクラク」シリーズを含む）、国税庁の電子帳簿保存法・インボイス関連、[`launch/templates/tool-stack-proposal.md`](../../../launch/templates/tool-stack-proposal.md) |

法令・料率・制度の**具体的な数値は固定知識にしない**。使う都度、公式の一次情報で確認し、出典URLと確認日を記録する（[`launch/README.md` — 情報の鮮度ルール](../../../launch/README.md#情報の鮮度ルール)）。

---

## 4. Inputs

### 必須入力

| 入力 | 形式 | 説明 |
|---|---|---|
| ビジネスモデル（取引形態・決済方法・顧客層） | Markdown | 必要な業務とツールを決める |
| 従業員・外注の予定 | Markdown | 労務・権限の設計に影響 |
| 月額ツール予算の上限 | 数値 | 未定なら提案時に範囲を示す |

### 任意入力
- 士業の選定結果（使うツールの指定があるか）
- 既に使っているツール
- セキュリティ要件

### Context / 前工程成果物 / 設定値

| 種別 | 内容 |
|---|---|
| **Context** | Launch Track L5。Gate L2 後に導入判断 |
| **前工程成果物** | `launch-brief.md` §1、`labor-setup-plan.md`、`capital-plan.md` |
| **設定値** | 予算上限、導入時期、価格の確認日 |

**入力不足の場合**: 推測で補完せず、不足項目を明示して呼び出し元（Agent/人間）に差し戻す（[Section 9 Error Handling](#9-error-handling)）。

---

## 5. Execution Framework

標準の実行フロー（Analyze → Plan → Execute → Validate → Optimize → Finalize）は [`Skill_Base_Template.md — Section 5`](../../../00_System/Skill_Base_Template.md#5-execution-framework) に従う。このSkillでの具体化は次のとおり。

| ステージ | このSkillでの型 |
|---|---|
| **Analyze** | 立ち上げ期に必要な業務は何か。人間が担うべき承認点はどこか |
| **Plan** | 業務洗い出し → 運用フロー → ツール比較 → 自動化仕分け → 権限設計 → ロードマップの順で進める |
| **Execute** | 公式情報で料金・機能を確認し、確認日付きで選定表を作成する |
| **Validate** | 最低2候補で比較したか／予算内か／士業が使えるか／認証情報の扱いが安全か |
| **Optimize** | 今必要なものに絞り、残りは導入時期付きで後回しにする |
| **Finalize** | `tool-stack-proposal.md`（自動化一覧を含む）を確定する |

**運用ルール**: Validate で未達の場合は Plan に戻る（手法選定から見直す）。3回繰り返しても未達の場合は [Section 9](#9-error-handling) のエスカレーションに従う。

---

## 6. Outputs

### 成果物

| 出力形式 | 用途 | 出力先 |
|---|---|---|
| **Markdown** | 必要情報ツール提案書（選定表・AI業務自動化一覧・セキュリティ設計・導入ロードマップ） | `strategy/launch/tool-stack-proposal.md` |
| **Recommendation** | ツールの採否と導入順の選択肢と推奨 | 成果物内 |

このSkillが実際に生成するのは: Markdown（ツール提案書）と Recommendation

---

## 7. Quality Criteria

### 完成条件（Definition of Done）
- [ ] 各カテゴリで最低2候補が比較され、価格・機能に出典URLと確認日がある
- [ ] 必要度（必須/推奨/後回し）と導入時期が決まっている
- [ ] 業務が自動化レベル（AI/協働/人間）に仕分けられ、人間の承認点が明記されている
- [ ] 認証情報・権限・2段階認証の方針がある
- [ ] Decision Log（判断根拠）が記録されている
- [ ] [Section 6 Outputs](#6-outputs)の形式に準拠している

### 品質基準
[`Quality_Standard.md`](../../../00_System/Quality_Standard.md) の共通5基準（明瞭さ・簡潔さ・一貫性・検証可能性・誠実さ）を適用する。このSkillでは特に **検証可能性（価格・機能の出典と確認日）と一貫性（運用フローとツールの整合）** を重視する。

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
- [ ] **倫理**: 従業員の監視にあたるツールは目的・範囲を明示して導入する
- [ ] **法務**: データの保存場所・委託先・個人情報の取扱い・電子保存要件は専門家へ
- [ ] **最終意思決定**: ツールの契約・課金／導入するか見送るか
- [ ] 自動化してよい業務の範囲（支払・契約締結・納税は人間が実行）

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
| **Speed** | 実行の所要時間（タスク規模あたり） | 1セッション以内（15カテゴリの比較） |
| **Cost** | 実行あたりのトークン・検索コスト | 調査は一次情報に絞り、同じ情報を重複取得しない |
| **Token Efficiency** | 不要なコンテキストを持ち込まない | 必要な知識・入力・テンプレートのみ参照する |
| **Scalability** | 業種・地域が変わっても品質が劣化しないか | 業種・地域固有の情報は Input で注入し、Skill本体は非依存に保つ |

---

## 11. Reusability

| 項目 | 内容 |
|---|---|
| **利用可能Agent** | 主利用: `business-launch` ／ 副利用: `ceo`、`security` |
| **関連Skill** | `labor-management`、`incorporation-legal`、`capital-planning` |
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
