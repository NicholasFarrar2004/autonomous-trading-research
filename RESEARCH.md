> Historical research snapshot from September 8, 2026. Sources and prices can change. Later implementation results are documented in README.md. Private coordination and personal constraints are omitted.

# Autonomous personal trading: initial due diligence

Status: **Initial bounded review complete; conclusions provisional. No system selected or implementation approved.**
Updated: 2026-09-08 17:05 EDT

## Finding

Credible public evidence shows that some automated systems have made money. This review did **not establish a ready-to-run open strategy with independently verified, repeatable net profitability suitable for the project operator’s deployment**. That is a bounded finding about the sources reviewed, not proof that no qualifying system exists.

For reusable code, **Carver's pysystemtrade and Passivbot lead the shortlist**: the former has positive multiyear author reporting; the latter has positive venue-reported cumulative P&L linked to a public strategy. PlainTape remains a further-diligence lead. These are useful foundations despite unresolved exact deployment matching. The [reusable-code catalog](CODE_CATALOG.md) separates engineering usefulness, profit evidence and practical fit.

The earlier slow unlevered ETF experiment remains an unselected simplicity benchmark, not a requirement that excludes other reusable projects. No independently audited dependable-profit setup was established, and no market or build was selected.

## Research scope

Review of reusable systems across public markets, distinguishing operator claims, independent evidence and engineering usefulness. This is a dated research record; current implementation status is in README.md.

## Method and evidence standard

The originating research reviewed primary repositories, papers, operator records, and account-linked evidence, looking for both positive and negative outcomes. This file owner directly checked selected key sources and integrated the remaining findings with explicit provenance. The [source ledger](SOURCE_LEDGER.md) contains 81 references, exact URLs, environments, grades, caveats, and verification status.

- Keep live money, forward paper simulation, historical out-of-sample tests, and in-sample backtests separate.
- Prefer total marked-to-market equity adjusted for cash flows. Realized P&L alone can hide losing open positions; deposits are not investment return.
- Include trading and operating costs, exposure, drawdown, recovery, liquidity, and a fair same-period benchmark. Report taxes separately.
- Require point-in-time data, a frozen specification, selection-bias controls, independent reproduction, and forward persistence before describing repeatability.
- Distinguish source publication, operator attribution, independently checked records, and independently reproducible strategies. A third-party dashboard is not automatically an audit.

Grades: A means audited/reconciled live results plus reproducible implementation; none qualified. B+ is transaction-grounded reconstruction, B primary live reports, B- partial live/account claims, C model/backtest evidence, and U unresolved. Grades measure evidence quality, not attractiveness or future return.

## Candidate comparison

| Candidate | Environment / grade | What it establishes | Principal gap / v1 implication |
|---|---|---|---|
| Academic arbitrage bots | Live / B | Short reported positive deployments | No public strategy repo or complete cost/denominator reconciliation; research lead |
| APOLLO MEV study | On-chain reconstruction / B+ | Automated profit exists in sampled activity | Analysis tool, much logic off-chain; aggregate is not entrant profitability |
| Passivbot | Venue live data / B+ | Positive cumulative P&L linked to public strategy | Variable deposits, averaging losses, config changes; high reuse-diligence priority |
| PlainTape / public pysystemtrade fork | Operator live / B | Positive dated NAV claim and verified public fork | Prioritized diligence lead; restatements, missing early data, deployed-code linkage unresolved |
| TTS | Live account-linked claim / B- | Large displayed gain and substantial drawdown | Private history, proprietary strategy, unresolved badges/linkage |
| Haystack | Operator live claim / B- | Short positive marked portfolio window | No independent account audit; zero sells does not mean zero economic profit |
| Mr Scrooge | Operator live-labeled log / B- | Negative NAV change in checked period | Practice headline differs from live log |
| Prediction Arena | Author-reported live / B | Earlier positive 23-day run; all six lost in later main window | Period dependence; no blanket conclusion about all agents |
| TradingAgents / AI Hedge Fund | Research tooling | Existing accessible frameworks | Framework capability is not edge; no deployment case established |
| Freqtrade / NostalgiaForInfinity | Tooling / backtest C | Existing dry-run and strategy ecosystem | Independent live equity record unresolved |
| pysystemtrade | Infrastructure plus operator live B | Positive multiyear author record, including losses | Strong reusable-code lead; not independently audited |
| Slow ETF trend | Historical/model C | Simple falsifiable candidate, mixed literature | No dependable-profit claim; fair passive comparison essential |
| Crypto carry / option selling / AMM | Historical/model C | Economic mechanisms and documented risks | Financing, tail or execution complexity; not recommended initial build |

## Positive live evidence, with limits

Passivbot's referenced vault showed cumulative P&L +$3,641.45 and equity $25,555.68 in the reviewer's September 8 venue-API snapshot, with history beginning September 3, 2025. P&L fell from +$1,509 to -$709 during a losing interval before recovery. Deposits varied, so neither equity growth nor P&L/equity is a valid inferred return. [Vault](https://app.hyperliquid.xyz/vaults/0x490af7d4a048a81db0f677517ed6373565b42349). Its public [strategy code](https://github.com/enarjord/passivbot) is a useful lead; version continuity and all-in costs remain unresolved.


PlainTape remains a positive open-foundation lead for further diligence. Its August 17, 2026 snapshot reports +38.1% since November 2025, +41.3% YTD, Sharpe 1.67 and -8.4% maximum drawdown. These are operator claims, not an independent audit. The author publicly discloses restatements and three opening deposit days still assigned zero return. [Dashboard](https://plaintape.fund/).

Methodology excludes earlier live history because of gaps and describes a complex futures program rather than a simple ETF rule. The reported $500,000 sizing notional is distinct from actual account capital. The current full ledger, cost treatment and exact deployed code need reconciliation. [Methodology](https://plaintape.fund/methodology/). The originating task traced the operator to a public fork; existence is verified, exact account-to-code linkage is not. [About](https://plaintape.fund/about/), [fork](https://github.com/garcia42/pysystemtrade). An August 17 health snapshot showed FAIL; that is dated operational evidence, not today's status. [Status](https://plaintape.fund/slo/).


Schwertfeger and Vogt report four live arbitrage bots and aggregate realized profit of $20,237.48. Three reported returns were 24.91%, 33.35%, and 17.39% during November 27–December 31, 2023; another was 6.15% during September 12–October 8, 2024. These are short windows, not annual returns. Full costs, capital denominators, and a public strategy implementation remain unresolved. The file owner's journal/preprint fetches failed; this detail is retained from the originating team's abstract-level primary reading, not a full-paper cost audit. An accessible university page corroborates publication and realized-trading research. [University research page](https://emwifo.ovgu.de/emwifo/en/Research.html). [Journal paper](https://www.sciencedirect.com/science/article/pii/S0378426626000956), [author preprint](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5055292).

APOLLO reconstructs activity from 2,052 bots and 2,516,236 transactions, reporting approximately $40m profit. The review period is January 2023–December 2024, with transaction fees deducted according to the originating review. Most sampled bots, 75.3%, depend on off-chain logic. These facts support automated profit in the sample, not a new entrant's expected return or all-in business profit. The sample includes sandwich activity alongside arbitrage/liquidation; the released repository is an analysis tool. [NDSS paper](https://www.ndss-symposium.org/wp-content/uploads/2026-s506-paper.pdf), [code](https://github.com/sec-study-dev/apollo).

The TTS Myfxbook snapshot showed +482.50%, EUR5,000 deposits, EUR29,115.59 equity, 875 trades, and 40.66% drawdown, with EUR2,560.86 commissions. Private individual history, unestablished badge verification, operator-only automation linkage, and affiliate incentives prevent calling it audited or reproducible. The supplied snapshot lacks a full start/end period, so it cannot be fairly ranked against other returns. [Account](https://www.myfxbook.com/members/TradingShelter/tts-bot/11932605), [operator](https://ttsautomation.com/).

Haystack's July 9–September 1 snapshot reports $4,803.66 contributed capital and $5,225.64 marked holdings, +8.78%, with 36 holdings and no sells. Its cash-flow-matched SPY comparator was $4,855.10. This is a short operator-reported window, not realized profit or an independent audit. A later search snapshot of +11.62% is a different date and is not substituted here. [Haystack](https://sbrn.io/projecthaystack/).

## LLM-agent evidence and misleading comparisons

Prediction Arena reports six live Kalshi models losing 16.0%–30.8% in its main 57-day window. Appendix B.2 also reports an earlier 23-day real-capital run: +10.9% ($1,090.32), 112 trades, 4.1% drawdown. The same model later lost in the main period. Both belong in the evidence; neither should be cherry-picked. The three-day paper cohort is separate. [Prediction Arena](https://arxiv.org/html/2604.07355v1).

Mr Scrooge illustrates why environment and equity matter. Its repository advertises a +10.54% practice result, while the directly checked live-labeled operator CSV starts at NAV 2,500 on July 29 and ends at 1,878.56 on September 8 at 20:15:02 UTC, with terminal net deposits zero. The calculated endpoint change is **-24.86%**, conditional on the cash-flow record being complete and accurate. Neither record is a brokerage audit. [Repository](https://github.com/BrockStar3540/mr-scrooge-v6), [CSV](https://raw.githubusercontent.com/BrockStar3540/mr-scrooge-v6/main/livelog/equity.csv).

TradingAgents currently describes research and simulated execution; its August update announces point-in-time fixes. The originating task retrieved a Reproducibility section warning about current news/social inputs, while this file owner retrieved a version without that section. This retrieval/version discrepancy remains unresolved; neither snapshot substitutes for an actual historical-input audit. The paper uses a narrow historical 2024 simulation. AI Hedge Fund describes educational use and no actual trades. These projects remain tooling candidates, not live-profit evidence. [TradingAgents](https://github.com/TauricResearch/TradingAgents), [paper](https://arxiv.org/html/2412.20138v7), [AI Hedge Fund](https://github.com/virattt/ai-hedge-fund).

FINSABER's broader historical assessment challenges earlier LLM advantages. Its commission assumption is explicit, $0.0049/share with $0.99/order minimum, but is not a current quote or a complete cost model. StockBench simulates opening-price fills for 20 Dow constituents in March–June 2025. AMA's positive short record has unresolved real-funding status; AI-Trader remains benchmark evidence. A survey's methodological counts concern a 19-study extraction subset of 77 included studies, not the entire field. [FINSABER](https://arxiv.org/html/2505.07078v4), [StockBench](https://arxiv.org/html/2510.02209v1), [AMA](https://arxiv.org/html/2510.11695v1), [AI-Trader](https://arxiv.org/html/2512.10971v1), [survey](https://arxiv.org/html/2605.19337v1).

An apparent TradingAgents replication needs reconciliation: Q1 2024 is labeled 305 trading days and LLM/MACD metrics are identical. That is an internal consistency concern, not evidence of fraud. Nof1 corporate result claims are interested-party evidence with wallet verification unresolved; a similarly named repository explicitly uses simulated examples and has unverified affiliation. [Replication](https://github.com/lucas020695/tradingagents_replicated), [investor release](https://www.nasdaq.com/press-release/sui-group-co-leads-15-million-funding-round-ai-trading-lab-nof1-makes-strategic), [unverified repository](https://github.com/alphaarenanof1ai/nof1ai-alpha-arena).

## Traditional strategies: why simple is testable, not proven

Trend has long historical support in AQR research and post-publication model evidence in Faber. Contrary studies find that volatility scaling explains much of apparent momentum performance, individual-asset predictability is weak, or large technical-rule searches fail after statistical corrections. This makes an identical passive basket and matched exposure essential. Institutional futures results do not automatically transfer to a small ETF account. [AQR](https://www.aqr.com/-/media/AQR/Documents/Insights/Journal-Article/AQR-JPM-Fall-2017.pdf), [Faber](https://papers.ssrn.com/sol3/Papers.cfm?abstract_id=962461), [Kim/Tse/Wald](https://www.sciencedirect.com/science/article/pii/S1386418116301379), [Huang et al.](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3165284), [Yang et al.](https://www.sciencedirect.com/science/article/abs/pii/S0927538X18300775).

pysystemtrade is now a strong reusable-code lead: Carver's next annual report records +23.7% net futures return for April 6, 2025–April 5, 2026, following the -16.3% year. He reports long-run mean 13.8%, volatility 17.3% and zero-risk-free Sharpe 0.80. His 13.0% CAGR uses monthly volatility-adjusted figures, not unqualified account CAGR. The account remained below its April 2024 high. This is positive multiyear author evidence, not an independent audit. [2026 report](https://qoppac.blogspot.com/2026/04/annual-performance-update-year-12.html), [2025 report](https://qoppac.blogspot.com/2025/04/annual-performance-update-returneth.html), [public engine](https://github.com/pst-group/pysystemtrade).

Hummingbot's September 2023 two-day competition reported two positive eligible entries, with a runner adapting published strategy code. This provides a narrow code-linked lead; submitted CSVs and two days do not establish repeatability. Liquidity-mining rewards must remain separate from trading P&L. [Competition](https://hummingbot.org/blog/-beta-bot-battle-results-and-roundup/), [miner interview](https://hummingbot.org/blog/interview-with-liquidity-miner-dominator008/). [openthomas](https://github.com/PredictionMarketTrader/openthomas) offers reusable prediction-market architecture; its cited +10.9% belongs to another project, not its own track record.

Crypto basis extremes are not net carry yields. Option-index returns are hypothetical, and option selling bears short-volatility losses. AMM fee income must be compared with arbitrage losses and the relevant benchmark, not treated as free yield. These approaches add financing, margin, execution, or tail-risk problems before the project operator has set a loss budget. Detailed figures and scope limits are retained in S33–S37. [BIS carry](https://www.bis.org/publ/work1087.pdf), [put-write study](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3393940), [option-selling study](https://faculty.providence.edu/en/publications/35-year-performance-analysis-of-cboe-sampp-500-option-selling-ind-2/), [AMM study](https://arxiv.org/html/2404.05803v1), [mechanism](https://arxiv.org/abs/2208.06046).

## Recommendation for the next discussion

Inspect reusable components from pysystemtrade first, with Passivbot as a separate code-and-live-evidence candidate. Exact historical deployment matching is not a gate to useful reuse. Compare practical requirements with a simple unlevered ETF baseline once the project operator supplies constraints; do not assume the more complex strategy is preferable because it has public profits. Freeze any proposed experiment and cost/drawdown criteria before evaluating outcomes. No implementation is selected by this ranking.

Before any implementation PRD, resolve:

- Capital explicitly available for an experiment and maximum acceptable dollar/percentage loss.
- Time horizon, objective versus passive investing, and acceptable drawdown/recovery time.
- Jurisdiction, eligible accounts/venues/instruments, and tax constraints.
- Available supervision and what should happen when data, orders, or account reconciliation fail.
- Whether the first approved phase is research simulation only, and what evidence would justify any later live phase.

## Coverage and remaining verification

Covered: public LLM frameworks and benchmarks; positive and negative live claims; arbitrage/MEV; systematic trend; crypto carry; option selling; AMM economics. This was a bounded public-source review, not an exhaustive commercial manager database search, account audit, code audit, or strategy reproduction. No current broker pricing, tax advice, venue eligibility, or investable opportunity was verified. Mutable repositories and account snapshots need refreshing before reliance. Key remaining checks are public exact strategy linkage, continuous equity and cash-flow reconciliation, all-in costs, independent reproduction, regime persistence, and user-specific constraints.

## Record history

2026-09-08 16:39 EDT: Integrated the initial scope and subsequent research packets, including PlainTape and source-retrieval corrections. Selected direct source checks and the TradingAgents wording correction are documented in the ledger. Initial review recorded; no trading system built or selected.

2026-09-08 16:48 EDT: Focused code review added Carver and Passivbot as leading reuse candidates, eight catalog groups and 60 source entries. Earlier initial findings retained with explicit corrections and current scope.

## Deployment planning extension

The [draft PRD](PRD.md) proposes copying one existing Passivbot route first, with no requirement to combine systems. Passivbot has the lower deployment burden of the two leading code-linked candidates; a generic Freqtrade dry-run is simpler still. Neither technical ease nor this draft selects a suitable market or authorizes implementation. Detailed dependency comparison is in the [catalog](CODE_CATALOG.md).

Independent review completed: first proposed experiment after PRD sign-off is the existing Passivbot offline fake-live scenario, then scripted failure/recovery checks. This requires no account or credentials and tests behavior rather than profit. Historical return reproduction and eventual venue/capital suitability remain unresolved.

## Later implementation

The initial research led to an offline Passivbot experiment, followed by a native IBKR paper integration. See [offline validation](OFFLINE_VALIDATION.md) and [current results](RESULTS.md). Broker alternatives remain historical feasibility research, not selected replacements or capital recommendations.
