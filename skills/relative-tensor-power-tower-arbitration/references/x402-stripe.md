# x402 + Stripe facilitator on RTPTPA

Profit arbitration is RTPTPA. Settlement is x402. The Stripe record is a `PaymentIntent` in `transaction_verification` mode — it attests an on-chain USDC transfer without taking custody of the buyer.

## Accounts

| Layer | Value |
| --- | --- |
| Stripe | `acct_1Sw9EcL3TAuvgpHc` · Genesis Conductor, LLC · livemode |
| payTo | `0x60C4499870f115664d7FfD8411b023DBEf3377d9` |
| USDC Base | `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913` |
| Network | `eip155:8453` |
| Live worker | https://x402-paid-service.iholt.workers.dev |

Existing Stripe catalog (Yennefer.quest Starter / Pro / Subscription) is the fiat counterpart. x402 IP grants are SHA-pinned and agent-native; they do not replace those products.

## After `arbitrate()`

1. Freeze `power_tower_weights`.
2. Carve operator tithe (default 5%).
3. Map remainder × weights → `extra.profit.splits`.
4. Emit HTTP 402 with `PAYMENT-REQUIRED`.
5. On valid `PAYMENT-SIGNATURE`, write evt- `x402_negotiation` as a child of the RTPTPA evt.
6. Optionally record a Stripe PaymentIntent:

```
amount            = round(pool_usdc * 100)   # cents; skip if < 1
currency          = usd
payment_method    = crypto
crypto.mode       = transaction_verification
network           = base
transaction_hash  = on-chain tx
idempotency_key   = transaction_hash
```

Do **not** create live PaymentIntents from a preview facilitator. The local receipt is labeled `livemode: false` even though the Stripe account itself is live.

## Related skills

- `relative-tensor-power-tower-arbitration` — fusion engine
- `x402-negotiation-ip` — this handshake
- `igor-holt/x402-monetize-plugin` — generic paid-endpoint scaffold
