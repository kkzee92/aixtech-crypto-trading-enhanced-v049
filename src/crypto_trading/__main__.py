"""Demo entrypoint."""

from crypto_trading.core.engine import TradingEngine
from crypto_trading.security.risk_gate import RiskGate
from crypto_trading.strategies.spot import SpotMomentumStrategy
from crypto_trading.strategies.futures import FuturesFundingArbStrategy

def main():
    engine = TradingEngine(RiskGate(), mode="paper")
    engine.register_strategy(SpotMomentumStrategy())
    engine.register_strategy(FuturesFundingArbStrategy())
    # Synthetic market data
    data = {"symbol": "BTCUSDT", "price": 65000, "ma_20": 64000, "volatility": 0.03, "funding_rate": 0.0006}
    intents = engine.run_cycle(data)
    print("Paper intents:", intents)

if __name__ == "__main__":
    main()
