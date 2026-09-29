# HP Template Library

| 項目 | 内容 |
|---|---|
| Version | 1.0.0 |
| Status | Active — 蓄積・制作テンプレート |
| Last Updated | 2026-09-29 |

参考HPと再利用テンプレートを蓄積する場所。依頼の「hp templete fail」はこの `hp_template/` として用意した。
参考サイトのURLはまだ受領していないため、実在サイトの推薦や架空の分析結果は登録していない。

## 保存先

| 保存先 | 用途 |
|---|---|
| [references/reference-entry.md](references/reference-entry.md) | 参考HPを観察・比較する書式 |
| [templates/site-brief.md](templates/site-brief.md) | HPの目的・顧客・要件・計測 |
| [templates/service-site/](templates/service-site/README.md) | 編集できるHTML/CSSのサービスHP |
| [templates/landing-page.md](templates/landing-page.md) | 単一商品LPの構成 |
| [templates/content-site.md](templates/content-site.md) | 記事・SEO中心のサイト構成 |
| [checklists/release.md](checklists/release.md) | 制作と公開前のチェック |
| [prompts/build-website.md](prompts/build-website.md) | AIへのHP制作指示 |
| [examples/reference-example.md](examples/reference-example.md) | 架空例による登録の見本 |

## 参考HP → 制作 → 改善

1. 参考URL、参考にしたい箇所、目的を受け取る。実際に見られた範囲だけ観察する。
2. 事業台帳に `reference` レコードを登録する。URLと観察日は必須、好みと計測結果は分ける。
3. 詳細分析を案件側に作り、採用/不採用とその理由を残す。他社素材・文章の複製はしない。
4. `website_template` のID・バージョンを選び、site-briefと既存の要件定義書を埋める。
5. 案件用ディレクトリにコピーし、コピー/色/画像/CTAを独自制作する。WordPressなら案件側のテーマ・ページ・ブロックに実装する。
6. QA、計測確認、Ownerの公開承認を行う。
7. `creative` → `experiment` → `knowledge` を記録する。複数案件で再利用できる学びを新しいテンプレート版へ反映する。

参考HPの構造化索引は各事業のregistry.jsonに置く。ここに同じURL一覧の別正本は作らない。
全社横断の検索時は各registryのtype=reference/website_templateを集め、出典workspaceとIDを表示する。

## 関連ドキュメント

| 正本 | 役割 |
|---|---|
| [Design Package](../design/README.md) | デザイン基準 |
| [Requirement Template](../templates/Requirement_Template.md) | 詳細要件 |
| [Quality Standard](../00_System/Quality_Standard.md) | 品質判定 |
| [Startup Package](../startup/README.md) | 構造化台帳・実験記録 |
| [Creative Workflow](../design/creative/README.md) | 制作と改善 |

## Version Management

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-09-29 | 参考登録、3用途の雛形、HTML/CSSスターター、QAを追加 |
