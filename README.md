# AIxTech Crypto Trading Enhanced v0.49

> Paper-only automated cryptocurrency trading information system with multi-asset-class strategies and strengthened zero-trust cyber/data security architecture.

![Python](https://img.shields.io/badge/python-3.10%2B-blue) ![Licence](https://img.shields.io/badge/licence-MIT-green)

## Overview

Enhanced reference implementation inspired by [zeekiankok92/aixtech-agent-harness-demo](https://github.com/zeekiankok92/aixtech-agent-harness-demo) AI-agent harness practices.

**Features:**
- Modular strategies per asset class (Spot, Futures/Perps, Options proxies, DeFi, Stablecoins, Altcoins)
- Multi-factor signals: regime detection, adaptive volatility sizing, correlation filters
- Zero-trust security: redaction, lineage tracking, risk gates, anomaly detection
- Fail-closed paper mode by default
- CI gates for lint, tests, secret scanning

**Disclaimer:** Educational/research only. Not financial advice. Substantial risk of loss. No live execution support in this version. Always paper-trade first. Comply with regulations.

## Quick Start

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m crypto_trading demo
```

## Architecture

See [docs/architecture.md](docs/architecture.md), [docs/security-architecture.md](docs/security-architecture.md), [docs/trading-strategies.md](docs/trading-strategies.md).

## AI-Agent Harness

Follows rules in `AGENTS.md`. Human review required. No production secrets or personal data.

## Licence

MIT © 2026
