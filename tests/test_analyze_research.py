import csv
import importlib.util
import tempfile
import unittest
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "tools/analyze_research.py"
spec = importlib.util.spec_from_file_location("analyzer", PATH)
a = importlib.util.module_from_spec(spec)
spec.loader.exec_module(a)

class AnalyzerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "data.csv"
        self.fields = ["participant_id", *a.FLAGS]

    def write(self, rows):
        with self.path.open("w", newline="") as out:
            writer = csv.DictWriter(out, fieldnames=self.fields)
            writer.writeheader()
            writer.writerows(rows)

    def row(self, pid, **overrides):
        row = dict.fromkeys(self.fields, "unknown")
        row.update(participant_id=pid, consent_confirmed="yes", completed_cycle="yes",
                   needed_facilitator_rescue="no", action_has_owner_deadline_and_check="yes")
        row.update(overrides)
        return row

    def test_empty_and_small_are_suppressed(self):
        self.write([])
        rows, excluded = a.analyze(self.path)
        self.assertIn("Consented participants: 0", a.report(rows, excluded))
        self.write([self.row("p1")])
        rows, excluded = a.analyze(self.path)
        self.assertIn("Consented participants: suppressed", a.report(rows, excluded))
        self.assertIn("Independent cycle with actionable next step, completed cycles: suppressed", a.report(rows, excluded))

    def test_consent_and_unknowns(self):
        self.write([self.row(str(i), action_completed="unknown") for i in range(5)] +
                   [self.row("excluded", consent_confirmed="no")])
        rows, excluded = a.analyze(self.path)
        self.assertEqual((len(rows), excluded), (5, 1))
        result = a.report(rows, excluded)
        self.assertIn("5/5 observed (100.0%)", result)
        self.assertIn("0/0 observed (not available); unknown: 5", result)
        self.assertNotIn("excluded", result.lower().split("excluded:")[-1].splitlines()[0])

    def test_small_cell_suppressed(self):
        rows = [self.row(str(i), unsafe_or_unauthorized_recommendation="no") for i in range(5)]
        rows.append(self.row("x", unsafe_or_unauthorized_recommendation="yes"))
        self.write(rows)
        report = a.report(*a.analyze(self.path))
        self.assertIn("Unsafe or unauthorized recommendation, all consented: suppressed", report)

    def test_duplicate_and_invalid_rejected(self):
        self.write([self.row("p"), self.row("p")])
        with self.assertRaisesRegex(ValueError, "Duplicate participant"):
            a.analyze(self.path)
        self.write([self.row("p", completed_cycle="maybe")])
        with self.assertRaisesRegex(ValueError, "Invalid value"):
            a.analyze(self.path)

if __name__ == "__main__":
    unittest.main()
