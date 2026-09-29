# Entrepreneur責務と既存Agentの対応

Version 1.0.0 / 2026-09-29

組織の正本は [Agent Architecture](../../00_System/Agent_Architecture.md)。25個の独立実行Agentを新設せず、添付の責務を既存13役割へ接続する。以下は運用上の担当マップであり、APIによる自律Agent実装ではない。

| # | 添付の責務 | 既存の主担当 | 成果物/境界 |
|---|---|---|---|
| 1 | Strategy | CEO | 戦略・撤退条件 |
| 2 | Market Research | Market Research | 市場・競合・根拠 |
| 3 | Customer | UX Research | ICP・JTBD・VOC |
| 4 | Value Proposition | Product Manager | 顧客価値・受入条件 |
| 5 | Business Model | CEO | 収益構造・価格仮説 |
| 6 | Product | Product Manager | MVP・ロードマップ |
| 7 | Requirement Definition | Product Manager | 既存要件定義テンプレート |
| 8 | Work Requirement | Product Manager | Taskの入力・出力・DoD |
| 9 | PMO | Product Manager | 進捗・依存・余日 |
| 10 | WBS | Product Manager | タスク分解 |
| 11 | Marketing Strategy | Growth | チャネル・Offer・Funnel |
| 12 | Marketing Execution | Growth | 制作/投稿/計測の作業化 |
| 13 | Growth | Growth | KPI・改善 |
| 14 | Sales | CEO | 営業プロセス・成約仮説 |
| 15 | CRM / Retention | Growth | 継続・顧客価値 |
| 16 | Finance | CEO | 財務記録の整理・専門家への確認事項 |
| 17 | KPI | Growth | 定義・実績・目標差 |
| 18 | Team Management | Product Manager | 担当・稼働・成果物 |
| 19 | Risk | CEO | リスク・緩和策。Securityへ技術レビュー依頼 |
| 20 | Experiment | Growth | 仮説・比較・結果・判断 |
| 21 | Operations | Product Manager | 運営手順・引き継ぎ |
| 22 | Management Review | CEO | 意思決定・優先順位 |
| 23 | Competitive Intelligence | Market Research | 競合変化と根拠 |
| 24 | Corporate Value | CEO | 価値ドライバーの証拠 |
| 25 | M&A Readiness | CEO | 不足資料と改善作業。評価・契約判断は人間/専門家 |

HP: UX Research→UX Designer→UI Designer→Frontend/Backend→QA/Security/Performanceへ受け渡す。
制作物の自己承認は行わず、作成者とReviewerを分ける。予算・外部公開・契約・Go/No-GoはOwnerが判断する。
共通Inputは対象の台帳IDと最新版、OutputはID付き成果物・理由・不足項目・次Task。
最大3回の修正で解消しないBlockedや担当間の責務衝突はPM→Ownerへ戻す。自動の無限差し戻しループを設けない。
