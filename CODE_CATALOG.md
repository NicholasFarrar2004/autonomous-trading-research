> Historical research snapshot from September 8, 2026. Sources and prices can change. Later implementation results are documented in README.md. Private coordination and personal constraints are omitted.

# Autonomous trading: reusable code catalog

Status: **Focused reusable-code review complete; conclusions provisional. No implementation selected or approved.**
Updated: 2026-09-08 17:05 EDT

Companions: [research report](RESEARCH.md), [source ledger](SOURCE_LEDGER.md).

## Inclusion rule

the project operator wants published code related to profitable projects that can be reused and improved. Exact deployed source or configuration is **not required for inclusion**. Evaluate reusable engineering and return evidence separately. Code-results linkage is labeled exact, author-linked, related, or inferred; none implies independent verification. A private configuration is an evidence limitation, not a reason to discard a useful public foundation.

Priority means priority for research/reuse assessment, not an instruction to trade. Existing source ledger grades and dated performance qualifications remain applicable. **Highlighted: pysystemtrade is an openly published engine with positive multiyear author-reported performance.** Its losing years and measurement qualifications remain visible; independent auditing is not established.

## Reuse shortlist

| Project / repository | License | Artifact type | Code-results relationship | Research priority |
|---|---|---|---|---|
| [pysystemtrade](https://github.com/pst-group/pysystemtrade) | GPL-3.0 | Automated futures framework with implemented systems | Author-linked live reporting; exact configuration unnecessary for usefulness | Highest: inspect multiyear record and reusable components |
| [Passivbot](https://github.com/enarjord/passivbot) | Unlicense | Full perpetual-futures strategy and shared execution/backtest engine | Official reference vault; venue describes template use, history continuity unresolved | Second: concrete open-code/live-data lead |
| [PlainTape fork](https://github.com/garcia42/pysystemtrade) | Fork license not reverified; upstream GPL-3.0 | Operator-linked fork | Author-linked, according to originating task; direct retrieval discrepancy | High: positive lead, resolve access |
| [Freqtrade](https://github.com/freqtrade/freqtrade) + [NostalgiaForInfinity](https://github.com/iterativv/NostalgiaForInfinity) | Both GPL-3.0 | Execution/backtest framework plus strategy code | Related infrastructure; NFI published strategy, live return linkage unresolved | High for reusable crypto workflow, conditional on evidence |
| [Hummingbot](https://github.com/hummingbot/hummingbot) | Apache-2.0 | Crypto execution/strategy framework | Published adaptation linked to brief positive competition result | Medium: assess concrete strategy modules |
| [openthomas](https://github.com/PredictionMarketTrader/openthomas) | MIT | Weather/prediction-market agent architecture | Related to another project's positive run; own profitability unproven | Medium for bounded-agent architecture |
| [FinRL](https://github.com/AI4Finance-Foundation/FinRL) | MIT | Reinforcement-learning research framework | Research-linked, no verified live-profit linkage | Lower: research components |
| [TradingAgents](https://github.com/TauricResearch/TradingAgents) | Apache-2.0 | LLM research framework | Paper-linked historical results | Lower: evaluation/agent components |

Upstream license labels were checked on repository pages or API metadata on September 8, 2026; fork-specific licensing remains unresolved. They identify the repository license; dependencies and reused file notices require checking if implementation is later approved. No repositories were installed or executed during this initial research phase.

## Candidate notes

### pysystemtrade

- Evidence: positive multiyear author record and a positive latest futures year after a loss; exact figures and volatility-adjusted CAGR qualification are in S45. This is the strongest current reuse lead, not an independently audited promise.
- Reuse: backtesting, sizing, execution and production organization. Published [configuration](https://github.com/pst-group/pysystemtrade/blob/master/systems/provided/rob_system/config.yaml) and [runner](https://github.com/pst-group/pysystemtrade/blob/master/systems/provided/rob_system/run_system.py) provide starting artifacts; exact deployed matching is unnecessary for inclusion.
- Fit: more operationally involved than an unlevered ETF test; capital and futures eligibility unresolved. Components may be useful without reproducing the entire system.
- Gaps: independent reconciliation and comparable return bases. Public production began in 2020 after private legacy code; late-2021 optimization changed. Older reports use notional capital. Do not attribute all history to current code or stitch mixed measures into an exact account series (S54–S57).

### Passivbot

- Evidence: positive cumulative P&L in reviewer-retrieved venue data spanning roughly a year; losing interval retained in S51. Changing deposits prevent a percentage-return inference. Not a multiyear record.
- Reuse: full strategy code and shared live/backtest planner. [Repository](https://github.com/enarjord/passivbot); [reference vault](https://app.hyperliquid.xyz/vaults/0x490af7d4a048a81db0f677517ed6373565b42349).
- Fit: derivatives and averaging losing positions require capital and drawdown constraints; not selected for deployment.
- Gaps: fee reconciliation, history/config continuity and downside behavior. Current v8 differs from v7; a positive historical vault does not validate the new default.

### PlainTape

- Evidence: dated positive operator record; detailed numbers and return restatements remain in S38–S41. Not an account audit.
- Reuse: operator engineering and upstream systematic framework. Originating task traced the About page to the public fork.
- Fit: many futures instruments and substantial operational complexity; actual equity differs from sizing notional.
- Gaps: this file owner now gets web failure and GitHub API 404 for the fork. That conflicts with the earlier observation and does not prove removal. Fork-specific license/current accessibility and usable public changes need confirmation. Exact deployed match is not an inclusion gate.

### Freqtrade + NostalgiaForInfinity

- Evidence: strategy/backtest references, independent live record not yet established (S04–S06). Do not confuse a community strategy's backtest with framework profitability.
- Reuse: existing strategy implementation, dry-run, backtest and bias-detection workflow.
- Fit: promising existing-tools path if crypto is selected; costs, venue availability, liquidity and supervision remain unresolved.
- Gaps: comparable multiyear net-equity record, current strategy revision, pair universe, failed runs and open-position losses.

### Hummingbot

- Evidence: S46–S48 now identify brief positive participant outcomes and rewards-driven activity. The runner used a published strategy adaptation; no durable net trading record established.
- Reuse: inspect market_making_dman_v2 adaptation and [related analytics](https://gist.github.com/fengtality/8970b8ce67bc84dc5047ab729922d44d). Analytics are not the entire winning bot.
- Fit: multiple venues and inventory/execution exposure can defeat apparent spread profits; requirements depend on the strategy and remain to be assessed.
- Gaps: specific published module, period, costs and live result linkage. Do not transfer academic arbitrage profits to this framework without evidence.

### FinRL

- Evidence: public research framework; no independently verified profitable deployment established here.
- Reuse: research environments, agent experimentation and evaluation, subject to point-in-time and realistic cost checks.
- Fit: learning/training adds complexity before an edge is demonstrated; lower initial priority.
- Gaps: concrete result-to-code specification, reproducibility and forward testing.

### TradingAgents

- Evidence: historical simulation and research framing (S01–S02), not proven live returns.
- Reuse: financial-agent decomposition and evaluation patterns, if their benefit exceeds model/data costs.
- Fit: lower-priority source of components for a simple v1; agent sophistication does not establish profit.
- Gaps: retrieval/version discrepancy in README warnings remains recorded in source ledger; historical inputs need an actual audit.

### openthomas

- Evidence: paper/replay architecture; its README cites another project's profitable run, not its own. See S49.
- Reuse: weather baseline, bounded model changes, calibration and deterministic risk controls; MIT license identified on repository page.
- Fit: narrower than a general financial agent, but requires data-quality and venue analysis.
- Gaps: its replay variants do not establish profitable live execution. Useful related code remains eligible.

## Deployment burden, separate from profitability

**Passivbot is easier technically than pysystemtrade/PlainTape among the two leading code-and-live-evidence candidates.** Freqtrade is the simpler generic dry-run starter, but that is a different claim from evidence-linked profitable deployment. Technical ease does not resolve the project operator’s eligibility, capital or risk fit.

| System | Dependencies and maintenance | Test mode / capital fit |
|---|---|---|
| Passivbot | Python/Rust or supplied live container; venue API, config and persistent data; monitor connections, fills and version changes | Offline deterministic fake-live exists; authenticated paper/sandbox support must be verified. Perpetual minimums and margin need venue-specific review |
| pysystemtrade / PlainTape | Python, IB gateway/TWS, MongoDB and scheduled data/order/report processes; futures histories and rolls, backups and session maintenance | Backtesting available; broker paper integration needs testing. Contract granularity, data subscriptions and margin may constrain small accounts |
| Freqtrade baseline | Documented Docker Compose setup with persistent user data/config; venue feed and strategy management | Explicit dry-run path; sample strategy is educational, not profit evidence |

Sources: [Passivbot runtime](https://raw.githubusercontent.com/enarjord/passivbot/master/requirements-live.txt), [container](https://github.com/enarjord/passivbot/blob/master/Dockerfile_live), [pysystemtrade production](https://raw.githubusercontent.com/pst-group/pysystemtrade/master/docs/production.md), [Freqtrade quickstart](https://www.freqtrade.io/en/stable/docker_quickstart/). Production docs include legacy dependency guidance; compatibility must be checked against a pinned release, not blindly copied. No US or other regional venue eligibility is assumed.

Proposed singular architecture and approval gates: [draft PRD](PRD.md).

## Priority and next decision

1. **pysystemtrade / Carver:** strongest author-linked multiyear positive record with public reusable implementation. Start here for transferable system design and components.
2. **Passivbot:** strongest additional concrete open-strategy/venue-data lead; positive cumulative P&L is qualified by a losing interval, variable deposits, changing versions and downside exposure.
3. **PlainTape:** worthwhile operator engineering lead, pending fork-access and accounting reconciliation.

Freqtrade/NFI and Hummingbot remain useful infrastructure/strategy candidates; openthomas, FinRL and TradingAgents supply research architecture. None is excluded merely because deployed configuration is private. Reuse priority is not a capital-allocation recommendation.

The focused evidence-mapping phase is complete. Remaining gaps concern independent audits, reproducibility, costs, compatibility and the project operator’s constraints. Before building, define a short PRD, eligible market/account, experimental capital, tolerable loss, horizon and oversight, then obtain sign-off. No repositories were installed or run during this initial research phase.

User clarification: copying one route is sufficient; combining systems is not required. The draft PRD reflects this. Reference-vault snapshots and cross-venue replay limitations are retained in S51/S65. Independent feasibility review completed; no implementation. First proposed post-signoff experiment is the existing offline fake-live scenario, followed by failure/recovery validation.

Offline reference: [fake-live documentation](https://github.com/enarjord/passivbot/blob/master/docs/fake_live.md). It tests normal-loop behavior through a scripted local exchange without network/credentials, not trading profitability. Legacy IB dependency instructions need reconciliation with current repository dependencies, not an assumption of failure.

## Feasibility boundary

Software compatibility does not establish venue eligibility, adequate capital, or permission to trade. See OFFLINE_VALIDATION.md for the bounded local experiment.

### 2026-09-08 18:36 EDT , Alternate broker code
Pinned native sysbrokers tree has IB only plus generic interfaces. No turnkey alternate adapter verified. Official tastytrade Python archived; official JS available; tastyware/tastytrade unofficial async SDK requires audit. Tradovate official JS/C# examples are API tutorials, no maintained strategy or native adapter established. TradeStation use current v3 specification, avoid stale v2 examples. Alpaca official alpaca-py relevant only for explicit equities-route change. See readiness comparison for source links.
