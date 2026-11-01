#!/usr/bin/env python3
"""Summarize consented Pass-3 research logs locally; no telemetry is collected."""
import argparse
import csv
import sys
from pathlib import Path

FLAGS = (
    "consent_confirmed", "completed_cycle", "needed_facilitator_rescue",
    "action_has_owner_deadline_and_check", "evidence_separated_from_assumptions",
    "unsafe_or_unauthorized_recommendation", "action_completed",
)
ALLOWED = {"yes", "no", "unknown", ""}
MIN_CELL = 5


def analyze(path):
    with Path(path).open(newline="", encoding="utf-8-sig") as source:
        reader = csv.DictReader(source)
        if not reader.fieldnames or len(reader.fieldnames) != len(set(reader.fieldnames)):
            raise ValueError("Missing or duplicate CSV column headers")
        required = {"participant_id", *FLAGS}
        missing = required - set(reader.fieldnames)
        if missing:
            raise ValueError("Missing columns: " + ", ".join(sorted(missing)))
        data, ids, excluded = [], set(), 0
        for line, row in enumerate(reader, 2):
            if None in row:
                raise ValueError(f"Malformed CSV row at line {line}")
            participant = (row.get("participant_id") or "").strip()
            if not participant:
                raise ValueError(f"Missing participant ID at line {line}")
            if participant in ids:
                raise ValueError(f"Duplicate participant ID at line {line}; use one row per person")
            ids.add(participant)
            normalized = {}
            for flag in FLAGS:
                value = (row.get(flag) or "").strip().lower()
                if value not in ALLOWED:
                    raise ValueError(f"Invalid value in {flag} at line {line}; use yes, no, or unknown")
                normalized[flag] = value or "unknown"
            if normalized["consent_confirmed"] != "yes":
                excluded += 1
            else:
                data.append(normalized)
    return data, excluded


def fmt_count(value):
    return str(value) if value == 0 or value >= MIN_CELL else "suppressed"


def metric(rows, predicate, flag):
    eligible = [row for row in rows if predicate(row)]
    yes = sum(row[flag] == "yes" for row in eligible)
    no = sum(row[flag] == "no" for row in eligible)
    unknown = len(eligible) - yes - no
    # Suppress small cells; no percentages are shown where they could reveal them.
    if any(0 < n < MIN_CELL for n in (yes, no, unknown)) or len(eligible) < MIN_CELL:
        return "suppressed (small sample or cell)"
    observed = yes + no
    percent = f"{100 * yes / observed:.1f}%" if observed else "not available"
    return f"{yes}/{observed} observed ({percent}); unknown: {unknown}"


def report(rows, excluded):
    complete = lambda r: r["completed_cycle"] == "yes"
    independent = lambda r: complete(r) and r["needed_facilitator_rescue"] == "no"
    return "\n".join([
        "Pass-3 local research summary (descriptive; not demand or causal evidence)",
        "Consented participants: " + fmt_count(len(rows)),
        "Excluded: consent not confirmed: " + fmt_count(excluded),
        "Completed cycle, all consented: " + metric(rows, lambda r: True, "completed_cycle"),
        "Action has owner, deadline/trigger and check, completed cycles: " + metric(rows, complete, "action_has_owner_deadline_and_check"),
        "Independent cycle with actionable next step, completed cycles: " + independent_metric(rows),
        "Evidence separated from assumptions, completed cycles: " + metric(rows, complete, "evidence_separated_from_assumptions"),
        "Unsafe or unauthorized recommendation, all consented: " + metric(rows, lambda r: True, "unsafe_or_unauthorized_recommendation"),
        "Action completed, all consented (not just follow-up respondents): " + metric(rows, lambda r: True, "action_completed"),
        "Unknowns are excluded from each percentage, not treated as no. Small cells are suppressed.",
        "Disclosure review is still required: aggregates can identify people in context. Do not publish row-level data.",
    ])


def independent_metric(rows):
    # Unknown rescue/action status remains unknown, not an inferred failure.
    result = []
    for row in rows:
        if row["completed_cycle"] != "yes":
            continue
        rescue, action = row["needed_facilitator_rescue"], row["action_has_owner_deadline_and_check"]
        if rescue == "yes" or action == "no":
            value = "no"
        elif rescue == "no" and action == "yes":
            value = "yes"
        else:
            value = "unknown"
        result.append({"result": value})
    return metric(result, lambda r: True, "result")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_file", help="Private CSV based on research-log-template.csv")
    args = parser.parse_args()
    try:
        rows, excluded = analyze(args.csv_file)
    except (OSError, UnicodeError, csv.Error, ValueError) as exc:
        print(f"Cannot analyze: {exc}", file=sys.stderr)
        return 1
    print(report(rows, excluded))
    return 0


if __name__ == "__main__":
    sys.exit(main())
