# Results, telemetry, and analysis

## Current baseline

As of this document's preparation, **no independent participant sessions, follow-up results, or paid commitments are recorded here**. The [internal pilot](INTERNAL-PILOT.md) is a desk exercise, not a participant or customer result. There is no passive tracking, hosted analytics, visitor counter, or automatic transmission in this repository. Absence of recorded results is not a count of everyone who may have used the material.

## Collection and consent

Use the [research kit](RESEARCH-KIT.md) and its empty CSV template only after agreeing on participation, notes, access, retention, and deletion. Keep completed records in an approved private location; `private-research/` is ignored by Git as a convenience, not an access control or guarantee against disclosure. Store contact information separately. Do not put personal information, raw interview notes, private business details, or recordings in issues, public files, or logs. GitHub issue comments are public.

Use one row per pseudonymous participant. `yes`, `no`, `unknown`, and blank (treated as unknown) are valid for the analyzer's status columns. `completed_cycle` means a participant finished the cycle, not that the recommended action happened. `action_completed` should reflect actual follow-up; nonresponse is `unknown`. Record the quickstart version and dates, and record permission for follow-up separately. A row whose `consent_confirmed` is not `yes` is excluded from metrics. Do not enter a participant if recording their data is not authorized.

## Local analysis

Requires Python 3; no third-party dependencies or network access. From the repository root:

```bash
mkdir -p private-research
cp fleet/manifold-pass3/research-log-template.csv private-research/sessions.csv
# Fill the private CSV only after obtaining consent; then:
python3 tools/analyze_research.py private-research/sessions.csv
python3 -m unittest discover -s tests -v
```

The analyzer reports descriptive counts for consented participants and the completed-cycle subset, including independent, actionable cycles, evidence separation, unsafe recommendations, and follow-through. For each metric it uses observed yes/no responses as the percentage denominator and displays unknowns separately; follow-through uses all consented participants, not only responders. Duplicate IDs and invalid values are rejected. It suppresses individual counts of 1–4 and metric cells or eligible populations below five. This is a coarse precaution, **not anonymization**: combinations of statistics, dates, other publications, and contextual information can still identify people. Human review, consent, and any applicable privacy obligations remain necessary before sharing aggregates; small pilot findings should generally remain private.

Small-cell suppression also means the public-safe summary is **not a safety monitoring system**. The facilitator must flag unsafe outputs during each session and pause immediately; review private records under the agreed access controls. Do not wait for an aggregate to reveal a problem.

## Analysis post template — draft, not a finding

> **Question:** Can participants independently use the quickstart to select an owned, checkable action?
>
> **Method:** [recruitment method, dates, consent, sample and version; convenience sample limitations].
>
> **Results:** [eligible and completed counts; observed yes/no/unknown denominators; suppression and missing follow-up; safety issues in non-identifying form, only if consent and disclosure review permit].
>
> **What we learned:** [observations and representative, specifically approved quotes; distinguish facts from interpretation].
>
> **What we changed:** [version and precise changes; whether retested with new participants].
>
> **Limitations:** [small/nonrepresentative sample, missing responses, no control group, no causal or market-demand conclusions].
>
> **Next test:** [owner, action, deadline/trigger, predefined decision rule].

Do not publish percentages or a success claim from the empty template. Interest or completed worksheets are not revenue, and a small usability study cannot establish an uncontested market or prove business impact.
