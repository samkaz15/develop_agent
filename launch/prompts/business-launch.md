# Business Launch Agent 起動プロンプト

> [`Agent_Base_Template.md — Prompt Writing Standard`](../../00_System/Agent_Base_Template.md) の構成（①Agent定義 ②タスク ③入力・制約 ④成果物・出力先 ⑤実行ルール）に従う。`{{ }}` を埋めて Claude Code に渡す。
> 1プロンプト1Agent。分からない項目は埋めずに「未確認」と書いてよい（Agentは推測で補完せず、不足を質問する）。

---

## 1. フル起動（ビジネスモデル〜開業準備まで）

```markdown
## Agent
`agents/strategy/business-launch.md` の Business Launch Agent として振る舞ってください。
必要なSkillは `skills/business/` と `skills/growth/sns-marketing-framework/` から読み込んでください。

## Task Request
- **From**: Human（{{OWNER}}）
- **To**: business-launch
- **Phase**: Launch Track L0〜L8（Phase 00-01 の前段・並走）
- **Task**: 下記のやりたいことを事業として成立させ、ビジネスモデルと「〇〇をやります」を提示し、必要な情報ツール・資本金・法人設立・労務・補助金・SNSマーケ・管理表（WBS／余日管理表）までを出力してください。
- **やりたいこと（自由記述）**: {{IDEA}}
- **本店所在地の想定**: {{PREFECTURE}} {{CITY}}
- **投下できる資金**: 自己資金 {{SELF_FUNDS}} 円 / 借入可能額 {{LOANABLE}} 円 / 生活防衛資金は別枠 {{LIVING_RESERVE}} 円
- **稼働時間・期間**: 週 {{HOURS}} 時間 / {{PERIOD}}
- **法人形態の希望**: {{FORM}}（未定可）
- **従業員・共同創業者の予定**: {{TEAM}}
- **プロジェクト開始日**: {{START_DATE}}

## Input Files
- `launch/templates/` の各テンプレート（コピーして `strategy/launch/` に出力）
- {{既存の調査・メモがあればパス}}

## Constraints
- 対象: 日本国内の株式会社・合同会社の設立（それ以外は対象外として報告）
- 法令・料率・補助金は公式の一次情報を調べ、出典URLと確認日を必ず記録する
- 認証情報（APIキー・パスワード等）・個人情報は成果物に書かない
- 予算（ツール月額上限）: {{TOOL_BUDGET}} 円

## Expected Output
- `strategy/launch/launch-brief.md`（主成果物）と、そこからリンクする各成果物
- `strategy/launch/sheets/` に WBS・余日管理表・資金繰り・KPI-KGI・給与・補助金・法務台帳・SNSカレンダー（CSV）
- Decision Log・Handoff Note・Open Issues

## Execution Rules
- Agent定義の Lifecycle・Quality Control・Escalation に従う
- Gate L1〜L4 は人間が判断する。AIは選択肢・推奨案・根拠を出すまで
- 士業の確認が必要な項目は「専門家確認待ち」と明記し、確定扱いにしない（[`professional-review-checklist.md`](../checklists/professional-review-checklist.md)）
- 情報不足・判断不能のときは作業を止め、質問または選択肢を提示する
- Confidence が Low の項目は人間レビューを要求する
```

---

## 2. 部分起動（必要なSkillだけ）

| 目的 | 追記する Task | 使うSkill | 主な出力 |
|---|---|---|---|
| 資本金の適正額だけ知りたい | 「資本金の推奨レンジを根拠付きで提案」 | `capital-planning` | `capital-plan.md` / `cashflow-plan.csv` |
| 設立手順と必要書類を知りたい | 「法人形態の比較と設立手順・届出一覧」 | `incorporation-legal` | `legal-setup-plan.md` / `legal-procedure-tracker.csv` |
| 補助金・助成金を地域別に調べたい | 「{{PREFECTURE}}/{{CITY}} の創業向け制度を一次情報で調査」 | `subsidy-research` | `subsidy-tracker.csv` |
| 給与を決めたい | 「役員報酬・従業員給与のシナリオ比較」 | `payroll-design` | `payroll-simulation.csv` |
| 労務の準備をしたい | 「雇用に必要な手続・書面・規程の整理」 | `labor-management` | `labor-setup-plan.md` |
| バックオフィスのツールを決めたい | 「必要ツールの比較と導入順」 | `back-office-design` | `tool-stack-proposal.md` |
| 競合を分析したい | 「競合3社以上の企業分析」 | `company-analysis` | `company-analysis.md` |
| 自分たちの強みを棚卸ししたい | 「創業者の自社分析」 | `self-analysis` | `self-analysis.md` |
| SNS戦略を作りたい | 「SNSマーケ戦略とコンテンツカレンダー」 | `sns-marketing-framework` | `sns-marketing-framework.md` / `sns-content-calendar.csv` |
| 管理表を作りたい | 「WBSと余日管理表（予実）を作成」 | `launch-planning` | `wbs-incorporation.xlsx` / `yojitsu-template.xlsx` |

---

## 3. 月次レビュー起動（開業後）

```markdown
## Agent
`agents/strategy/business-launch.md` の Business Launch Agent として、`launch-planning` Skill を使ってください。

## Task Request
- **Task**: `strategy/launch/sheets/yojitsu-template.xlsx` と `kpi-kgi.csv` の今月分実績を読み、予実差異の要因（事実と仮説を分けて）・KPIの勝ち/負けパターン・来月の施策案を提示してください。
- **Expected Output**: `strategy/launch/monthly-review-{{YYYY-MM}}.md`
- **Constraints**: 施策の実行決定・予算の変更は提案止まり（人間が決定）
```
