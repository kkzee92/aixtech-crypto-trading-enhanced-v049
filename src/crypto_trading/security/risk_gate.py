"""Risk gate with zero-trust checks."""

from typing import Any

class RiskGate:
    def __init__(self, max_position_pct: float = 0.05, max_drawdown: float = 0.15):
        self.max_position_pct = max_position_pct
        self.max_drawdown = max_drawdown

    def approve(self, signal: Any) -> bool:
        # Fail-closed: basic checks
        if signal.size <= 0 or signal.confidence < 0.5:
            return False
        if signal.size > self.max_position_pct:
            return False
        # Add more: correlation, volatility regime, etc.
        return True
