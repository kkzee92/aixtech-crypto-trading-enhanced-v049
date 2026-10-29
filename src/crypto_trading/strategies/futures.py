"""Futures/Perps strategies."""

from typing import Optional
from crypto_trading.core.engine import Signal

class FuturesFundingArbStrategy:
    asset_class = "futures"

    def generate_signal(self, market_data: dict) -> Optional[Signal]:
        funding = market_data.get("funding_rate", 0)
        if abs(funding) > 0.0005:
            side = "sell" if funding > 0 else "buy"
            return Signal(
                symbol=market_data.get("symbol", "BTCUSDT-PERP"),
                side=side,
                size=0.01,
                asset_class=self.asset_class,
                confidence=0.65,
                metadata={"funding": funding},
            )
        return None
