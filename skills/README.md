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

## Business Launch Package の Skill（10 Skill・Status: Draft）

定義の正本は各 `SKILL.md`。Package は [`launch/README.md`](../launch/README.md)、実行Agentは [`agents/strategy/business-launch.md`](../agents/strategy/business-launch.md)。

| Skill | パス | カテゴリ | Status |
|---|---|---|---|
| Self Analysis | `business/self-analysis/` | business | 🟡 Draft |
| Company Analysis | `business/company-analysis/` | business | 🟡 Draft |
| Capital Planning | `business/capital-planning/` | business | 🟡 Draft |
| Incorporation Legal | `business/incorporation-legal/` | business | 🟡 Draft |
| Labor Management | `business/labor-management/` | business | 🟡 Draft |
| Payroll Design | `business/payroll-design/` | business | 🟡 Draft |
| Subsidy Research | `business/subsidy-research/` | business | 🟡 Draft |
| Back-office Design | `business/back-office-design/` | business | 🟡 Draft |
| Launch Planning | `business/launch-planning/` | business | 🟡 Draft |
| SNS Marketing Framework | `growth/sns-marketing-framework/` | growth | 🟡 Draft |

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
2. [`registry.json`](./registry.json)（機械可読レジストリ）は Business Launch Package の Skill 実体作成時に導入済み。Skill の追加・廃止のたびに更新する（[`Skill_Base_Template.md — Library Structure`](../00_System/Skill_Base_Template.md) 参照）
3. Skillの実体作成は、対応するAgent・実案件の需要が発生した時点で行う（先回りで量産しない）
