---
name: relative-tensor-power-tower-arbitration
description: Experimental prompt-arbitration prototype. Its outputs are illustrative and are not validated for quantum control or real-world allocation decisions.
metadata: {"openclaw": {"requires": {"bins": ["python3"]}, "emoji": "⚛️"}}
---

# Relative-Tensor Power-Tower Prompt Arbitration (experimental)

This skill describes a research prototype, not an operational quantum-control system. For a standalone human decision process, use the [Pass-3 protocol](../../fleet/manifold-pass3/PROTOCOL.md); it does not depend on this script.

## Important limitations

- `scripts/rtpTPA.py` imports NumPy; the metadata above checks only for Python, not NumPy. Installing the skill alone does not install that dependency.
- The componentwise relative formula is not generally invariant to coordinate shifts. Normalizing at each power-tower layer tends to make weights uniform, and the projected outputs can saturate. The embedding is a deterministic heuristic, not a validated semantic model.
- Fidelity and thermodynamic costs are arithmetic estimates, not hardware measurements. The event record's `convergence_improvement_factor: 1.28` and `structural_invariance: true` are hardcoded, not measured results. `attestation_ready` does not mean an output has been signed or verified.
- The script does not generate a validated executable hardware control sequence, perform a quantum simulation, or implement post-quantum signing. Do not dispatch its output to physical hardware or use it for financial allocations.

## Implementation and references

The prototype is `scripts/rtpTPA.py`; its self-test runs with `python3 scripts/rtpTPA.py` after NumPy is installed in the chosen environment. The output is illustrative only.

See [Genesis Conductor integration notes](references/genesis-conductor-integration.md), [x402 notes](references/x402-stripe.md), and the repository's [maps notes](../../references/maps-integration.md). These are proposals or illustrations, not evidence that external systems are connected or deployed. The [Cloudflare Worker](../../cloudflare/README.md) is a stub with no replay protection.
