"""Altcoin relative strength strategy."""

from typing import Optional
from crypto_trading.core.engine import Signal

class AltcoinRelativeStrength:
    asset_class = "altcoin"

    def generate_signal(self, market_data: dict) -> Optional[Signal]:
        rs = market_data.get("relative_strength_btc", 1.0)
        liq = market_data.get("liquidity_score", 0.5)
        if rs > 1.05 and liq > 0.6:
            return Signal(
                symbol=market_data.get("symbol", "ETHUSDT"),
                side="buy",
                size=0.015,
                asset_class=self.asset_class,
                confidence=0.6,
                metadata={"rs": rs, "liq": liq},
            )
        return None
