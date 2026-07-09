# develop_agent — AI Development Operating System

AIエージェントを中核に据えた、プロダクト開発のためのオペレーティングシステム（開発OS）。
企画からグロースまでの全工程を、明文化されたプロセス・仮想エージェント組織・再利用可能なパッケージ群によって推進する。
AIサービス・Webサービス・SaaS・モバイルアプリ・AIエージェントなど、今後制作するすべてのプロダクトの共通基盤。

| 項目 | 内容 |
|---|---|
| **Version** | 1.0.0 |
| **Status** | Active（設計層完成・実行層構築中） |
| **Last Updated** | 2026-07-10 |

---

## 目的

- **開発プロセス全体の体系化**: 企画・UX・UI・AI・実装・テスト・リリース・グロースの全ライフサイクルを1つのOSとして管理する
- **AIエージェントによる開発の加速**: 各工程に特化したAIエージェントが実行を担い、人間は意思決定に集中する
- **知識の資産化**: プロセス・基準・テンプレート・プロンプトを再利用可能な形で蓄積し、プロジェクトを重ねるごとにOS自体が進化する

## 思想

1. **プロセスをコードのように管理する** — 判断基準・成果物フォーマットをすべて明文化しバージョン管理する。暗黙知を残さない
2. **人間は意思決定、AIは実行** — ブランド・事業・倫理・法務・最終承認は人間、実行・分析・生成はAI。境界は全ドキュメントで明文化
3. **判定可能でなければ基準ではない** — 「高品質」ではなく数値と判定文で書く
4. **Build Once, Use Everywhere** — Platform・Design・AI・Engineeringの各Packageは一度作りすべてのサービスで再利用する
5. **失敗を基準に還元する** — 障害・差し戻し・レビュー指摘は必ず該当基準・チェックリストの改訂に還元する

## リポジトリ構成

```
develop_agent/
│
│  ── OS基盤（00_System/: プロセス・組織・能力・品質の正本） ──
├── 00_System/
│   ├── Repository_Standard.md     # リポジトリ構造・配置規約の正本
│   ├── Development_Workflow.md    # 標準開発フロー（Phase 00-19 + 改善ループ）
│   ├── Agent_Architecture.md      # 仮想開発組織（5 Layer / 13 Agent / RACI）
│   ├── Agent_Base_Template.md     # 全Agent共通の定義テンプレート（13セクション）
│   ├── Skill_Architecture.md      # スキル能力体系（7カテゴリ / 17 Skill）
│   ├── Skill_Base_Template.md     # 全Skill共通の定義テンプレート（12セクション）
│   ├── Quality_Standard.md        # 品質基準の単一情報源（10領域・数値基準・Score）
│   ├── Review_Process.md          # レビュー実行機構（7ステージ・Gate・Severity）
│   └── Project_Template.md        # 実案件への適用テンプレート（初期化・Dashboard）
│
│  ── 要件定義（01_Product/） ──
├── 01_Product/
│   └── Requirement_Engineering_Framework.md  # 要件定義20ステージ・4ゲート
│
│  ── 共有資産Package（無番号: 全サービス横断で再利用） ──
├── platform/       # Platform Package（認証・決済・通知・監視など12 Domain）
├── design/         # Design Package（UX/UI原則・Figma System・UX Writing・A11y）
├── ai/             # AI Package（Prompt・RAG・評価駆動・AI Safety の5 Layer）
├── engineering/    # Engineering Package（13 Domain実行標準・Git規約・12 Review）
│
│  ── 実行資産（構築中） ──
├── agents/         # Agent定義ファイル（Agent_Base_Template準拠・13体を順次作成）
├── skills/         # Skillライブラリ（Skill_Base_Template準拠・レジストリ管理）
├── templates/      # 成果物テンプレート（Requirement_Template ほか）
├── prompts/        # 再利用可能プロンプト
├── examples/       # 成果物サンプル・過去事例
├── docs/           # 補足ドキュメント
│
│  ── Workflow成果物置き場（プロジェクト実行時に使用） ──
├── 02_UX/  03_UI/  04_AI/  05_Development/  06_Test/  07_Launch/  08_Growth/
```

配置ルールの詳細は [`00_System/Repository_Standard.md`](./00_System/Repository_Standard.md) を参照。

## 使い方（Quick Start）

1. **OSを理解する**: `00_System/Development_Workflow.md`（プロセス）→ `Agent_Architecture.md`（組織）→ `Quality_Standard.md`（基準）の順に読む
2. **新規プロジェクトを始める**: `00_System/Project_Template.md` の Initialization Flow に従って初期化する
3. **要件定義を行う**: `templates/Requirement_Template.md` をコピーし、`01_Product/Requirement_Engineering_Framework.md` の20ステージを進める（Gate A〜Dは人間が判定）
4. **開発する**: Development_Workflow の Phase 03以降を、各Package（platform / design / ai / engineering）の標準に従って実行する
5. **学びを還元する**: 実案件で得た知見は各Packageの `examples/`・チェックリスト・基準に還元する

## 運用ルール

- ファイル名は英語（成果物はケバブケース）。1ファイル1トピック
- すべての正本ドキュメントはVersion・変更履歴を持ち、変更はPull Request＋Owner承認で行う
- 重要な意思決定はDecision Logとして記録し、コミットメッセージに理由を残す
- 各ドキュメントの役割分担（何がどこの正本か）は `00_System/Repository_Standard.md` に従う

## ロードマップ（実行層の構築順）

- [ ] **P0**: `agents/executive/product-manager.md`・`ceo.md`（この2体で要件定義Gate Aまで運用可能）
- [ ] **P1**: Market Research / UX Research Agent、最初の実案件で要件定義を開始
- [ ] **P2以降**: 残りAgent・Skill実体・ドキュメントテンプレート群を実案件と並走で整備
- [ ] Platform P0 Domain（Deployment / Security / Monitoring）の詳細設計

詳細な依存関係と優先順位は [`01_Product/Requirement_Engineering_Framework.md`](./01_Product/Requirement_Engineering_Framework.md) の「Agent一覧（作成計画）」を参照。
