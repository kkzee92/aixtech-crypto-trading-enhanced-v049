# AI Agent Rules

- Never include real API keys, secrets, private keys, seed phrases, or personal data (PDPA/GDPR style).
- Use only synthetic fixtures.
- Prefer paper/simulation modes. No live trading code paths without explicit multi-gate approval.
- All changes must pass CI gates: ruff, pytest, secret scan.
- Document AI assistance in commit messages with trailer: AI-Assisted: yes
- Strategies must declare asset_class and implement generate_signal returning Optional[Signal].
- Risk gate has final authority; strategies only propose signals.
- Follow zero-trust: least privilege, fail-closed.
