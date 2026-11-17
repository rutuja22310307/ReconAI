
import unittest
import pandas as pd

from reconciliation import reconcile


class TestReconAI(unittest.TestCase):

    def setUp(self):
        self.transactions = pd.DataFrame([
            ["T1", "PAYMENT", "", "2026-01-31", "50.00"],
            ["T2", "PAYMENT", "", "2026-01-10", "100.005"],
            ["T3", "PAYMENT", "", "2026-01-11", "100.005"],
            ["T4", "PAYMENT", "", "2026-01-12", "100.005"],
            ["T5", "PAYMENT", "", "2026-01-15", "20.00"],
            ["R1", "REFUND", "UNKNOWN", "2026-01-20", "-10.00"]
        ], columns=[
            "transaction_id", "type", "original_transaction_id",
            "date", "amount"
        ])

        self.settlements = pd.DataFrame([
            ["T1", "2026-02-01", "50.00"],
            ["T2", "2026-01-11", "100.00"],
            ["T3", "2026-01-12", "100.00"],
            ["T4", "2026-01-13", "100.00"],
            ["T5", "2026-01-16", "20.00"],
            ["T5", "2026-01-16", "20.00"]
        ], columns=[
            "transaction_id", "settlement_date", "amount"
        ])

    def test_next_month_settlement(self):
        report, summary = reconcile(
            self.transactions, self.settlements
        )
        self.assertEqual(
            report.loc[report["Transaction ID"] == "T1", "Status"].iloc[0],
            "Next-month settlement"
        )

    def test_duplicate_settlement(self):
        report, summary = reconcile(
            self.transactions, self.settlements
        )
        self.assertEqual(
            report.loc[report["Transaction ID"] == "T5", "Status"].iloc[0],
            "Duplicate settlement"
        )

    def test_orphan_refund(self):
        report, summary = reconcile(
            self.transactions, self.settlements
        )
        self.assertEqual(
            report.loc[report["Transaction ID"] == "R1", "Status"].iloc[0],
            "Orphan refund"
        )

    def test_aggregate_rounding_difference(self):
        report, summary = reconcile(
            self.transactions, self.settlements
        )
        self.assertTrue(summary["aggregate_rounding_difference"])
        self.assertEqual(
            summary["aggregate_difference"], "0.015"
        )


if __name__ == "__main__":
    unittest.main()
