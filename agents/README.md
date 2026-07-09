# Agents — 定義ファイルレジストリ

> 全Agent定義ファイルの索引。定義の構造は [`00_System/Agent_Base_Template.md`](../00_System/Agent_Base_Template.md)、組織・RACIは [`00_System/Agent_Architecture.md`](../00_System/Agent_Architecture.md) を正本とする。
> 作成順・依存関係は [`01_Product/Requirement_Engineering_Framework.md`](../01_Product/Requirement_Engineering_Framework.md) の「Agent一覧（作成計画）」に従う。

| 優先 | Agent | 定義ファイル | Layer | Status |
|---|---|---|---|---|
| P0-1 | Product Manager | `executive/product-manager.md` | Executive | 🔲 Planned |
| P0-2 | CEO | `executive/ceo.md` | Executive | 🔲 Planned |
| P1-1 | Market Research | `strategy/market-research.md` | Strategy | 🔲 Planned |
| P1-2 | UX Research | `design/ux-research.md` | Design | 🔲 Planned |
| P2-1 | UX Designer | `design/ux-designer.md` | Design | 🔲 Planned |
| P2-2 | Backend Engineer | `engineering/backend.md` | Engineering | 🔲 Planned |
| P2-3 | AI Engineer | `engineering/ai-engineer.md` | Engineering | 🔲 Planned |
| P3-1 | UI Designer | `design/ui-designer.md` | Design | 🔲 Planned |
| P3-2 | Security | `quality/security.md` | Quality | 🔲 Planned |
| P3-3 | QA Engineer | `quality/qa-engineer.md` | Quality | 🔲 Planned |
| P3-4 | Growth | `strategy/growth.md` | Strategy | 🔲 Planned |
| P4-1 | Frontend Engineer | `engineering/frontend.md` | Engineering | 🔲 Planned |
| P4-2 | Performance | `quality/performance.md` | Quality | 🔲 Planned |

**Status凡例**: 🔲 Planned / 🟡 Draft / ✅ Active / ⛔ Deprecated

### 追加ルール

1. 新Agentは [`Agent_Base_Template.md`](../00_System/Agent_Base_Template.md) をコピーして作成し、同テンプレートの「新規Agent作成チェックリスト」を全て満たしてからマージする
2. 本レジストリ・[`Agent_Architecture.md`](../00_System/Agent_Architecture.md) の一覧/RACI/Workflow統合表を同時に更新する
3. P0の2体（PM・CEO）完成時点で要件定義（Gate Aまで）の実運用を開始できる
