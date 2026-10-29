"""Spot market strategies with enhancements."""

from typing import Optional
from crypto_trading.core.engine import Signal

class SpotMomentumStrategy:
    asset_class = "spot"

    def generate_signal(self, market_data: dict) -> Optional[Signal]:
        # Enhanced: simple momentum with regime proxy
        price = market_data.get("price", 0)
        ma = market_data.get("ma_20", price)
        vol = market_data.get("volatility", 0.02)
        if price > ma * (1 + vol) and vol < 0.1:
            return Signal(
                symbol=market_data.get("symbol", "BTCUSDT"),
                side="buy",
                size=0.02,  # volatility-adjusted later
                asset_class=self.asset_class,
                confidence=0.7,
                metadata={"regime": "trend"},
            )
        return None
