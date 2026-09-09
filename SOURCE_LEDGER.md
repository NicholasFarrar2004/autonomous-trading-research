> Historical research snapshot from September 8, 2026. Sources and prices can change. Later implementation results are documented in README.md. Private coordination and personal constraints are omitted.

# Autonomous trading: source and evidence ledger

Status: Initial bounded review recorded; investment conclusion remains provisional.
Updated: 2026-09-08 17:05 EDT


## Provenance

Entries combine originating-task evidence packets with selected direct checks on September 8, 2026. D means the file owner directly opened the source and checked the specified claim on that date. R means relayed primary-source reading by the originating research team, not reverified by the file owner. F means the file owner's fetch failed. D/R separates directly checked facts from additional relayed details. Access to text does not constitute an independent account audit. Sources without supplied publication dates remain undated here; snapshot dates are not current performance claims. Repositories are mutable and were not commit-pinned.

Grades describe evidence, not expected returns: A = independently audited/reconciled live account and reproducible implementation (none established); B+ = transaction-grounded empirical reconstruction; B = primary author/operator live report; B- = partial account/log evidence with attribution or verification gaps; C = simulation, backtest, model, or methodological evidence; U = unresolved. Tooling alone receives no profit grade. Negative outcomes can have stronger evidence than positive claims.

## S01 , TradingAgents

- Source: [TradingAgents](https://github.com/TauricResearch/TradingAgents)
- Environment / grade: Tooling / no profit grade
- Provenance: D
- Finding: Research framework; README describes simulated execution. Current August v0.4.0 announcement reports point-in-time/lookahead fixes.
- Limits / next verification: Originating task retrieved a Reproducibility section at lines 343–356 warning about current news/social inputs; file-owner snapshot lacks it. Unresolved retrieval/version discrepancy; audit actual historical inputs before reliance. Fix announcements are not a code audit.

## S02 , TradingAgents paper v7

- Source: [TradingAgents paper v7](https://arxiv.org/html/2412.20138v7)
- Environment / grade: Backtest / C
- Provenance: R
- Finding: Section 5.1: January 1–March 29, 2024 historical simulation, narrow technology universe.
- Limits / next verification: Not live capital. Relayed HTML formatting anomalies include placeholder names; avoid elevating headline metrics.

## S03 , AI Hedge Fund

- Source: [AI Hedge Fund](https://github.com/virattt/ai-hedge-fund)
- Environment / grade: Tooling / no profit grade
- Provenance: R
- Finding: Educational README says no actual trades despite roadmap.
- Limits / next verification: Roadmap does not establish implementation or profitable execution.

## S04 , Freqtrade Strategy 101

- Source: [Freqtrade Strategy 101](https://docs.freqtrade.io/en/stable/strategy-101/)
- Environment / grade: Tooling / no profit grade
- Provenance: R
- Finding: Explains dry-run and warns ranked backtests can be unrealistic.
- Limits / next verification: Useful existing infrastructure, not a profitable strategy by itself.

## S05 , Freqtrade lookahead analysis

- Source: [Freqtrade lookahead analysis](https://www.freqtrade.io/en/stable/lookahead-analysis/)
- Environment / grade: Tooling / no profit grade
- Provenance: R
- Finding: Tool detects future-data bias.
- Limits / next verification: Passing one diagnostic is not universal proof of unbiased or profitable results.

## S06 , NostalgiaForInfinity

- Source: [NostalgiaForInfinity](https://github.com/iterativv/NostalgiaForInfinity)
- Environment / grade: Backtest / C
- Provenance: R
- Finding: Backtest references in commit comments; no independent live record located in this review.
- Limits / next verification: Search gap does not prove no live record exists; verify revision, equity, costs, and forward results.

## S07 , Prediction Arena v1

- Source: [Prediction Arena v1](https://arxiv.org/html/2604.07355v1)
- Environment / grade: Live capital / B
- Provenance: D
- Finding: Main six-model live cohort lost 16.0%–30.8%, January 12–March 9, 2026. Appendix B.2 directly checked: earlier 23-day real-capital run +10.9%/$1,090.32, 112 trades, 4.1% drawdown; same model later lost.
- Limits / next verification: Author report, not our account audit. Separate three-day paper cohort. Calendar dates of earlier run not established here.

## S08 , FINSABER v4

- Source: [FINSABER v4](https://arxiv.org/html/2505.07078v4)
- Environment / grade: Backtest / C
- Provenance: D/R
- Finding: Broad two-decade, 100+ symbol evaluation challenges earlier LLM advantage. Section 6.1 commissions: $0.0049/share, $0.99 minimum/order, directly checked.
- Limits / next verification: Cost specification is a paper assumption, not a current broker quote or complete execution-cost model. Broader findings relayed; earlier window October 6, 2022–April 10, 2023.

## S09 , FINSABER code

- Source: [FINSABER code](https://github.com/waylonli/FINSABER)
- Environment / grade: Tooling / no profit grade
- Provenance: R
- Finding: Associated reproducibility code.
- Limits / next verification: Availability is not independent reproduction; pin revision/configuration.

## S10 , Evaluation survey v1

- Source: [Evaluation survey v1](https://arxiv.org/html/2605.19337v1)
- Environment / grade: Survey / C
- Provenance: R
- Finding: 77 included studies; primary subset 19: 2/19 extractable temporal splits, 1/19 explicit costs, none R3.
- Limits / next verification: Author coding, not entire-field prevalence. Verify R3 definition before using taxonomy.

## S11 , AMA v1

- Source: [AMA v1](https://arxiv.org/html/2510.11695v1)
- Environment / grade: Unresolved or paper / U
- Provenance: R
- Finding: Positive two-month outcomes; linked dashboard appears paper trading.
- Limits / next verification: Real funds not established. Do not relabel as live success.

## S12 , StockBench v1

- Source: [StockBench v1](https://arxiv.org/html/2510.02209v1)
- Environment / grade: Simulation / C
- Provenance: R
- Finding: Sections 2.1–2.2: 20 high-weight Dow stocks, March 3–June 30, 2025, opening-price simulated fills; mixed outcomes.
- Limits / next verification: Model cutoff assumptions need refreshing for modern models; no audited live profitability.

## S13 , AI-Trader v1

- Source: [AI-Trader v1](https://arxiv.org/html/2512.10971v1)
- Environment / grade: Benchmark / C
- Provenance: R
- Finding: Mixed benchmark outcomes.
- Limits / next verification: Not independently audited deployable profit; exact environment and cost treatment remain extraction gaps.

## S14 , TradingAgents replication

- Source: [TradingAgents replication](https://github.com/lucas020695/tradingagents_replicated)
- Environment / grade: Backtest / U
- Provenance: R
- Finding: README calls Q1 2024 305 trading days and shows identical LLM/MACD returns, trades, and costs.
- Limits / next verification: Internal consistency concern, not an accusation of fraud. Reconcile labels and raw outputs before relying on replication.

## S15 , Schwertfeger/Vogt journal paper

- Source: [Schwertfeger/Vogt journal paper](https://www.sciencedirect.com/science/article/pii/S0378426626000956)
- Environment / grade: Live capital / B
- Provenance: R/F
- Finding: Four live arbitrage bots; aggregate realized $20,237.48. Three returns 24.91%, 33.35%, 17.39% for November 27–December 31, 2023; fourth 6.15% September 12–October 8, 2024.
- Limits / next verification: Short windows; full cost/return-denominator audit unresolved; no public strategy repo located; data on request. Direct access failed here; originating task verified the abstract through search, not a full-paper audit; see S44.

## S16 , Arbitrage author preprint

- Source: [Arbitrage author preprint](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5055292)
- Environment / grade: Live capital / B
- Provenance: R/F
- Finding: Companion to S15.
- Limits / next verification: Direct fetch returned 403. Do not double-count as independent study or verification.

## S17 , APOLLO NDSS paper

- Source: [APOLLO NDSS paper](https://www.ndss-symposium.org/wp-content/uploads/2026-s506-paper.pdf)
- Environment / grade: On-chain reconstruction / B+
- Provenance: D/R
- Finding: Introduction directly confirms 2,052 bots, 2,516,236 transactions, about $40m profit, 75.3% relying on off-chain logic. Review reports January 2023–December 2024 and transaction fees subtracted.
- Limits / next verification: Aggregate is not entrant success or all-in profit. Categories include arbitrage, liquidation, and sandwich activity; not all desirable or deployable. No independent reconstruction by us.

## S18 , APOLLO code

- Source: [APOLLO code](https://github.com/sec-study-dev/apollo)
- Environment / grade: Analysis tool / no profit grade
- Provenance: R
- Finding: Research analysis implementation.
- Limits / next verification: Not a ready-to-run profitable bot; on-chain contracts omit much off-chain strategy logic.

## S19 , TTS Myfxbook account

- Source: [TTS Myfxbook account](https://www.myfxbook.com/members/TradingShelter/tts-bot/11932605)
- Environment / grade: Account-linked live claim / B-
- Provenance: R
- Finding: Snapshot: +482.50%; EUR5,000 deposits, EUR29,115.59 equity, 875 trades, 40.66% drawdown, EUR2,560.86 commissions.
- Limits / next verification: History private; badge verification not established through text. Automation/source linkage is operator claim. Start/end period not supplied; no annualization or cross-system ranking warranted.

## S20 , TTS operator

- Source: [TTS operator](https://ttsautomation.com/)
- Environment / grade: Operator claim / U
- Provenance: R
- Finding: Proprietary bot linked to S19.
- Limits / next verification: Affiliate broker incentives; no audited open strategy linkage. Not independent corroboration.

## S21 , Project Haystack

- Source: [Project Haystack](https://sbrn.io/projecthaystack/)
- Environment / grade: Operator live claim / B-
- Provenance: R
- Finding: July 9–September 1 snapshot: capital $4,803.66, marked holdings $5,225.64, +8.78%, 36 holdings, zero sells/realized profit; cash-flow-matched SPY $4,855.10.
- Limits / next verification: Operator report, 55-day window. September 4 search result +11.62% is a different snapshot; do not call either current or combine them.

## S22 , Mr Scrooge repository

- Source: [Mr Scrooge repository](https://github.com/BrockStar3540/mr-scrooge-v6)
- Environment / grade: Practice headline / C
- Provenance: R
- Finding: +10.54% practice claim.
- Limits / next verification: Must distinguish practice from S23 live-labeled operator log.

## S23 , Mr Scrooge equity log

- Source: [Mr Scrooge equity log](https://raw.githubusercontent.com/BrockStar3540/mr-scrooge-v6/main/livelog/equity.csv)
- Environment / grade: Live-labeled operator log / B-
- Provenance: D
- Finding: Direct CSV: July 29, 2026 11:13:14Z NAV 2500.00; September 8 20:15:02Z NAV 1878.56, terminal net_deposits 0.00. Computed endpoint change -24.8576%.
- Limits / next verification: Calculation (1878.56/2500-1)*100, conditional on complete accurate cash-flow record. Operator data, not brokerage audit. Ending NAV includes unrealized positions.

## S24 , Nof1 investor release

- Source: [Nof1 investor release](https://www.nasdaq.com/press-release/sui-group-co-leads-15-million-funding-round-ai-trading-lab-nof1-makes-strategic)
- Environment / grade: Interested-party claim / U
- Provenance: R
- Finding: Investor release reports six profitable of 32 result sets.
- Limits / next verification: Corporate interested source, not independent exchange validation; direct Nof1 access 403 in originating review and wallet reconciliation unresolved.

## S25 , Unverified Nof1 affiliation repository

- Source: [Unverified Nof1 affiliation repository](https://github.com/alphaarenanof1ai/nof1ai-alpha-arena)
- Environment / grade: Simulated example / U
- Provenance: R
- Finding: Example results explicitly simulated.
- Limits / next verification: Do not label official Nof1 or infer affiliation from name.

## S26 , pysystemtrade

- Source: [pysystemtrade](https://github.com/pst-group/pysystemtrade)
- Environment / grade: Existing infrastructure / no profit grade
- Provenance: R
- Finding: Open systematic-trading infrastructure; author has live performance discussion.
- Limits / next verification: Public code alone does not identify exact live configuration or establish reproducibility; futures add operational complexity.

## S27 , Carver annual performance

- Source: [Carver annual performance](https://qoppac.blogspot.com/2025/04/annual-performance-update-returneth.html)
- Environment / grade: Operator live report / B
- Provenance: R
- Finding: UK year ended April 5, 2025: futures account -16.3% net; commissions 0.29%, slippage 0.56% of starting capital; pure futures marked return -14.5%.
- Limits / next verification: Transparent operator disclosure, not independent audit. Account and pure-futures measures differ; do not cherry-pick one.

## S28 , AQR century of trend following

- Source: [AQR century of trend following](https://www.aqr.com/-/media/AQR/Documents/Insights/Journal-Article/AQR-JPM-Fall-2017.pdf)
- Environment / grade: Historical simulation / C
- Provenance: R
- Finding: Long historical simulated support with modeled costs.
- Limits / next verification: Institutional and often diversified futures evidence does not establish a retail ETF rule; assess assumptions and cash/volatility exposure.

## S29 , Faber tactical allocation

- Source: [Faber tactical allocation](https://papers.ssrn.com/sol3/Papers.cfm?abstract_id=962461)
- Environment / grade: Model evidence / C
- Provenance: R
- Finding: Includes 2008–2012 post-publication model evidence.
- Limits / next verification: Post-publication is useful but not brokerage audit or a current live result.

## S30 , Kim/Tse/Wald time-series momentum

- Source: [Kim/Tse/Wald time-series momentum](https://www.sciencedirect.com/science/article/pii/S1386418116301379)
- Environment / grade: Historical analysis / C
- Provenance: R
- Finding: 55 futures, 1985–2013; 1985–2009 scaled momentum alpha 1.08% monthly versus 0.39% unscaled, latter statistically indistinguishable from unscaled buy-and-hold; underperformed 2009–2013.
- Limits / next verification: Scaling explains much of reported edge; ensure like-for-like risk/exposure comparison.

## S31 , Huang et al. momentum

- Source: [Huang et al. momentum](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3165284)
- Environment / grade: Historical analysis / C
- Provenance: R
- Finding: Little individual-asset in/out-of-sample predictability reported.
- Limits / next verification: Qualifies broad trend narratives; extract exact specification before transferring conclusion to any candidate.

## S32 , Yang et al. technical rules

- Source: [Yang et al. technical rules](https://www.sciencedirect.com/science/article/abs/pii/S0927538X18300775)
- Environment / grade: Historical analysis / C
- Provenance: R
- Finding: 15,376 monthly rules; none beat equal-weight buy-and-hold after corrections.
- Limits / next verification: Multiple-testing correction matters; not a proof against every prespecified future rule.

## S33 , BIS crypto carry

- Source: [BIS crypto carry](https://www.bis.org/publ/work1087.pdf)
- Environment / grade: Historical market study / C
- Provenance: R
- Finding: Historical basis extremes of 60% annualized.
- Limits / next verification: Not net yield or current opportunity. Margin, liquidation, counterparty exposure, changing funding, and post-spot-ETF basis compression matter; no live yield assumed.

## S34 , Put-write performance study

- Source: [Put-write performance study](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3393940)
- Environment / grade: Hypothetical index / C
- Provenance: R
- Finding: PUT 1986–2018: CAGR 9.54%, volatility 9.95%, maximum drawdown -32.7%, longest drawdown 40 months.
- Limits / next verification: Not live retail net performance; short-volatility risk compensation, execution and capital differ.

## S35 , Option-selling index study

- Source: [Option-selling index study](https://faculty.providence.edu/en/publications/35-year-performance-analysis-of-cboe-sampp-500-option-selling-ind-2/)
- Environment / grade: Index research / C
- Provenance: R
- Finding: Context for short-volatility compensation.
- Limits / next verification: Does not certify an autonomous retail options strategy.

## S36 , AMM profitability study v1

- Source: [AMM profitability study v1](https://arxiv.org/html/2404.05803v1)
- Environment / grade: Historical/model analysis / C
- Provenance: R
- Finding: January 2022–December 2023 WETH-USDC 5bp pool fees around 80% of modeled arbitrage losses, with exceptions.
- Limits / next verification: Benchmark measure, not total cash P&L; does not generalize directly to centralized order books.

## S37 , AMM loss mechanism

- Source: [AMM loss mechanism](https://arxiv.org/abs/2208.06046)
- Environment / grade: Mechanism research / C
- Provenance: R
- Finding: Provides mechanism context for liquidity-provider losses.
- Limits / next verification: Theory is not a current, deployable profit record.

## S38 , PlainTape dashboard

- Source: [PlainTape dashboard](https://plaintape.fund/)
- Environment / grade: Operator live / B
- Provenance: D
- Finding: August 17, 2026 snapshot: +38.1% since November 2025, +41.3% YTD, Sharpe 1.67, drawdown -8.4%. August 7 restatement: inception 42.16% to 40.65%, YTD 45.47% to 43.92%.
- Limits / next verification: Three opening deposit days remain zeroed; body NAV-cost claims and footer estimated-cost language need reconciliation. Actual account range $150,000–300,000. Not audited or current.

## S39 , PlainTape methodology

- Source: [PlainTape methodology](https://plaintape.fund/methodology/)
- Environment / grade: Operator methodology / B
- Provenance: D/R
- Finding: Reported series begins November 4, 2025; earlier live history from late 2024 excluded for gaps. Review identifies 269 futures, 25% volatility target, 40 rules and $500,000 sizing notional.
- Limits / next verification: Notional is not account equity. Full ledger/cash-flow and cost reconciliation outstanding; self-described compliance is not independent certification.

## S40 , PlainTape about

- Source: [PlainTape about](https://plaintape.fund/about/)
- Environment / grade: Operator attribution / B
- Provenance: R
- Finding: Daily rebalancing/hourly execution; originating task traced public operator GitHub.
- Limits / next verification: Public identity linkage is not exact deployed-code-to-account verification.

## S41 , PlainTape operational status

- Source: [PlainTape operational status](https://plaintape.fund/slo/)
- Environment / grade: Operator operations / B
- Provenance: R
- Finding: August 17 snapshot overall FAIL.
- Limits / next verification: Dated snapshot only, not present health. Reconcile failure relevance before considering operation.

## S42 , PlainTape public fork

- Source: [PlainTape public fork](https://github.com/garcia42/pysystemtrade)
- Environment / grade: Verified repository / no profit grade
- Provenance: R
- Finding: Originating task directly opened public fork of pst-group/pysystemtrade.
- Limits / next verification: Exact deployed revision, modifications and performance attribution unverified.

## S43 , PlainTape linked GitHub identity

- Source: [PlainTape linked GitHub identity](https://github.com/garcia42)
- Environment / grade: Attribution / no profit grade
- Provenance: R
- Finding: Originating task followed About page link to this identity and S42.
- Limits / next verification: Identity linkage does not audit broker results.

## S44 , University author research page

- Source: [University author research page](https://emwifo.ovgu.de/emwifo/en/Research.html)
- Environment / grade: Publication corroboration / no extra profit grade
- Provenance: R
- Finding: Originating task confirms accessible primary publication and realized-trading research reference for S15.
- Limits / next verification: Not an independent account audit; does not resolve full-paper cost/denominator access gap.

## S45 , Carver year 12

- Source: [Carver year 12](https://qoppac.blogspot.com/2026/04/annual-performance-update-year-12.html)
- Environment / grade: Operator multiyear live / B
- Provenance: D/R
- Finding: April 6, 2025–April 5, 2026 futures +23.7% net; prior year -16.3%. Long-run mean 13.8%, volatility 17.3%, rf-zero Sharpe 0.80.
- Limits / next verification: 13.0% CAGR is monthly volatility-adjusted, not unqualified account CAGR. Total portfolio +6.4% is separate. Still below April 2024 high; no independent audit.

## S46 , Hummingbot beta competition

- Source: [Hummingbot beta competition](https://hummingbot.org/blog/-beta-bot-battle-results-and-roundup/)
- Environment / grade: Short participant live claims / B-
- Provenance: D/R
- Finding: September 2023, 48 hours; published October 12, 2023. Winner 134.72 USDT, runner WeGotGame 11.24; other eligible entrants negative. Runner adapted market_making_dman_v2.
- Limits / next verification: Participant CSVs, tiny window. Footer update is not event date. No dependable-profit claim.

## S47 , Hummingbot related analytics

- Source: [Hummingbot related analytics](https://gist.github.com/fengtality/8970b8ce67bc84dc5047ab729922d44d)
- Environment / grade: Related analysis artifact / no profit grade
- Provenance: R
- Finding: Competition-related analytics code.
- Limits / next verification: Do not treat analytics as full winning strategy or exact result reproduction.

## S48 , Liquidity miner interview

- Source: [Liquidity miner interview](https://hummingbot.org/blog/interview-with-liquidity-miner-dominator008/)
- Environment / grade: Operator interview / B-
- Provenance: R
- Finding: More than 10 ETH rewards; trading described as approximately break-even/slightly profitable before rewards.
- Limits / next verification: Rewards are economically distinct from spread/trading profit; availability and persistence unverified.

## S49 , openthomas

- Source: [openthomas](https://github.com/PredictionMarketTrader/openthomas)
- Environment / grade: Related architecture and replay / C
- Provenance: D/R
- Finding: MIT repository; weather baseline, bounded LLM adjustments, calibration, deterministic risk controls, paper default.
- Limits / next verification: README positive +10.9% cites another project. Own replay negative then near-breakeven variants; no own profitable live record established.

## S50 , Passivbot

- Source: [Passivbot](https://github.com/enarjord/passivbot)
- Environment / grade: Strategy and framework / author-linked live
- Provenance: D/R
- Finding: Unlicense, Python/Rust, shared live/backtest planner; current v8.1 trailing-martingale default versus earlier v7 grid default. Official reference-vault linkage reported by reviewer.
- Limits / next verification: Historical configuration continuity unverified. Averaging losing perpetual positions creates downside exposure. No forward-profit guarantee.

## S51 , Passivbot reference vault

- Source: [Passivbot reference vault](https://app.hyperliquid.xyz/vaults/0x490af7d4a048a81db0f677517ed6373565b42349)
- Environment / grade: Venue live data / B+
- Provenance: R: reviewer queried documented API
- Finding: September 8 snapshot: all-time P&L +$3,641.45, equity $25,555.68; history begins September 3, 2025. Cumulative P&L +$1,509 January 21 to -$709 February 11 before recovery. Description claims standard unaltered template.
- Limits / next verification: Variable deposits: do not infer return from equity growth or P&L/equity. Leader commission 10%; all-fee/infrastructure reconciliation unresolved. Venue observation is not full independent audit.

- Later root verification: read-only vaultDetails retrieved 2026-09-08T20:48:49Z, name Passivbot Canon. allTime first point [1756938960105, 0.0], last [1788900529006, 3640.088311]; last equity 25554.318311; leaderCommission 0.1. Root independently rechecked venue endpoint. Difference from earlier snapshot is normal market movement, not a conflicting return. No follower-account data retained.

## S52 , Hyperliquid info endpoint

- Source: [Hyperliquid info endpoint](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/info-endpoint)
- Environment / grade: API documentation / no profit grade
- Provenance: R
- Finding: Reviewer used read-only vaultDetails for S51.
- Limits / next verification: File owner did not repeat API query; numerical provenance is reviewer callback. Raw response not archived in this record.

## S53 , Third-party Passivbot report

- Source: [Third-party Passivbot report](https://www.beaverknight.com/report/hlv-passivbot-canon-490af7)
- Environment / grade: Third-party claim / U
- Provenance: R
- Finding: Reported +13.2% with conflicting date window.
- Limits / next verification: Use venue P&L figures without inferring a percentage return; no reconciliation established.

## S54 , Carver system history

- Source: [Carver system history](https://qoppac.blogspot.com/2021/12/my-trading-system.html)
- Environment / grade: Author deployment history / B
- Provenance: D/R
- Finding: Production moved from private legacy engine to public pysystemtrade in 2020; optimization changed late 2021.
- Limits / next verification: Do not attribute the entire 2014-onward record to current public code. Author-linked reuse remains valid.

## S55 , Carver public configuration

- Source: [Carver public configuration](https://github.com/pst-group/pysystemtrade/blob/master/systems/provided/rob_system/config.yaml)
- Environment / grade: Configuration artifact / no extra profit grade
- Provenance: R
- Finding: Published rob_system configuration supplied by reviewer.
- Limits / next verification: Mutable branch/path; current default branch is develop. Do not equate this file with all historical deployments.

## S56 , Carver public runner

- Source: [Carver public runner](https://github.com/pst-group/pysystemtrade/blob/master/systems/provided/rob_system/run_system.py)
- Environment / grade: Runner artifact / no extra profit grade
- Provenance: R
- Finding: Published rob_system runner supplied by reviewer.
- Limits / next verification: Exact historical configuration not established; usefulness does not require exact match.

## S57 , Carver year 9

- Source: [Carver year 9](https://qoppac.blogspot.com/2023/05/trading-and-investing-performance-year.html)
- Environment / grade: Author historical return methods / B
- Provenance: R
- Finding: Older returns use notional capital.
- Limits / next verification: Historical measures differ; do not stitch an exact account-equity series from mixed reporting bases.

## S58 , Freqtrade repository

- Source: [Freqtrade repository](https://github.com/freqtrade/freqtrade)
- Environment / grade: Framework / no profit grade
- Provenance: D
- Finding: Repository and GPL-3.0 metadata checked.
- Limits / next verification: Framework does not inherit profitability from strategies using it.

## S59 , Hummingbot repository

- Source: [Hummingbot repository](https://github.com/hummingbot/hummingbot)
- Environment / grade: Framework / no profit grade
- Provenance: D
- Finding: Repository and Apache-2.0 metadata checked.
- Limits / next verification: Concrete strategy evidence separate in S46–S48.

## S60 , FinRL repository

- Source: [FinRL repository](https://github.com/AI4Finance-Foundation/FinRL)
- Environment / grade: Research framework / no profit grade
- Provenance: D
- Finding: Repository and MIT metadata checked.
- Limits / next verification: No audited live profit established by this review.

## S61 , pysystemtrade production

- Source: [pysystemtrade production](https://raw.githubusercontent.com/pst-group/pysystemtrade/master/docs/production.md)
- Environment / grade: Deployment documentation; no profit grade
- Provenance: D
- Finding / limits: Linux-oriented IB/MongoDB production, scheduled processes and futures-data/roll maintenance. Legacy version guidance requires current compatibility check.

## S62 , Freqtrade Docker quickstart

- Source: [Freqtrade Docker quickstart](https://www.freqtrade.io/en/stable/docker_quickstart/)
- Environment / grade: Deployment documentation; no profit grade
- Provenance: D
- Finding / limits: Documented Compose and dry-run path. Sample strategy is not a profitable default.

## S63 , Passivbot live requirements

- Source: [Passivbot live requirements](https://raw.githubusercontent.com/enarjord/passivbot/master/requirements-live.txt)
- Environment / grade: Deployment documentation; no profit grade
- Provenance: D
- Finding / limits: Direct dependency list includes Rust requirements, ccxt and numerical/data libraries; pin release before installation.

## S64 , Passivbot live Dockerfile

- Source: [Passivbot live Dockerfile](https://github.com/enarjord/passivbot/blob/master/Dockerfile_live)
- Environment / grade: Deployment documentation; no profit grade
- Provenance: D
- Finding / limits: Python 3.12 build/runtime stages; Rust compilation into wheel. Retrieved documentation is not a tested deployment.

## S65 , Passivbot backtesting documentation

- Source: [Backtesting docs](https://raw.githubusercontent.com/enarjord/passivbot/master/docs/backtesting.md)
- Environment / grade: Replay documentation; no profit grade
- Provenance: R, direct originating-task reading
- Finding / limits: One-minute candles; default data sources include Binance/Bybit. Hyperliquid history depends on available source; another venue's replay is not identical vault reproduction.

## S66 , Passivbot fake-live

- Source: [Passivbot fake-live](https://github.com/enarjord/passivbot/blob/master/docs/fake_live.md)
- Environment / grade: Operational documentation; no profit grade
- Provenance: D/R
- Finding / limits: Documented deterministic offline exchange runs normal Python/Rust loop, no network/credentials. Behavior test, not profit or authenticated paper validation.

## S67 , Legacy IB library

- Source: [Legacy IB library](https://github.com/erdewit/ib_insync)
- Environment / grade: Operational documentation; no profit grade
- Provenance: R
- Finding / limits: Archived dependency cited by older production material; current engine README refers to ib_async. Compatibility needs checking; no installation failure demonstrated.

## S68 , IB paper-account explanation

- Source: [IB paper-account explanation](https://www.interactivebrokers.com/campus/glossary-terms/paper-trading-account/)
- Environment / grade: Operational documentation; no profit grade
- Provenance: R
- Finding / limits: Paper execution differs from real fills. Generic limitation, not verification that a proposed adapter supports paper mode.

## S69 , Bybit restrictions

- Source: [Bybit restrictions](https://www.bybit.global/en/help-center/article/?id=000001085&language=en_US)
- Environment / grade: Eligibility or implementation evidence; no profit grade
- Provenance: R, originating task / independent public-doc review
- Finding / limits: Official U.S. exclusion reported by independent public-doc reviewer.

## S70 , Bitget terms

- Source: [Bitget terms](https://www.bitget.com/support/articles/360014944032-terms-of-use)
- Environment / grade: Eligibility or implementation evidence; no profit grade
- Provenance: R, originating task / independent public-doc review
- Finding / limits: Official U.S. restriction reported by reviewer.

## S71 , KuCoin terms

- Source: [KuCoin terms](https://www.kucoin.com/legal/terms-of-use)
- Environment / grade: Eligibility or implementation evidence; no profit grade
- Provenance: R, originating task / independent public-doc review
- Finding / limits: Official U.S. restriction reported by reviewer.

## S72 , Gate agreement

- Source: [Gate agreement](https://www.gate.com/legal/user-agreement)
- Environment / grade: Eligibility or implementation evidence; no profit grade
- Provenance: R, originating task / independent public-doc review
- Finding / limits: Official U.S. restriction reported by reviewer.

## S73 , OKX U.S. terms

- Source: [OKX U.S. terms](https://app.okx.com/en-us/help/terms-of-service-us)
- Environment / grade: Eligibility or implementation evidence; no profit grade
- Provenance: R, originating task / independent public-doc review
- Finding / limits: U.S. spot terms do not establish permitted perpetual access.

## S74 , Fidelity official support response

- Source: [Fidelity official support response](https://www.reddit.com/r/fidelityinvestments/comments/1td0i2u/fidelity_personal_api/)
- Environment / grade: Eligibility or implementation evidence; no profit grade
- Provenance: R, originating task / independent public-doc review
- Finding / limits: Official support response states no public API; not evidence of supported retail autonomous trading access.

## S75 , Fidelity institutional integration

- Source: [Fidelity institutional integration](https://clearingcustody.fidelity.com/app/item/RD_9883092/integration-xchange.html)
- Environment / grade: Eligibility or implementation evidence; no profit grade
- Provenance: R, originating task / independent public-doc review
- Finding / limits: Institutional integration is not retail API entitlement.

## S76 , Alpaca paper documentation

- Source: [Alpaca paper documentation](https://docs.alpaca.markets/us/docs/paper-trading)
- Environment / grade: Eligibility or implementation evidence; no profit grade
- Provenance: R, originating task / independent public-doc review
- Finding / limits: Paper-only API infrastructure without funded brokerage is a possible separate path; no account opened and no profitable strategy implied.

## S77 , Alpaca fractional minimum

- Source: [Alpaca fractional minimum](https://alpaca.markets/support/can-we-submit-orders-smaller-than-1-usd-in-notional-value)
- Environment / grade: Eligibility or implementation evidence; no profit grade
- Provenance: R, originating task / independent public-doc review
- Finding / limits: Reported $1 fractional notional minimum; does not establish a validated profitable stock strategy or complete eligibility.

## S78 , IB paper API limitations

- Source: [IB paper API limitations](https://www.interactivebrokers.com/docs/tws-api/doc/notes-limitations/limitations/paper-trading)
- Environment / grade: Eligibility or implementation evidence; no profit grade
- Provenance: R, originating task / independent public-doc review
- Finding / limits: Approved/funded setup described by reviewer; capital needs and suitable instrument granularity unresolved.

## S79 , Issuer prospectus on SEC EDGAR

- Source: [Issuer prospectus on SEC EDGAR](https://www.sec.gov/Archives/edgar/data/2088139/000121390026056692/ea0290714-424b3_bitwise.htm)
- Environment / grade: Eligibility or implementation evidence; no profit grade
- Provenance: R, originating task / independent public-doc review
- Finding / limits: Issuer states Hyperliquid interface terms exclude U.S. residents. Not SEC legal advice or a universal legal conclusion about protocol interactions.

## S80 , HSL episode documentation

- Source: [HSL episode documentation](https://github.com/enarjord/passivbot/blob/master/docs/equity_hard_stop_loss.md)
- Environment / grade: Eligibility or implementation evidence; no profit grade
- Provenance: D
- Finding / limits: Direct lookup supports flatten/reset contracts. Local diagnosis showed saved stop metrics used stale fills; generic episode reset alone did not explain the defect.

## S81 , Upstream tied-fill history

- Source: [Upstream tied-fill history](https://github.com/enarjord/passivbot/commit/890908b86fc22243353fb9b80737f66cb8747a40)
- Environment / grade: Eligibility or implementation evidence; no profit grade
- Provenance: D
- Finding / limits: Direct GitHub API history check: September 5 tied-fill evidence change touched fixtures. No maintainer explanation for this exact stale-finalization defect found; local code/evidence establishes cause.

## Fields still required for any shortlisted system

Continuous marked-to-market equity; dated deposits and withdrawals; complete fees, spreads, slippage, funding/borrow costs and model/data/hosting expenses; same-period passive and cash comparator; leverage, concentration, turnover, liquidity and capacity; maximum drawdown and recovery; execution failures; frozen code/model/parameters; point-in-time data and universe; independent reproduction and forward persistence. Missing fields are unknown, not zero. Tax effects should be reported separately under the eventual jurisdiction.

## Correction log

- TradingAgents retrieval/version discrepancy: originating task saw a Reproducibility warning, file owner did not. File-owner snapshot announces point-in-time fixes and retains research/simulation framing. Neither snapshot is a code audit; preserve both observations.
- Mr Scrooge practice headline is separated from the dated live-labeled CSV endpoint calculation.
- Initial report was not treated as complete before the later positive-live and conventional-strategy packets arrived.

- 2026-09-08 16:46 EDT: Expanded code reuse scope: exact deployment match is not an inclusion gate. Added positive Carver multiyear lead and earlier profitable Prediction Arena run; separated rewards and third-party cited returns. Focused audit continues.

- 2026-09-08 16:48 EDT: Focused reuse review completed. Added venue-backed Passivbot P&L and Carver deployment history. No percentage return inferred from variable-deposit vault balances. No strategy selected.


## Integration-readiness sources, September 8

### S82 , IBKR individual accounts
- Source: https://www.interactivebrokers.com/en/accounts/individual.php
- Verification: direct primary-source web/source check this phase.
- Finding / limits: U.S. individual futures offering; individual approval remains unknown.

### S83 , IBKR API plan requirement
- Source: https://www.interactivebrokers.com/docs/third-party-integrations/general-third-party-frequently-asked-questions
- Verification: direct primary-source web/source check this phase.
- Finding / limits: Pro required for API support.

### S84 , IBKR U.S. futures margin
- Source: https://www.interactivebrokers.com/en/trading/margin-futures-fops.php?ex=us&hm=us&ot=0&pm=0&rgt=0&rsk=1&rst=1
- Verification: direct primary-source web/source check this phase.
- Finding / limits: MES long overnight initial 3358.65 USD and maintenance 2603.70 observed; variable, not capital recommendation.

### S85 , IBKR market-data pricing
- Source: https://www.interactivebrokers.com/en/pricing/market-data-pricing.php
- Verification: direct primary-source web/source check this phase.
- Finding / limits: Standard individual paid-data equity threshold 500 USD plus costs; not total trading capital.

### S86 , IBKR socket setup
- Source: https://www.interactivebrokers.com/campus/trading-lessons/installing-configuring-tws-for-the-api/?retakeFinal=1
- Verification: direct primary-source web/source check this phase.
- Finding / limits: Paper Gateway 4002/TWS 7497; read-only blocks orders.

### S87 , IBKR error codes
- Source: https://www.interactivebrokers.com/docs/tws-api/doc/error-handling/error-codes
- Verification: direct primary-source web/source check this phase.
- Finding / limits: 50 messages per second error boundary; not empirically probed.

### S88 , CME MES specifications
- Source: https://www.cmegroup.com/markets/equities/sp/micro-e-mini-sandp-500.contractSpecs.html
- Verification: direct primary-source web/source check this phase.
- Finding / limits: Multiplier 5 USD, tick 0.25 index point/1.25 USD.

### S89 , Alpaca account plans
- Source: https://docs.alpaca.markets/us/docs/account-plans
- Verification: direct primary-source web/source check this phase.
- Finding / limits: Paper user may onboard into live brokerage; strategy not supplied.

### S90 , Alpaca domestic funding
- Source: https://alpaca.markets/support/how-can-a-domestic-user-us-tax-resident-fund-their-account
- Verification: direct primary-source web/source check this phase.
- Finding / limits: U.S. ACH funding route.

### S91 , Alpaca application requirements
- Source: https://alpaca.markets/support/requirements-alpaca-brokerage-account
- Verification: direct primary-source web/source check this phase.
- Finding / limits: U.S. account requirements, not personal approval.

### S92 , Alpaca domestic schema
- Source: https://docs.alpaca.markets/us/docs/domestic-usa-accounts
- Verification: direct primary-source web/source check this phase.
- Finding / limits: Maryland listed; schema is not individual suitability approval.

### S93 , Statsmodels SciPy issue
- Source: https://github.com/statsmodels/statsmodels/issues/9542
- Verification: direct primary-source web/source check this phase.
- Finding / limits: Primary upstream issue corroborates local _lazywhere import failure.

### S94 , Pinned pysystemtrade source
- Source: https://github.com/pst-group/pysystemtrade/tree/b4a25e6e1e33a54a3ecfb45c0f6db5e2b60b84f8
- Verification: direct primary-source web/source check this phase.
- Finding / limits: Native ib_async adapter/MES mapping; local compatibility evidence in readiness report.

### S95 , Individual account minimums
- Source: https://www.interactivebrokers.com/en/accounts/required-minimums.php
- Verification: direct official documentation, September 8.
- Finding / limits: Individual Pro/Lite minimum and inactivity fee both zero; separate from data and margin.

### S96 , Current Client Portal paper instructions
- Source: https://www.ibkrguides.com/clientportal/papertradingaccount.htm
- Verification: direct official documentation, September 8.
- Finding / limits: New clients automatically receive paper account; normal creation 24 hours. Differs in framing from funded prerequisite in TWS API docs; actual access unverified.

### S97 , Application requirements
- Source: https://www.interactivebrokers.com/en/general/what-you-need-inv.php
- Verification: direct official documentation, September 8.
- Finding / limits: Personal declarations and verification documents; not filled or submitted.

### S98 , Official Gateway distributions
- Source: https://www.interactivebrokers.com/en/trading/ibgateway-latest.php?menu=B
- Verification: direct official documentation, September 8.
- Finding / limits: Apple Silicon stable/latest choices verified on official page; no binary download/installation or signature verification yet.

### S99 , IBKR account-type comparison
- Source: https://www.interactivebrokers.com/en/accounts/configuring-your-account.php
- Verification: direct official page, September 8.
- Finding / limits: Futures explicitly described for Cash and Margin, variation collateral and liquidation requirements. Standard Margin is a flexibility recommendation, not a strict futures prerequisite. Legacy formHelp also read but stale T+3 settlement language was not adopted.


### S100 , Alternate broker primary-source comparison (2026-09-08 18:36 EDT)
Sources (official pages checked today unless repository author):
- [Tradovate retail API access](https://tradovate.zendesk.com/hc/en-us/articles/4403105829523-How-Do-I-Get-Access-to-the-Tradovate-API), [API environments](https://api.tradovate.com/), [NinjaTrader getting started](https://docs.ninjatrader.com/api/getting-started), [pricing](https://www.tradovate.com/pricing/), [linked all-in schedule](https://www.tradovate.com/TradovateAllInRates120625.pdf).
- [TradeStation API onboarding](https://www.tradestation.com/platforms-and-tools/trading-api/), [retail API FAQ](https://api.tradestation.com/docs/faq/), [SIM limitations](https://api.tradestation.com/docs/fundamentals/sim-vs-live/), [pricing](https://www.tradestation.com/pricing/), [account/data fee FAQ](https://www.tradestation.com/faqs/).
- [tastytrade API](https://tastytrade.com/api/), [sandbox limitations](https://developer.tastytrade.com/docs/sandbox/), [funded market data](https://developer.tastytrade.com/docs/concepts/market-data/), [permissions](https://tastytrade.com/learn/accounts/account-resources/trading-permissions/), [margin distinction](https://tastytrade.com/learn/accounts/account-resources/margin-vs-cash-accounts/), [fee schedule April6,2026](https://assets.contentstack.io/v3/assets/blt7dc2e3d4a7071563/blt2b752fef372188fe/commissions-and-fees).
- [tastytrade repositories](https://github.com/tastytrade), [unofficial Python SDK](https://github.com/tastyware/tastytrade), [Tradovate examples](https://github.com/tradovate/example-api-js), [pysystemtrade broker guide](https://github.com/pst-group/pysystemtrade/blob/develop/docs/IB.md).
- [Alpaca paper](https://docs.alpaca.markets/us/docs/paper-trading), [data plans](https://docs.alpaca.markets/us/docs/about-market-data-api), [retail API fees](https://alpaca.markets/learn/start-paper-trading).

Verification: official pages and native repository inspected; TradeStation onboarding body read through BrowserClaw after web fetch405. API minimum is$10,000 on actual page, FAQ less specific. No new broker account eligibility or API calls tested. Pricing/add-on/data ambiguities explicitly retained.
