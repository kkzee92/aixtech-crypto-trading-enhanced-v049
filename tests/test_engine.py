from crypto_trading.core.engine import TradingEngine, Signal
from crypto_trading.security.risk_gate import RiskGate
from crypto_trading.strategies.spot import SpotMomentumStrategy

def test_paper_cycle():
    engine = TradingEngine(RiskGate())
    engine.register_strategy(SpotMomentumStrategy())
    data = {"price": 100, "ma_20": 90, "volatility": 0.02}
    intents = engine.run_cycle(data)
    assert isinstance(intents, list)
