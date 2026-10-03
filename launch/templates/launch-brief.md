# Launch Brief — {{BUSINESS_NAME}}

> Business Launch Agent の**主成果物**。ビジネスモデルを出し、「〇〇をやります」を宣言し、そのために必要な情報・ツール・手続・資金・管理表までを1か所に束ねる。
> 配置先: `strategy/launch/launch-brief.md`（[`Project_Template.md`](../../00_System/Project_Template.md) の `strategy/` 配下）。個人情報・認証情報は書かない。

| 項目 | 内容 |
|---|---|
| **Project** | {{BUSINESS_NAME}} |
| **Version** | {{VERSION}} |
| **Status** | Draft / In Review / Approved |
| **Owner（人間）** | {{OWNER}} |
| **作成・更新日** | {{CREATED_DATE}} / {{UPDATED_DATE}} |
| **作成Agent** | `business-launch`（[`agents/strategy/business-launch.md`](../../agents/strategy/business-launch.md)） |
| **Confidence** | High / Medium / Low（根拠の強さ。Lowは人間レビュー必須） |
| **前提としている法令・制度の確認日** | {{LAW_CHECKED_DATE}}（これより古い場合は再確認） |

---

## 0. Intake（ヒアリング結果）

| 項目 | 回答 | 未確認なら「未確認」と書く |
|---|---|---|
| 立ち上げの目的（なぜやるか） | | |
| 投下できる自己資金 / 借入可能額 | | 生活防衛資金（創業者の生活費◯か月分）は別枠で確保 |
| 稼働できる時間（週◯時間）・期間 | | |
| 創業者のスキル・実績・人脈 | | |
| 本店所在地の想定（都道府県・市区町村） | | 補助金・届出の調査単位になる |
| 法人形態の希望 | | 未定なら `legal-setup-plan.md` で比較 |
| 共同創業者・従業員の予定 | | 労務・社会保険の要否に直結 |
| 許認可が必要になりそうな業種か | | |
| リスク許容度・撤退ライン | | |

---

## 1. ビジネスモデル宣言

> 私たちは **{{WHO}}** のために、**{{PROBLEM}}** を **{{SOLUTION}}** で解決し、**{{REVENUE_MODEL}}** で収益化します。

| 項目 | 内容 | 根拠（出典/仮説） |
|---|---|---|
| 顧客（誰の） | | |
| 課題（何に困っているか） | | |
| 解決策（何を提供するか） | | |
| 提供価値（なぜ選ばれるか） | | |
| 収益モデル・価格 | | |
| 集客チャネル | | |
| ユニットエコノミクス | LTV: / CAC: / LTV÷CAC: | [`kpi-kgi.csv`](./kpi-kgi.csv) |
| 競合との違い | | [`company-analysis.md`](./company-analysis.md) |
| 最重要の未検証仮説 | | 検証方法・期限を書く |

### Lean Canvas

| 課題 | 解決策 | 独自の価値提案 | 圧倒的な優位性 | 顧客セグメント |
|---|---|---|---|---|
| | | | | |

| 主要指標 | チャネル | コスト構造 | 収益の流れ |
|---|---|---|---|
| | | | |

---

## 2. 「〇〇をやります」— 最初の90日

| 項目 | 内容 |
|---|---|
| **やります（Do）** | 1. 2. 3.（最大5つ。動詞で書く） |
| **やりません（Don't）** | 1. 2.（スコープ膨張を防ぐ） |
| **成功条件（数値）** | 例: 90日で有料顧客◯人 / 売上◯円 / 問い合わせ◯件 |
| **撤退・見直し条件** | 例: 60日で問い合わせ◯件未満なら施策を見直す |
| **最初の1週間の行動** | |

---

## 3. 必要な情報ツール

→ [`tool-stack-proposal.md`](./tool-stack-proposal.md)

| カテゴリ | 採用（候補） | 必要度（必須/推奨/後回し） | 月額目安 | 導入時期 |
|---|---|---|---|---|
| | | | | |

---

## 4. 資金計画

→ [`capital-plan.md`](./capital-plan.md) / [`finance-plan.csv`](./finance-plan.csv)

| 項目 | Worst | Base | Best |
|---|---|---|---|
| 推奨資本金 | | | |
| 必要資金総額（設立費用＋初期投資＋運転資金） | | | |
| 資金ショート月 | | | |
| ランウェイ（月） | | | |

**資本金の決定（Gate L2）**: 未決 / 決定（日付・決定者）

---

## 5. 法人設立プラン

→ [`legal-setup-plan.md`](./legal-setup-plan.md) / [`legal-procedure-tracker.csv`](./legal-procedure-tracker.csv)

| 項目 | 内容 |
|---|---|
| 法人形態 | |
| 設立予定日（登記申請日） | |
| 許認可の要否 | |
| 依頼する士業 | 司法書士 / 税理士 / 社労士 / 行政書士 / 弁護士 |

---

## 6. 労務・給与

→ [`labor-setup-plan.md`](./labor-setup-plan.md) / [`payroll-simulation.csv`](./payroll-simulation.csv)

| 項目 | 内容 |
|---|---|
| 役員報酬（月額）案 | |
| 雇用予定（人数・時期・形態） | |
| 会社総コスト（月） | |
| 社会保険・労働保険の適用 | |

---

## 7. 補助金・助成金・融資

→ [`subsidy-tracker.csv`](./subsidy-tracker.csv)

| 制度 | 実施機関 | 適合度 | 想定受給額 | 申請期限 | 交付決定前の着手 |
|---|---|---|---|---|---|
| | | | | | |

---

## 8. マーケティング（SNS）

→ [`sns-marketing-framework.md`](./sns-marketing-framework.md) / [`sns-content-calendar.csv`](./sns-content-calendar.csv)

| 項目 | 内容 |
|---|---|
| 主チャネル / 副チャネル | |
| コンテンツピラー | |
| ファネルKPI（IMP→プロフィール→問い合わせ→購入） | |

---

## 9. 分析サマリ

| 分析 | 結論（So What） | 詳細 |
|---|---|---|
| 市場・企業分析 | | [`company-analysis.md`](./company-analysis.md) |
| 自社分析 | | [`self-analysis.md`](./self-analysis.md) |

---

## 10. 管理表

| 管理表 | 目的 | ファイル |
|---|---|---|
| WBS | 立ち上げ全工程のスケジュールと担当 | [`wbs-incorporation.csv`](./wbs-incorporation.csv) |
| 余日管理表（予実管理表） | 月次の予算と実績の差異管理 | [`budget-actual-tracker.csv`](./budget-actual-tracker.csv) |
| KPI-KGI | ファネル逆算とKPIツリー | [`kpi-kgi.csv`](./kpi-kgi.csv) |

---

## 11. リスク・前提・未確認事項（Open Issues）

| # | 種別（リスク/前提/未確認） | 内容 | 影響 | 対応・期限 | 担当 |
|---|---|---|---|---|---|
| 1 | | | | | |

> 「未確認」を空欄にしない。推測で埋めた箇所は Confidence を下げ、その旨をここに書く。

---

## 12. Human承認・士業確認ログ

| ゲート / 項目 | 判断者 | 日付 | 結果（承認/条件付き/差し戻し） | 条件・コメント |
|---|---|---|---|---|
| Gate L1 事業Go/No-Go | Owner | | | |
| Gate L2 資本・調達方針 | Owner（＋税理士） | | | |
| Gate L3 設立内容の最終確認 | Owner（＋司法書士等） | | | |
| Gate L4 開業前最終確認 | Owner | | | |
| 定款・登記内容 | 司法書士 | | | |
| 税務届出・消費税判断 | 税理士 | | | |
| 社会保険・労働保険・規程 | 社労士 | | | |
| 許認可 | 行政書士 | | | |
| 利用規約・契約・広告表示 | 弁護士 | | | |

---

## 13. Decision Log

| 日付 | 決定事項 | 選択肢 | 却下案と理由 | 決定者 |
|---|---|---|---|---|
| | | | | |

---

## 14. Handoff Note

- **From / To**: `business-launch` → `ceo`（Go/No-Go提案）/ `product-manager`（要件定義）
- **Deliverables**: 本書および §3〜§10 のリンク先一式
- **Summary**:（3行以内）
- **Decisions**:
- **Open Issues**: §11 を参照
- **Assumptions**:
- **QC Status**: PASS / WARNING / FAIL
