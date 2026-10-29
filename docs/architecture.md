# System Architecture

```mermaid
flowchart TD
    Data[Market Data Synthetic] --> Strategies[Asset-Class Strategies]
    Strategies --> Risk[Zero-Trust Risk Gate]
    Risk --> Engine[Paper Engine]
    Engine --> Logs[Audit Lineage]
    Security[Redaction + Scans] -.-> Engine
```

Modular, fail-closed, paper-only.
