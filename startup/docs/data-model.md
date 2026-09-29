# データモデルと運用定義

Version 1.0.0 / 2026-09-29

`schemas/model.json` はこのCLI専用の入力契約。一般のJSON Schemaバリデータ向けではない。
トップレベル: schema_version=1、workspace、records配列、audit配列。
共通項目: id/type/title/status/evidence/source/updated_on。IDは事業台帳内で一意な英小文字ケバブケース。

| Type | 管理対象 | 主な接続 |
|---|---|---|
| company / strategy | Mission、顧客価値、収益モデル、目標、戦略仮説 | company_ids |
| customer | 匿名セグメント、JTBD、Pain/Gain | company_ids |
| project | スコープ、期限、予定完了、予測完了 | company_ids / kpi_ids |
| task | WBS、担当、期限、工数、DoD、成果物 | project_ids / kpi_ids / depends_on |
| team | 役割・稼働時間 | タスクownerで参照する担当名 |
| kpi | 定義・単位・目標・実績・計測日・改善方向 | company_ids |
| marketing | チャネル、Offer、CTA、予算 | project_ids / kpi_ids |
| creative | コピー・CTA・版・素材パス | project_ids / kpi_ids / reference_ids / template_ids |
| experiment | 仮説・変数・対照・処置・標本計画・結果・判断 | project_ids / kpi_ids / creative_ids |
| knowledge | 学び・適用条件・次の作業 | experiment_ids / evidence_ids |
| reference | 参考URL、観察日、構成、採用理由、権利 | テンプレート・クリエイティブから参照 |
| website_template | テンプレートパス・版・用途・受入条件 | reference_ids |
| finance | 月次の通貨・指標辞書・計算前提 | company_ids |
| valuation | 価値ドライバーと根拠・限界 | company_ids / evidence_ids |
| risk / decision | リスク・緩和策、意思決定・理由・再確認日 | project_ids |

全typeの完全な入力雛形は `../templates/records/` にある。追加項目を許可するため、詳細な分析内容は自由記述で拡張できる。
requiredは項目の存在を要求し、draft段階ではnullを許可する。CLIは全ての業務内容の正しさや文章の充足を判定しない。着手・完了条件とチェックリストを併用する。

## WBSと作業要件

Taskに必要に応じて `workstream`, `purpose`, `requirement_ids`, `input`, `process`, `output`, `parent_task_id`, `risk`, `notes` を追加する。
階層は Business(company) → Project → Workstream → Deliverable → Task → Subtask。`parent_task_id` は文書上の階層用（CLIの参照検証対象外）、`depends_on` は依存関係検証用。
`draft` は未確認項目がある状態。`ready/in_progress/done` はowner/reviewer/due_date/DoD/project_ids/kpi_ids必須。
`done` はprogress=100とdeliverableも必須。成果物品質の人間レビューは別途必要。
P0〜P3は優先度案。根拠を `priority_reason` に記録し、Ownerが上書きできる。CLIは優先度を自動変更しない。

## KPI

割合は0〜1など単位を統一し、定義に分母・対象期間・除外条件を記載する。CVRの異なる分母を混ぜない。
実績値があるときは `measured_on` 必須。`target/actual=null` は未取得であり0として扱わない。
`review` は単一の目標差を検知するだけで、時系列トレンド・異常検知の統計モデルではない。

## 余日管理

暦日で計算（休日・工数・担当稼働の自動考慮なし）。
計画余日 = deadline − required_finish。残余日 = deadline − forecast。
消費日 = max(0, forecast − required_finish)。消費率 = 消費日 ÷ 計画余日。
残余日<0ならCRITICAL、残余日=0または消費率>=100%ならRED、50%以上ならYELLOW、他はGREEN。
計画余日ゼロでは締切到達をRED、超過をCRITICAL。必要日付がnullならUNKNOWN。
forecastは人間/PMが更新する予測。クリティカルパスは作業依存・所要時間を元に別途分析する。

## 財務と企業価値

finance.metricsに数値を保存する場合、期間・通貨・収益認識・税込税抜・データソースを明記する。
この版は財務数値の集計・EBITDA/FCF計算・企業価値評価を自動実行しない。
valuationは収益成長・利益率・継続率・顧客獲得効率・ブランド・IP・データ・経営者依存などの根拠を蓄積する。
実験でCVRが上がっただけで売上や企業価値を確定額として増やさない。実現した取引と財務原票の確認後に反映する。

## 監査・権限

upsertは全体の検証に成功した場合だけ保存し、actor/reason/対象ID/時刻/変更前後ハッシュを追記する。
Gitで本文の履歴を保つ。監査ログは改ざん防止の署名台帳ではなく、手編集は検知しきれない。
外部公開・予算変更・契約・削除・Go/No-GoはOwnerの承認をDecisionに記録し、実行環境側でも制御する。このCLIは外部操作を持たない。
