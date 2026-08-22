# RTPTPA-QCG — Relative-Tensor Power-Tower Prompt Arbitration

**OpenClaw + Hermes compatible skill** for fusing multi-agent prompts into quantum control directives for Diamond NV-center systems.

Companion skill **x402 negotiation IP** turns the same arbitration into a SHA-pinned USDC royalty table, settled over HTTP 402 with Stripe as facilitator.

## Install

### OpenClaw
```bash
# From this repo (workspace skills)
openclaw skills install git:igor-holt/rtptpa-openclaw-hermes@main
# or clone into ~/.openclaw/skills/ or <workspace>/skills/
```

### Hermes
Copy `skills/relative-tensor-power-tower-arbitration/` into `~/.hermes/skills/` or use OpenClaw → Hermes migration tooling.
Copy `skills/x402-negotiation-ip/` alongside it when licensing / profit splits are in scope.

## Triggers
- `rtpTPA` / `RTPTPA-QCG`
- `power-tower arbitration`
- `quantum control genesis`
- `hermes classify quantum-control`
- `mcp dispatch rtpTPA`
- `x402` / `negotiation IP` / `PAYMENT-REQUIRED` / `Stripe facilitator`

## Core Invariants
- Relative tensors only (coordinate-invariant)
- Power-tower hierarchical weights (thermodynamic → quantum → control → genesis)
- Thermodynamic cost (Landauer) tracking
- evt- provenance + post-quantum attestation ready
- Projection to Diamond NV control_spec (frequency, phase, DD scheme, fidelity)
- GitHub SHA pin is the IP coordinate; x402 `exact` scheme is the settlement wire

## Structure
```
skills/relative-tensor-power-tower-arbitration/
  SKILL.md
  scripts/rtpTPA.py
  references/genesis-conductor-integration.md
  references/maps-integration.md
  references/x402-stripe.md
skills/x402-negotiation-ip/
  SKILL.md
  schema.json          # x402 v2 challenge + Genesis extra (stripe, github, profit)
cloudflare/
  worker.js            # minimal authenticated webhook skeleton
examples/
  maps-deckgl-rtptpa.html
```

## x402 negotiation IP

Unpaid request → HTTP 402 + `PAYMENT-REQUIRED`. Buyer signs EIP-3009 and retries with `PAYMENT-SIGNATURE`. Amount equality is strict.

| Layer | Value |
| --- | --- |
| Stripe | `acct_1Sw9EcL3TAuvgpHc` · Genesis Conductor, LLC |
| payTo | `0x60C4499870f115664d7FfD8411b023DBEf3377d9` |
| USDC Base | `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913` |
| Live worker | https://x402-paid-service.iholt.workers.dev |

Operator tithe (default 500 bps) is carved before power-tower weights split the remainder. Each grant is bound to `owner/repo@sha`.

## Cloudflare Webhook
Minimal Worker for authenticated trigger + rate-limit + A2A JSONL emission. Deploy via Wrangler or Cloudflare dashboard. See `cloudflare/README.md`.

## Genesis Conductor Alignment
Compatible with Seismic Tree-of-Thoughts, Ouroboros V2, Diamondnode high-VPD portfolio, maru guards, and trace-consent ledger.

## Google Maps Platform + deck.gl Geo-Visualization (NEW)

The RTPTPA system is now geo-located as a holographic scientific dashboard over **NASA Ames Research Center** (Moffett Field, CA — home of QuAIL / Quantum Artificial Intelligence Laboratory).

**Coordinates**: 37.4153° N, 122.0628° W

Live Imagine-generated visualization (6s video of the full system pulsing over the Ames campus map):
- Relative-tensor network R_ij + power-tower bars (thermodynamic → quantum → control → genesis)
- Landauer entropy production field at 300 mK
- Diamond NV spin stabilization with XY8/CPMG dynamical decoupling
- GPU/NVML thermal heat maps
- Real-time crystal_score / spectral_gap metrics

**Interactive demo**: open `examples/maps-deckgl-rtptpa.html` (replace `YOUR_API_KEY` and optionally set a cloud Map ID).

This follows official Google Maps Platform best practices for scientific data visualization:
- deck.gl `GoogleMapsOverlay` (interleaved WebGL mode preferred for 3D depth with campus buildings)
- HeatmapLayer for entropy / thermal fields
- ScatterplotLayer / custom layers for NV centers and tensor nodes
- Vector basemap + tilt/rotation for cinematic camera

See `references/maps-integration.md` for full details, code, and links to GMP docs.

**Principal Investigator:** Igor Holt (Kovach Enterprises / Genesis Conductor)  
ORCID: 0009-0008-8389-1297

License: MIT
