# Architecture and code map

Two investigations share an evidence standard, not a combined trading strategy.

## Offline Passivbot investigation

`passivbot-offline.patch` applies to the commit in `upstreams.json`. It changes the scripted fake-live harness, its regression tests, a restart fixture and the changelog. It does not change Rust strategy code or a live venue adapter. The original native terminal assertion failure remains documented in OFFLINE_VALIDATION.md.

## Native IBKR paper integration

- `pysystemtrade-connection.patch` validates the isolated profile before constructing the client and verifies the exact managed account before exposing the connection.
- `paper_guard.py` blocks writes by default. Its ephemeral lease permits only the specified MES contract and paper account, IOC limits, one entry and one reducing cleanup. It consumes each intent before the network call.
- `fetch_data.py` and `fetch_continuous.py` call the native IB price client. Continuous history is for the signal; contract resolution identifies the actual unexpired future for orders.
- `native_signal.py` feeds the native simple-system stages. It checks at least 200 valid traded days, order/uniqueness, OHLC bounds, gaps, freshness and measurable volatility.
- `operate.py` coordinates an exclusive process lock, SQLite synchronous FULL journal, native contract/order adapter, finite IOC monitoring, reconnect and reconciliation. Default invocation prepares without submitting an order. `--execute` is explicit.
- `verify_exit.py` opens an independent read-only client, checks positions and orders, and verifies the default mutation guard without sending its test order to the broker.
- `project_paths.py` places data, private configuration, upstream checkouts and the journal under configurable local storage. Packaging changes are path/configuration changes, not strategy changes.

The continuous PRICE denominator supports the selected EWMAC-only integration variant. It is not the native production multiple/adjusted/roll history pipeline and does not implement carry. No Mongo scheduler or perpetual execution service was deployed.
