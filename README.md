# RTPTPA-QCG — Relative-Tensor Power-Tower Prompt Arbitration

**OpenClaw + Hermes compatible skill** for fusing multi-agent prompts into quantum control directives for Diamond NV-center systems.

## Install

### OpenClaw
```bash
# From this repo (workspace skills)
openclaw skills install git:igor-holt/rtptpa-openclaw-hermes@main
# or clone into ~/.openclaw/skills/ or <workspace>/skills/
```

### Hermes
Copy `skills/relative-tensor-power-tower-arbitration/` into `~/.hermes/skills/` or use OpenClaw → Hermes migration tooling.

## Triggers
- `rtpTPA` / `RTPTPA-QCG`
- `power-tower arbitration`
- `quantum control genesis`
- `hermes classify quantum-control`
- `mcp dispatch rtpTPA`

## Core Invariants
- Relative tensors only (coordinate-invariant)
- Power-tower hierarchical weights (thermodynamic → quantum → control → genesis)
- Thermodynamic cost (Landauer) tracking
- evt- provenance + post-quantum attestation ready
- Projection to Diamond NV control_spec (frequency, phase, DD scheme, fidelity)

## Structure
```
skills/relative-tensor-power-tower-arbitration/
  SKILL.md
  scripts/rtpTPA.py
  references/genesis-conductor-integration.md
cloudflare/
  worker.js          # minimal authenticated webhook skeleton
```

## Cloudflare Webhook
Minimal Worker for authenticated trigger + rate-limit + A2A JSONL emission. Deploy via Wrangler or Cloudflare dashboard. See `cloudflare/README.md`.

## Genesis Conductor Alignment
Compatible with Seismic Tree-of-Thoughts, Ouroboros V2, Diamondnode high-VPD portfolio, maru guards, and trace-consent ledger.

**Principal Investigator:** Igor Holt (Kovach Enterprises / Genesis Conductor)  
ORCID: 0009-0008-8389-1297

License: MIT
