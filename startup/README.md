# Startup Package

| 項目 | 内容 |
|---|---|
| Version | 1.0.0 |
| Status | Active — 手動運用とローカルCLI |
| Last Updated | 2026-09-29 |

事業構想を、要件・制作・施策・計測・学びへ接続するデータ蓄積基盤。
最初に [入力済みの初期台帳](data/initial-business/registry.json) と [事業ブリーフ](templates/business-brief.md) を使う。
初期台帳は今回の依頼に基づく構想であり、会社情報・価格・実績・担当・期限は未確認。勝手に売上やCVRを補完しない。

## 最初の使い方

リポジトリルートで Python 3.10 以降を使用する。追加ライブラリ・APIキーは不要。

```bash
python startup/tools/workspace.py validate startup/data/initial-business/registry.json
python startup/tools/workspace.py review startup/data/initial-business/registry.json --today 2026-09-29
```

1. [事業ブリーフ](templates/business-brief.md) で顧客・課題・価格・目的を記入する。
2. `templates/records/` のJSONをコピーし、`{{...}}` を置換する。初期台帳の既存IDを指定すると全項目を置換するので、更新時は現在のレコード全体をコピーする。
3. 複数の関連レコードは一つのJSON配列で入力する。`null` は未確認、0は実際のゼロ。根拠・確認日・evidenceを記録する。
4. 下記 `upsert` で保存する。参照・日付・数値・重複・依存循環・着手条件を検証し、理由と変更ハッシュを監査履歴へ追記する。
5. HP制作は [hp_template](../hp_template/README.md)、改善は [creative](../design/creative/README.md) へ進む。

```bash
# input.json は手順2で作ったレコード配列
python startup/tools/workspace.py upsert startup/data/initial-business/registry.json input.json --actor owner --reason '顧客と提供価値を確認'
# 新しい事業は空台帳から開始する。既存ファイルを上書きしない。
python startup/tools/workspace.py init startup/data/new-business/registry.json --name new-business --actor owner
python -m unittest discover -s startup/tests -v
```

`upsert` は削除を行わず、同じ入力の再送では履歴を増やさない。検証失敗時は保存しない。
同一ファイルの並行CLI更新はロックで拒否する。手編集との同時実行は避ける。クラッシュ後の `.lock` は実行プロセスがないことを確認してから除去する。
GitのPRで差分・理由・履歴を残し、mainへのマージはOwnerが承認する。

## 正本と蓄積ルール

- 事業ごとの `data/<business>/registry.json` が構造化データの正本。案件文書はIDを参照する。
- `templates/` は空の雛形、`examples/` は架空例。実績に集計しない。
- `hp_template/templates/` は共通部品。案件固有の修正は案件側にコピーし、検証できた知見だけ共通テンプレートへ戻す。
- `source` に出典、`updated_on` に確認日。外部調査はURL・閲覧日・対象市場・推定方法を併記する。
- `evidence`: `fact` 確認済み / `hypothesis` 仮説 / `unknown` 未確認 / `sample` 架空例。
- このリポジトリは公開。実顧客の氏名・連絡先・非公開財務はアクセス制限された別の保管場所で管理し、ここには匿名化した集計または資料IDのみ保存する。

## 実装済みと今後

実装済み: 台帳初期化・更新・検証・監査履歴、期限超過/KPI目標差/実験終了/未設定の警告、暦日ベースの余日確認。
`review` は実行時の読取り診断。予測日は入力値であり、自動工数予測・クリティカルパス計算・統計的有意差判定はしない。
未実装: 常駐Agent、外部サービス連携、計測値自動取得、投稿・広告配信、金融計算エンジン、Web管理画面。
詳細は [導入計画](../docs/startup-foundation-plan.md)。添付の全体要件は将来構想として [原本](../docs/entrepreneur-agent-request.md) に保持する。

## 関連ドキュメント

| 正本 | 役割 |
|---|---|
| [Repository Standard](../00_System/Repository_Standard.md) | 配置・命名・変更手順 |
| [Agent Architecture](../00_System/Agent_Architecture.md) | 組織と責任 |
| [責務対応表](docs/responsibility-map.md) | 25責務を既存Agentへ接続 |
| [データ契約](schemas/model.json) / [定義](docs/data-model.md) | 入力項目・関係・計算範囲 |
| [要件テンプレート](../templates/Requirement_Template.md) | 要件定義の正本 |
| [Quality Standard](../00_System/Quality_Standard.md) | 品質の判定基準 |

## Version Management

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-09-29 | 初期台帳・テンプレート・検証CLI・制作接続を追加 |
