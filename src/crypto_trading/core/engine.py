"""Core trading engine — fail-closed, signal-to-order pipeline."""

from typing import Protocol, Optional, List
from dataclasses import dataclass

@dataclass
class Signal:
    symbol: str
    side: str  # "buy" | "sell"
    size: float
    asset_class: str
    confidence: float
    metadata: dict

class Strategy(Protocol):
    asset_class: str

    def generate_signal(self, market_data: dict) -> Optional[Signal]:
        ...

class TradingEngine:
    """Orchestrates strategies → risk → (paper) execution."""

    def __init__(self, risk_gate, mode: str = "paper"):
        self.risk_gate = risk_gate
        self.mode = mode
        self.strategies: List[Strategy] = []

    def register_strategy(self, strategy: Strategy) -> None:
        self.strategies.append(strategy)

    def run_cycle(self, market_data: dict) -> list[dict]:
        intents = []
        for strat in self.strategies:
            signal = strat.generate_signal(market_data)
            if signal is None:
                continue
            if not self.risk_gate.approve(signal):
                continue
            intent = {
                "symbol": signal.symbol,
                "side": signal.side,
                "size": signal.size,
                "mode": self.mode,
                "strategy": type(strat).__name__,
                "asset_class": signal.asset_class,
                "confidence": signal.confidence,
            }
            intents.append(intent)
        return intents
