# Pass-3: a decision cycle for finding market gaps

A lightweight, seven-step decision aid for founders and small teams exploring a possible underserved market. Start with a customer and their current alternatives; finish with **one owned, checkable next action**. It can be run by one person or with an assistant—no deployment, numerical engine, or multi-agent fleet required.

- **[Start here: five-minute market-gap quickstart](fleet/manifold-pass3/BLUE-OCEAN-QUICKSTART.md)** — worksheet, copy-paste prompt, and fictional worked example.
- **[Full Pass-3 protocol](fleet/manifold-pass3/PROTOCOL.md)** — role contracts, consent and stop rules, and a cycle record.
- **[Validation plan](fleet/manifold-pass3/VALIDATION-PLAN.md)** and **[research kit](fleet/manifold-pass3/RESEARCH-KIT.md)** — proposed sessions, consent script, and an empty log; no user research or commercial results are claimed.
- **[Internal desk pilot](fleet/manifold-pass3/INTERNAL-PILOT.md)** — an example using this repository, not an independent user test.
- **[Results and local analysis](fleet/manifold-pass3/RESULTS-AND-TELEMETRY.md)** — privacy-conscious, opt-in research workflow; no passive tracking.

A “blue ocean” is a hypothesis to investigate, not a finding established by this tool. It does not prove novelty, demand, willingness to pay, or outcomes; the decision owner remains responsible for evidence, authorization, and consequential decisions.

## What else is in this repository?

| Path | Status |
| --- | --- |
| `fleet/` | The source material and decision protocol; Passes 1 and 2 are historical dialects, not separate required agents. |
| `skills/relative-tensor-power-tower-arbitration/` | Experimental numerical prototype and skill description. **Not validated for quantum control, weighting decisions, or deployment.** |
| `skills/x402-negotiation-ip/` | Experimental x402 licensing schema and documentation. Integration and settlement are not verified by the Pass-3 protocol. |
| `cloudflare/` | Bearer-authenticated webhook **stub**, not an engine or production service. No HMAC or replay protection; optional KV rate limiting is non-atomic. |
| `examples/` and `references/` | Illustrations and integration notes, not evidence of live telemetry, validated control, or institutional endorsement. |

### Numerical prototype limitations

The Python prototype requires NumPy, which is not declared in the skill's current OpenClaw metadata. It should not be used to drive physical hardware or allocate value. Its normalized iterative weights tend toward uniformity, its componentwise relative formula is not generally coordinate-invariant, and output projection can saturate. Fidelity and thermodynamic cost values are formula-derived rather than measured. Its event record includes a hardcoded `1.28` convergence value and a structural-invariance flag; neither establishes an observed result. No cryptographic attestation is performed by the Python script. These limitations remain unresolved; the standalone decision protocol does not depend on it.

The geographic visualization uses a NASA Ames/QuAIL location as an illustrative setting only. This repository does not establish affiliation, endorsement, or operation there. The map example requires external services and an API key; simulated values are not measurements.

## License and attribution

The repository metadata declares MIT, but this checkout does not contain a standalone license file. Repository materials attribute the work to Igor Holt (ORCID 0009-0008-8389-1297).
