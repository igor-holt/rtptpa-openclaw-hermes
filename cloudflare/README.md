# Cloudflare Worker for RTPTPA Triggers

Minimal authenticated webhook skeleton that accepts multi-agent prompts and returns a control_spec / evt- envelope.

## Deploy

```bash
# With Wrangler
cd cloudflare
npm i -g wrangler   # if needed
wrangler secret put RTP_TPA_SECRET
# optional: create KV namespace for rate limiting + A2A log, bind as RATE_LIMIT_KV / A2A_LOG
wrangler deploy
```

Or paste `worker.js` into the Cloudflare dashboard Workers editor and set the secret + bindings.

## Usage

```bash
curl -X POST https://<your-worker>.workers.dev/rtpTPA \
  -H "Authorization: Bearer $RTP_TPA_SECRET" \
  -H "Content-Type: application/json" \
  -d '{
    "prompts": [
      "Stabilize NV |0⟩ at 300 mK with minimal Landauer cost",
      "Apply XY8 dynamical decoupling"
    ],
    "crystal_scores": [0.95, 0.82],
    "spectral_gaps": [0.2, 0.15]
  }'
```

## Production Notes

- Replace the stub with a call to the real `RTPTPA` engine (Durable Object running Python, or HTTP to a Genesis Conductor / MCP endpoint).
- Add HMAC signature verification and timestamp window for full replay protection.
- Enforce maru / R>0.4 guards before committing high-stakes control directives.
- Emit full A2A JSONL for utilization ledger and VPD accounting.
