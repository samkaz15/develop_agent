# Entrepreneur Agent 構築指示

あなたはシニアAIアーキテクト兼、起業家・経営戦略コンサルタント・PMO・マーケティング責任者・CFOとして行動してください。

本プロジェクトでは、スタートアップおよびマーケティング会社の事業立ち上げ・事業運営・マーケティング施策実行・チーム管理・企業価値向上を一気通貫で支援する「Entrepreneur Agent」を構築します。

単なるアドバイスAIではなく、

「事業構想 → 市場分析 → 顧客価値定義 → ビジネスモデル設計 → 要件定義 → 作業要件 → プロジェクト化 → WBS → 担当割当 → 施策実行 → KPI計測 → 進捗管理 → 問題検知 → 改善施策 → 経営判断 → 企業価値向上」

までを管理できる実務型AIエージェントとして実装してください。

---

# 1. Entrepreneur Agentの最終目的

このAgentの目的は「良いアイデアを出すこと」ではありません。

最終目的を以下とします。

1. 顧客価値を作る
2. PMFを検証する
3. 売上を作る
4. 利益を作る
5. 再現性のある顧客獲得モデルを作る
6. 継続購入・LTVを向上させる
7. 業務を標準化する
8. 経営者依存を減らす
9. チームで再現可能な状態にする
10. キャッシュフローを最大化する
11. 競争優位性を蓄積する
12. 企業価値を向上させる

すべての提案について、

「この施策は何の企業価値を高めるのか？」

を説明できる状態にしてください。

---

# 2. Entrepreneur Agent Operating System

以下の構造で設計してください。

Entrepreneur Agent
│
├── 01 Strategy Agent
├── 02 Market Research Agent
├── 03 Customer Agent
├── 04 Value Proposition Agent
├── 05 Business Model Agent
├── 06 Product Agent
├── 07 Requirement Definition Agent
├── 08 Work Requirement Agent
├── 09 PMO Agent
├── 10 WBS Agent
├── 11 Marketing Strategy Agent
├── 12 Marketing Execution Agent
├── 13 Growth Agent
├── 14 Sales Agent
├── 15 CRM / Retention Agent
├── 16 Finance Agent
├── 17 KPI Agent
├── 18 Team Management Agent
├── 19 Risk Agent
├── 20 Experiment Agent
├── 21 Operations Agent
├── 22 Management Review Agent
├── 23 Competitive Intelligence Agent
├── 24 Corporate Value Agent
└── 25 M&A Readiness Agent

親AgentであるEntrepreneur Agentが各専門Agentを統括してください。

---

# 3. Strategy Agent

以下を定義します。

・Mission
・Vision
・Value
・Why Now
・事業目的
・3年目標
・1年目標
・Quarter Goal
・North Star Metric
・KGI
・KPI
・KSF
・戦略仮説
・競争戦略
・成長戦略
・撤退条件

戦略から実行施策まで論理的につながっている状態を維持してください。

---

# 4. Startup Framework Library

以下のフレームワークを実装してください。

## 市場分析

・PEST / PESTEL
・5 Forces
・3C
・市場規模分析
・TAM / SAM / SOM
・市場成長率
・競合分析
・Competitive Landscape
・Positioning Map

## 顧客分析

・STP
・Persona
・ICP
・JTBD
・Customer Journey Map
・Pain / Gain
・VOC分析
・購買障壁分析

## 価値設計

・Value Proposition Canvas
・USP
・UVP
・Moat
・Switching Cost
・Network Effect
・Brand Equity

## ビジネスモデル

・Business Model Canvas
・Lean Canvas
・Revenue Model
・Pricing Model
・Unit Economics
・CAC
・LTV
・LTV/CAC
・Payback Period
・Contribution Margin

## Growth

・AARRR
・Growth Loop
・Growth Funnel
・Pirate Metrics
・Cohort Analysis
・Retention Curve
・Referral Loop

## 戦略

・SWOT
・TOWS
・Ansoff Matrix
・BCG Matrix
・Blue Ocean Strategy
・Porter's Generic Strategies

## Startup Execution

・Lean Startup
・MVP
・Build → Measure → Learn
・Hypothesis Testing
・Experiment Backlog
・ICE
・RICE
・Impact / Effort Matrix

ただし、フレームワークを機械的に全部使ってはいけません。

事業フェーズと課題を判定し、必要なものだけ選択してください。

---

# 5. Requirement Definition Agent

事業・プロジェクト開始時に「要件定義書」を生成してください。

最低限、

・背景
・目的
・解決する課題
・対象顧客
・Stakeholder
・Scope
・Out of Scope
・Business Requirements
・Functional Requirements
・Non-functional Requirements
・Marketing Requirements
・Data Requirements
・Operational Requirements
・Security Requirements
・Legal / Compliance Requirements
・Dependencies
・Constraints
・Acceptance Criteria
・KPI
・Deliverables
・Milestone

を定義してください。

曖昧な要求をそのままWBSにしてはいけません。

---

# 6. Work Requirement Agent

要件定義から実際の作業要件書を生成します。

各Taskについて、

Task ID
Project
Workstream
Task
Purpose
Requirement
Input
Process
Output
Definition of Done
Owner
Reviewer
Priority
Dependency
Start Date
Due Date
Estimated Hours
Actual Hours
Status
Progress %
KPI Impact
Risk
Notes

を管理してください。

---

# 7. WBS Agent

要件定義書・作業要件書からWBSを自動生成してください。

階層：

L0 Business
L1 Project
L2 Workstream
L3 Deliverable
L4 Task
L5 Subtask

各Taskに必ず、

Owner
Deadline
Dependency
Priority
Status
Progress
Estimated Hours
Actual Hours
KPI
Deliverable
Definition of Done

を設定してください。

---

# 8. Schedule / Buffer Management

余日管理表を作成してください。

各プロジェクトについて、

Deadline
Required Finish Date
Current Forecast
Buffer Days
Buffer Consumption
Schedule Variance
Critical Path
Delay Risk

を計算してください。

Buffer Status：

GREEN
YELLOW
RED
CRITICAL

の4段階で管理してください。

遅延発生後ではなく、

「このまま進むと何日後に遅延する可能性があるか」

を検知してください。

---

# 9. Team Execution Management

チームメンバーごとに、

担当Task
期限
進捗率
予定工数
実績工数
遅延Task
Blocked Task
成果物
レビュー状況
KPI Contribution

を管理してください。

ただし、単純な作業量だけで個人評価をしないでください。

評価対象は、

Output
Quality
Deadline
Business Impact

を中心とします。

---

# 10. Marketing Strategy Agent

以下を設計してください。

Market
Segment
ICP
Persona
Positioning
Offer
Message
Channel
Funnel
CTA
Conversion Point
Retention
Referral

チャネル例：

SEO
Google Ads
Meta Ads
TikTok
Instagram
X
YouTube
Email
LINE
Affiliate
Influencer
PR
Community

チャネルごとに、

Objective
Target
Creative
Offer
CTA
Budget
KPI
CAC
CVR
ROAS
LTV
Payback Period

を管理してください。

---

# 11. Marketing Execution Agent

戦略を「施策」に変換してください。

例えば、

「TikTokを伸ばす」

ではTaskとして認めません。

必ず、

企画
競合調査
Hook作成
Script作成
撮影
編集
Thumbnail
Caption
投稿
Analytics
改善

まで分解してください。

各施策には、

Hypothesis
Action
Expected Result
KPI
Owner
Deadline
Result
Learning
Next Action

を設定してください。

---

# 12. Experiment Engine

すべてのマーケティング改善を実験として管理してください。

Experiment ID
Hypothesis
Variable
Control
Treatment
Primary KPI
Secondary KPI
Start
End
Sample
Result
Interpretation
Decision

Decision：

Scale
Continue
Modify
Stop

実験結果をKnowledge Baseへ保存してください。

同じ失敗を繰り返さない構造にしてください。

---

# 13. KPI Tree

KGIから施策まで分解してください。

例：

Enterprise Value
↓
Revenue / EBITDA / FCF
↓
Customers × ARPU
↓
Traffic × CVR × ARPU
↓
Channel
↓
Campaign
↓
Creative
↓
Task

「このTaskがどのKPIに接続しているか」を追跡可能にしてください。

KPIにつながらないTaskは警告してください。

---

# 14. Financial Management

以下を管理してください。

Revenue
COGS
Gross Profit
OPEX
EBITDA
Operating Profit
FCF
Cash Balance
Burn Rate
Runway

Unit Economics：

CAC
LTV
ARPU
Gross Margin
Churn
Retention
Payback Period
LTV/CAC

Budget vs Actualも管理してください。

---

# 15. Corporate Value Agent

Entrepreneur Agentの重要機能です。

企業価値の源泉を、

Revenue Growth
Margin
Recurring Revenue
Retention
CAC Efficiency
LTV
Brand
Customer Base
Technology
Data
IP
Network Effect
Switching Cost
Operational Efficiency
Founder Dependency

に分解してください。

そして、

「現在この会社の価値はどこに蓄積されているのか？」

を常に説明できる状態にしてください。

---

# 16. Founder Dependency Index

以下を測定してください。

Sales Dependency
Marketing Dependency
Product Dependency
Relationship Dependency
Decision Dependency
Operational Dependency

Founder Dependency Scoreを作成してください。

Founderが30日間不在でも事業が正常運営できる状態を目標としてください。

---

# 17. M&A Readiness Agent

以下を監視してください。

Financial Records
Recurring Revenue
Customer Concentration
Founder Dependency
Contracts
IP Ownership
Data Quality
Legal Risk
Operational Documentation
Management Team
Growth Rate
Profitability
Retention
Customer Acquisition
Security
Compliance

M&A準備状況について、

不足項目
改善Task
Owner
Deadline

までWBSへ戻してください。

企業価値について単純な固定倍率を使用しないでください。

DCF、Trading Comparables、Precedent Transactionsなど、目的に応じた評価方法を使い分けられる設計にしてください。

---

# 18. Management Review

Daily / Weekly / Monthly / Quarterly Reviewを実装してください。

## Daily

昨日の成果
今日のPriority
Blocked
Deadline Risk
重要KPI異常

## Weekly

KPI
Plan vs Actual
Experiment Result
Marketing Performance
Sales
Project Progress
Team Capacity
Risk
Decision Required
Next Week Priority

## Monthly

P/L
Cash Flow
Growth
CAC
LTV
Retention
Channel Performance
Budget Variance
Business Value
Strategic Issues

## Quarterly

Strategy
Market
Product
Growth
Finance
Organization
Moat
Corporate Value
Next Quarter OKR

---

# 19. Decision Log

重要な意思決定について、

Decision ID
Date
Issue
Options
Decision
Reason
Expected Impact
Owner
Review Date
Actual Result

を保存してください。

「なぜその意思決定をしたのか」を後から追跡可能にします。

---

# 20. Risk Register

Risk ID
Category
Description
Probability
Impact
Risk Score
Owner
Mitigation
Contingency
Status

を管理してください。

カテゴリー：

Market
Product
Marketing
Finance
Operations
People
Legal
Technology
Security

---

# 21. Single Source of Truth

情報が複数ファイルに分散して矛盾しないようにしてください。

以下をSingle Source of Truthとして設計してください。

Company
Strategy
Projects
Tasks
Team
KPI
Finance
Marketing
Experiments
Customers
Risks
Decisions
Corporate Value

各Agentは同じデータモデルを参照してください。

---

# 22. Agent Automation

Agentは毎回人間から質問されるまで待つだけではなく、データ更新時に以下を検知できる設計にしてください。

KPI異常
期限超過
Buffer消費
CAC悪化
CVR低下
Retention低下
Cash不足
Budget超過
Task Block
Dependency遅延
Experiment終了
Founder Dependency上昇

問題を検知した場合、

Detect
↓
Diagnose
↓
Prioritize
↓
Recommend
↓
Create Task
↓
Assign
↓
Track
↓
Review

まで処理できる構造にしてください。

ただし、重要な経営判断・予算変更・契約・外部公開・削除などは人間の承認を必要としてください。

---

# 23. Priority Engine

全Taskを、

Business Impact
Urgency
KPI Impact
Revenue Impact
Customer Impact
Risk Reduction
Effort
Dependency

で評価してください。

優先順位：

P0 Critical
P1 High
P2 Medium
P3 Low

ただしAIが勝手に優先度を確定するのではなく、理由と根拠を表示し、人間がOverrideできるようにしてください。

---

# 24. Entrepreneur Dashboard

以下を1画面で確認できるDashboardを設計してください。

North Star Metric

KGI
KPI

Revenue
EBITDA
Cash
Runway

CAC
LTV
LTV/CAC
Retention
Churn

Active Projects
Project Progress
Delayed Tasks
Critical Tasks
Buffer Status

Marketing Channel Performance
Experiments

Team Workload
Blocked Tasks

Top Risks
Decision Required

Corporate Value Drivers
Founder Dependency

そして最後に、

「今週経営者が意思決定すべきTOP5」

を表示してください。

---

# 25. AI出力ルール

AIは抽象論で終了してはいけません。

悪い例：

「SNSを強化しましょう」

良い例：

TikTok Organic Acquisition改善

Hypothesis:
冒頭3秒の離脱率改善によって平均視聴時間が上昇する。

Action:
既存上位10動画のHookを分析し、新Hookを20本作成する。

Owner:
Marketing Team

Deadline:
YYYY-MM-DD

Primary KPI:
3-second retention

Secondary KPI:
Average Watch Time

Expected Impact:
Organic Traffic増加

Definition of Done:
20本のHook制作＋5本投稿＋結果測定完了

Next Action:
勝ちHookを次の20本へ展開

この粒度まで落としてください。

---

# 26. Repository Design

既存Repositoryを最初に解析してください。

既存構造を破壊しないでください。

推奨構造：

/entrepreneur-agent
    /agents
    /strategy
    /requirements
    /projects
    /wbs
    /marketing
    /experiments
    /finance
    /kpi
    /team
    /operations
    /risk
    /valuation
    /ma
    /reviews
    /knowledge
    /schemas
    /prompts
    /tests
    /docs

各Agentについて、

mission
responsibility
input
process
output
tools
permissions
escalation
schema

を定義してください。

---

# 27. Data Schema

最低限、

company.json
strategy.json
project.json
task.json
team.json
kpi.json
marketing.json
experiment.json
finance.json
risk.json
decision.json
valuation.json

のSchemaを設計してください。

IDによって相互参照可能にしてください。

例：

Company
↓
Objective
↓
KGI
↓
KPI
↓
Project
↓
Task
↓
Experiment
↓
Result

という因果関係を追跡できる構造にしてください。

---

# 28. 実装原則

以下を守ってください。

・既存コードを最初に解析する
・既存機能を壊さない
・重複Agentを作らない
・責務を明確にする
・Schemaを統一する
・可能な限り型を定義する
・Validationを実装する
・Error Handlingを実装する
・Loggingを実装する
・Testを作る
・Documentationを作る
・Human Approval Pointを設定する
・重要データ変更にはAudit Logを残す
・Agent間の無限ループを防止する

---

# 29. 実装手順

いきなりコードを書き始めないでください。

Phase 1
Repository解析

Phase 2
現在のArchitectureを説明

Phase 3
不足機能のGap Analysis

Phase 4
Entrepreneur Agent Architecture設計

Phase 5
Data Model設計

Phase 6
Agent Responsibility設計

Phase 7
Implementation Plan作成

Phase 8
WBS作成

Phase 9
実装

Phase 10
Test

Phase 11
Documentation

Phase 12
実際のサンプル事業を入力してEnd-to-End Test

の順番で進めてください。

---

# 30. 最終Acceptance Criteria

以下が実際に動作することを確認してください。

新規事業を登録
↓
市場・顧客分析
↓
Value Proposition作成
↓
Business Model作成
↓
事業目標設定
↓
KGI/KPI設定
↓
要件定義書作成
↓
作業要件書作成
↓
Project生成
↓
WBS生成
↓
担当者設定
↓
施策実行
↓
KPI入力
↓
Plan vs Actual分析
↓
問題検知
↓
改善案作成
↓
Experiment生成
↓
結果記録
↓
Knowledge蓄積
↓
次施策生成
↓
財務数値へ反映
↓
Corporate Value Driver更新
↓
Management Review生成

ここまでが一つのループとして接続されていること。

Entrepreneur Agentの最終的な役割は、

「経営者の代わりに会社を経営するAI」

ではありません。

「経営者が正しい情報を見ながら、事業価値を高める意思決定を高速で行い、その意思決定をチームの具体的な実行まで落とし込む経営OS」

として構築してください。
