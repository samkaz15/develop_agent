# Skills — Skillライブラリレジストリ

> 全Skillの索引。体系・カテゴリは [`00_System/Skill_Architecture.md`](../00_System/Skill_Architecture.md)、個別Skillの定義構造は [`00_System/Skill_Base_Template.md`](../00_System/Skill_Base_Template.md) を正本とする。
> 新Skillは Skill_Base_Template 内の「Skill定義テンプレート」をコピーし、`skills/{category}/{skill-name}/SKILL.md` として作成する。

## コアSkill（Skill_Architecture 定義の17 Skill）

| Skill | パス | カテゴリ | Status |
|---|---|---|---|
| Market Research | `business/market-research/` | business | 🔲 Planned |
| Business Strategy | `business/business-strategy/` | business | 🔲 Planned |
| Product Management | `product/product-management/` | product | 🔲 Planned |
| KPI Design | `product/kpi-design/` | product | 🔲 Planned |
| UX Research | `ux/ux-research/` | ux | 🔲 Planned |
| UX Design | `ux/ux-design/` | ux | 🔲 Planned |
| UI Design | `ui/ui-design/` | ui | 🔲 Planned |
| Apple HIG | `ui/apple-hig/` | ui | 🔲 Planned |
| Material Design | `ui/material-design/` | ui | 🔲 Planned |
| Frontend | `engineering/frontend/` | engineering | 🔲 Planned |
| Backend | `engineering/backend/` | engineering | 🔲 Planned |
| AI Engineering | `engineering/ai/` | engineering | 🔲 Planned |
| QA | `quality/qa/` | quality | 🔲 Planned |
| Security | `quality/security/` | quality | 🔲 Planned |
| Performance | `quality/performance/` | quality | 🔲 Planned |
| Marketing | `growth/marketing/` | growth | 🔲 Planned |
| CRO | `growth/cro/` | growth | 🔲 Planned |

## Package拡張Skill（各Packageが定義）

| Skill群 | 定義元 | パス |
|---|---|---|
| Platform Skills（Auth / Stripe / Notification / Analytics / Monitoring / Storage / Security / Deployment / Feature Flag） | [`platform/README.md`](../platform/README.md) | `engineering/platform/*` |
| Design Skills（Figma System / UX Writing / Motion Design / Accessibility） | [`design/README.md`](../design/README.md) | `ui/*` `ux/*` |
| AI Skills（Prompt Engineering / Conversation Design / RAG / Agent Design / Evaluation / Safety） | [`ai/README.md`](../ai/README.md) | `engineering/ai/*` |
| Engineering Skills（Architecture / Database / API Design / Testing / Code Review） | [`engineering/README.md`](../engineering/README.md) | `engineering/backend/*` `quality/qa/*` |

**Status凡例**: 🔲 Planned / 🟡 Draft / ✅ Active / ⛔ Deprecated

### 追加ルール

1. Skill追加時は本レジストリと [`Skill_Architecture.md`](../00_System/Skill_Architecture.md) の一覧・Matrixを同時更新する
2. `registry.json`（機械可読レジストリ）は最初のSkill実体作成時に導入する（[`Skill_Base_Template.md — Library Structure`](../00_System/Skill_Base_Template.md) 参照）
3. Skillの実体作成は、対応するAgent・実案件の需要が発生した時点で行う（先回りで量産しない）
