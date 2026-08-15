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
  references/maps-integration.md
cloudflare/
  worker.js          # minimal authenticated webhook skeleton
examples/
  maps-deckgl-rtptpa.html   # Google Maps + deck.gl holographic overlay demo
```

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
