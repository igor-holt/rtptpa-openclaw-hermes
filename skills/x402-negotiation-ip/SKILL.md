---
name: x402-negotiation-ip
description: Negotiate GitHub-pinned intellectual property over x402 HTTP 402. RTPTPA power-tower weights become the USDC royalty table. Stripe records a crypto PaymentIntent in transaction_verification mode against Genesis Conductor, LLC. Triggers on x402, negotiation IP, profit arbitration, PAYMENT-REQUIRED, Stripe facilitator, SHA-pin license.
metadata: {"openclaw": {"requires": {"bins": ["python3"]}, "related": ["relative-tensor-power-tower-arbitration"]}}
---

# x402 Negotiation IP on Agentic Profit Arbitration

Activate when an agent must license SHA-pinned IP, split a USDC pool among competing claimants, or settle an HTTP 402 challenge. Payment is the credential. There is no account, API key, or subscription.

## Invariants

1. **GitHub is the IP coordinate.** Every grant names `owner/repo@sha`. Relative, never floating HEAD.
2. **RTPTPA splits the pool.** Competing claims are prompts. Crystal score × spectral gap → power-tower weights. Operator tithe (default 500 bps) is carved first.
3. **x402 v2 is the wire.** Unpaid request → HTTP 402 + `PAYMENT-REQUIRED` (base64 JSON). Buyer signs EIP-3009 `transferWithAuthorization` and retries with `PAYMENT-SIGNATURE`. Amount equality is strict (`exact` scheme).
4. **Stripe is the facilitator record.** `acct_1Sw9EcL3TAuvgpHc` (Genesis Conductor, LLC). `payment_method_types: [crypto]`, `crypto.mode: transaction_verification`, network `base`. Live USDC still settles to `0x60C4499870f115664d7FfD8411b023DBEf3377d9`.
5. **Emit evt-.** `record_type: x402_negotiation`. Parent is the RTPTPA arbitration evt.

## Handshake

```
GET/POST  /api/x402/challenge?ip=<id>
        → 402  PAYMENT-REQUIRED: <base64 x402 v2 body>

POST      /api/x402/settle
          { challenge, payment_signature }
        → 200  { license, stripe PaymentIntent-shaped receipt, evt- }
        → 402  if signature/amount/payTo/timeout fail
```

Catalog (free): `GET /api/x402/`

Live reference (real USDC on Base, Coinbase CDP facilitator):

| Tier | URL | Amount (USDC atomic) |
| --- | --- | --- |
| Discovery | `POST https://x402-paid-service.iholt.workers.dev/api/execute` | `10000` ($0.01) |
| Founders | `GET https://x402-paid-service.iholt.workers.dev/api/founders` | `4999000000` ($4,999) |

`payTo` = `0x60C4499870f115664d7FfD8411b023DBEf3377d9`  
USDC Base = `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913` (`eip155:8453`)

Always convert `amount` by 10^6 before paying.

## Accepts extra (Genesis extension)

Each `accepts[]` entry carries:

- `extra.stripe` — account, livemode, `transaction_verification`
- `extra.github` — owner, repo, sha, license
- `extra.profit` — `operator_tithe_bps`, `pool_usdc`, `splits[]`, `arbitration_id`
- `extra.ip` — catalog id, name, kind

## Procedure

1. Select IP from the catalog (SHA-pinned).
2. Set pool USDC and operator tithe.
3. Ingest claimant prompts (treasury, skill author, protocol agent, …).
4. Run RTPTPA. Freeze weights at challenge time.
5. Return 402 with `PAYMENT-REQUIRED`.
6. Verify signature: payTo, exact amount, validity window.
7. Grant non-transferable license bound to the SHA. Write Stripe-shaped PaymentIntent. Emit evt-.

Do not dilute this into a checkout form. Agents negotiate in-band over HTTP.
