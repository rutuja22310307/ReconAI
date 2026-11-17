
import pandas as pd
import os

os.makedirs("data", exist_ok=True)

# Company transaction records
transactions = pd.DataFrame([
    ["T101", "PAYMENT", "", "2026-01-05", "100.00"],
    ["T102", "PAYMENT", "", "2026-01-10", "200.00"],
    ["T103", "PAYMENT", "", "2026-01-15", "100.005"],
    ["T104", "PAYMENT", "", "2026-01-31", "50.00"],
    ["T105", "PAYMENT", "", "2026-01-20", "20.00"],
    ["T106", "REFUND", "T999", "2026-01-25", "-10.00"],
    ["T107", "PAYMENT", "", "2026-01-16", "100.005"],
    ["T108", "PAYMENT", "", "2026-01-17", "100.005"]
], columns=[
    "transaction_id",
    "type",
    "original_transaction_id",
    "date",
    "amount"
])

# Bank settlement records
settlements = pd.DataFrame([
    ["T101", "2026-01-06", "100.00"],
    ["T102", "2026-01-11", "200.00"],
    ["T103", "2026-01-16", "100.00"],
    ["T104", "2026-02-01", "50.00"],
    ["T105", "2026-01-21", "20.00"],
    ["T105", "2026-01-21", "20.00"],
    ["T107", "2026-01-17", "100.00"],
    ["T108", "2026-01-18", "100.00"]
], columns=[
    "transaction_id",
    "settlement_date",
    "amount"
])

transactions.to_csv(
    "data/transactions.csv", index=False
)

settlements.to_csv(
    "data/settlements.csv", index=False
)

print("Sample datasets generated successfully!")
print("Created: data/transactions.csv")
print("Created: data/settlements.csv")
