# Pass-3 Arbitration Protocol

A structured, single-cycle method for choosing one next action when a decision has competing options, uncertain evidence, and limited attention. One person or one assistant can run it; the seven roles are sequential checks, not seven separate agents. The result is a recommendation for an accountable human to accept, change, or reject.

This is an operational decision aid, not a validated prediction, physical simulation, automated payment system, or guarantee of an outcome. It does not depend on the `rtpTPA.py` engine. An example or risk score is not evidence of revenue, measured thermodynamic savings, or real-world performance.

## When to use it

Use for a bounded decision with a real task, a decision owner, at least one feasible option, and an identifiable constraint. Examples: choosing a customer discovery action, deciding whether to build or defer a feature, or selecting a coalition's next experiment. Do not use it to replace qualified review for safety-critical, legal, medical, financial, or other consequential decisions.

**Deliverable:** a cycle record and a three-statement summary: current position, binding constraint, and exactly one next vector. A vector is one actionable step with an owner, a deadline or trigger, and a checkable result. If action is not justified, the vector can be a bounded information-gathering step, a human escalation, or an explicit stop.

## Before the cycle

1. Name the task and decision owner. Identify what decision is actually in scope, the deadline, options, available evidence, constraints, and what cannot be reversed easily. Ask for missing information when it would change the decision; otherwise label assumptions.
2. List the permitted surfaces (documents, systems, or stakeholders) and who may access them. Do not access a surface, publish, contact someone, spend money, or deploy anything without authorization.
3. **Trace and consent:** agree on what will be recorded, where it will be stored, who can see it, and retention/deletion rules. Record only necessary information. A local record is not an immutable ledger, and a hash is not consent. If the required consent or authorized storage is absent, stop and request it; do not claim a D1, Merkle, or ORCID entry exists unless actually created and verified.
4. **Diathesis pre-check:** before any live multi-agent task, identify potential harms, sensitive data, authority boundaries, and failure/rollback paths. If the work is outside authorization or requires expertise or safeguards that are unavailable, escalate or stop. A solo desk review can use the same check.
5. Supply `risk_R` only if the operator has a defined scoring method; record its definition and basis. The repository's `R > 0.4` trigger is an internal heuristic, not a calibrated probability. If risk is unknown, write `null`, not a fabricated score, and consider a reframe or escalation on the evidence.

### Input template

```json
{
  "task": "Decision to make",
  "pass": 3,
  "decision_owner": "Authorized owner",
  "risk_R": null,
  "risk_basis": "unknown; no scoring method supplied",
  "surfaces": ["authorized documents or systems"],
  "elapsed_cycles": 0,
  "options": ["option A", "option B", "defer"],
  "evidence": ["source and observation; distinguish assumptions"],
  "constraints": ["budget, deadline, permissions, or other limits"],
  "consent_and_storage": "agreed recording scope and location",
  "live_task": true
}
```

`elapsed_cycles` is the number of prior completed cycles on this task, not the number of speakers or tool calls. `surfaces` identifies allowed sources and destinations, not permission to act on them. If inputs are insufficient, output the missing information as the next vector rather than inventing it.

## Seven beats, in order

Write a short note for each beat. One role speaks at a time; these can be sections in a single document.

1. **Orchestrator — frame.** State the present position ("height"), the candidate binding constraint, the next speaker, and forbidden moves. A binding constraint is the limitation that most directly prevents the objective *now*; state the evidence or mark it as an assumption. Forbid unauthorized actions and duplicate sources of truth.
2. **Accumulator — compounding test.** For each plausible action, ask: does it create a reusable primitive, and does it lower the cost of the next operation? Only if both are supported label it `compounding`; otherwise `additive` or `unknown`. Note what can be reused, what should remain open, and whether a fork creates a second source of truth. Volume alone is not progress.
3. **Catalyst — intervention.** Propose one feasible intervention or `null`. Explain why its expected benefit justifies its cost and coordination burden, and name the alternatives rejected. Treat cost as an estimate unless measured.
4. **Bound-watcher — surplus inquisition.** Test the proposed benefit: (a) measured, with what instrument and source? (b) stable under a relevant perturbation, such as changing an assumption or label? (c) already contained in an existing artifact? Classify surplus as `genuine` (supported incremental benefit), `ductile` (repackaging or already captured), or `none` (no demonstrated benefit). Record untested claims as unverified and keep unverified limits binding. Where a claim is physical or thermodynamic, a hermitian audit means naming the measurement method, units, and evidence; absent these, make no measurement claim.
5. **Decoherence-arbiter — timing.** Choose exactly one: `crystallize` (commit to a bounded action or artifact), `reinvest` (gather evidence or improve an existing artifact), or `leave_uncollapsed` (defer a commitment). State the reason and what remains open. If there is no live task and fewer than two prior cycles, use `leave_uncollapsed`.
6. **Invariance-engine — decision.** Choose one judgment and one next vector using the binding constraint, not a majority vote. State what is retained, demoted, and uncertain. Escalate unresolved disagreement to the decision owner after at most one reframe; do not spawn agents to manufacture consensus.
7. **Scribe — communicate.** Write three statements: current position, binding constraint, and next vector. Keep the complete summary to one page at most. Include the owner, deadline or trigger, and verification criterion in the next vector. State uncertainties plainly.

## Reframe and stop rules

- **Maru / `#!nox`:** if a defined `risk_R` is greater than 0.4 or the task presents a no-win, challenge the objective or assumption, not just the options. Record the original framing, proposed reframe, supporting reason, and an A2A artifact: a short, shareable handoff containing the task, decision, evidence, and next vector. This is a document, not evidence that an agent-to-agent system was invoked. A reframe does not itself reduce risk; do not invent a new score.
- If a reframe still leaves a material disagreement or missing authority, escalate to the human owner. No new catalog, Worker, agent fleet, or second source of truth is required by this protocol.
- Finish the seven beats, emit the record and summary, then **stop**. Do not restart beat 1 unless the operator supplies a new task. A later decision is a new task even if it follows from this one.
- `leave_uncollapsed` is a valid outcome. No action, deployment, payment, endorsement, or result has occurred merely because it appears in a record.

## Cycle record template

Save where consent permits; use `unknown`, `null`, or an empty list rather than fabricate evidence.

```json
{
  "record_type": "pass_cycle",
  "pass": 3,
  "task": "",
  "decision_owner": "",
  "risk_R": null,
  "risk_basis": "",
  "surfaces": [],
  "elapsed_cycles": 0,
  "precheck": {"consent": "", "harms_and_authority": "", "rollback": ""},
  "reframe": {"triggered": false, "original": "", "reframed": "", "basis": ""},
  "orchestrator": {"height": "", "binding_constraint": "", "next_speaker": "accumulator", "forbidden_moves": []},
  "accumulator": {"assessment": [], "reusable": [], "leave_open": []},
  "catalyst": {"intervention": null, "rationale": "", "rejected": []},
  "bound_watcher": {"evidence_and_tests": [], "binding": [], "surplus_verdict": "none"},
  "decoherence_arbiter": {"timing": "leave_uncollapsed", "reason": "", "open": []},
  "invariance_engine": {"judgment": "", "retained": [], "demoted": [], "uncertainties": []},
  "next_vector": {"action": "", "owner": "", "deadline_or_trigger": "", "verification": ""},
  "surfaces_touched": [],
  "status": "closed"
}
```

The `surplus_verdict` values are `genuine`, `ductile`, or `none`; `timing` values are `crystallize`, `reinvest`, or `leave_uncollapsed`. Record actual surfaces touched, not just permitted ones. `status: closed` means the reasoning cycle stopped, not that the recommended action was completed.

## Worked example (illustrative, not a real engagement)

**Task:** A small advisory team has one week to decide whether to build a dashboard or test demand for its existing decision protocol. Owner: team lead. Evidence: the protocol exists; no buyer interviews or sales are documented for this hypothetical case. Constraints: one week, no budget approved for development. The team consents to a private notes document; no customer contact is authorized yet. Risk is unscored.

1. **Frame:** Current position: a reusable protocol exists. Candidate binding constraint: demand is untested, not lack of a dashboard. Forbidden: deploy or contact customers without approval.
2. **Compound:** A reusable interview plan could lower the cost of learning (`compounding`, assuming the owner uses it); dashboard work is `unknown` without evidence of demand.
3. **Intervene:** Draft a one-page interview plan using the existing protocol. Reject dashboard development for now because it does not directly test demand.
4. **Watch bounds:** No measured demand or conversion benefit; the plan's reuse is a hypothesis. Verdict: `none` for demonstrated commercial surplus; budget and contact authorization remain binding.
5. **Time:** `reinvest` in evidence preparation, not a product launch. Interviews and sales remain open.
6. **Decide:** Retain the existing protocol; defer the dashboard. The owner should prepare a plan, not claim validation.
7. **Summary:** A decision protocol exists, but demand is unknown. The binding constraint is lack of buyer evidence and contact authorization. By Friday, the team lead will draft a one-page interview plan in the authorized private document; completion is verified by the owner's review of the plan, not by a claimed sale.

## Source and adaptation

This standalone guide operationalizes the repository's [cycle kernel](cycle-kernel.md), [role contracts](roles.jsonl), [compounding test](../power-tower-fleet/EVOLVED.md), and [surplus inquisition](../genesis-tower-fleet/EVOLVED.md). The [tunnel note](TUNNEL.md) proposes an advisory use but explicitly does not establish revenue. Where integrations are named in the original skill, this guide treats them as checks or external dependencies—not as services that have been executed. The original files remain the historical source; this guide does not create a new pass or claim validated outcomes.
