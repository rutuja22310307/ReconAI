
import pandas as pd
from decimal import Decimal, InvalidOperation

TOLERANCE = Decimal("0.01")


def money(value):
    try:
        return Decimal(str(value))
    except (InvalidOperation, ValueError):
        raise ValueError(f"Invalid amount: {value}")


def reconcile(transactions, settlements):

    required_tx = {
        "transaction_id", "type",
        "original_transaction_id", "date", "amount"
    }

    required_bank = {
        "transaction_id", "settlement_date", "amount"
    }

    if not required_tx.issubset(transactions.columns):
        raise ValueError("Missing transaction columns")

    if not required_bank.issubset(settlements.columns):
        raise ValueError("Missing settlement columns")

    tx = transactions.copy()
    bank = settlements.copy()

    # Validate amounts
    for value in tx["amount"]:
        money(value)

    for value in bank["amount"]:
        money(value)

    # Find duplicate IDs
    duplicate_tx_ids = set(
        tx.loc[
            tx.duplicated("transaction_id", keep=False),
            "transaction_id"
        ]
    )

    duplicate_bank_ids = set(
        bank.loc[
            bank.duplicated("transaction_id", keep=False),
            "transaction_id"
        ]
    )

    # Find original payment IDs
    payment_ids = set(
        tx.loc[
            tx["type"].str.upper() == "PAYMENT",
            "transaction_id"
        ]
    )

    results = []

    for _, transaction in tx.iterrows():

        tid = transaction["transaction_id"]
        kind = str(transaction["type"]).upper()

        if tid in duplicate_tx_ids:
            results.append([
                tid, "Duplicate transaction",
                "Repeated transaction ID",
                str(transaction["amount"]), None
            ])
            continue

        # Refund validation
        if kind == "REFUND":

            original_id = transaction["original_transaction_id"]

            if pd.isna(original_id) or original_id not in payment_ids:
                status = "Orphan refund"
                explanation = "Original payment does not exist"
            else:
                status = "Refund"
                explanation = "Original payment exists"

            results.append([
                tid, status, explanation,
                str(transaction["amount"]), None
            ])
            continue

        # Find bank settlement
        matches = bank[
            bank["transaction_id"] == tid
        ]

        if tid in duplicate_bank_ids:
            results.append([
                tid, "Duplicate settlement",
                "Multiple bank entries found",
                str(transaction["amount"]), None
            ])
            continue

        if matches.empty:
            results.append([
                tid, "Missing settlement",
                "No matching bank entry",
                str(transaction["amount"]), None
            ])
            continue

        settlement = matches.iloc[0]

        company_amount = money(transaction["amount"])
        bank_amount = money(settlement["amount"])

        difference = abs(company_amount - bank_amount)

        transaction_date = pd.to_datetime(transaction["date"])
        settlement_date = pd.to_datetime(
            settlement["settlement_date"]
        )

        if (
            transaction_date.month != settlement_date.month
            or transaction_date.year != settlement_date.year
        ):
            status = "Next-month settlement"
            explanation = "Settlement occurred in another month"

        elif difference > TOLERANCE:
            status = "Amount mismatch"
            explanation = f"Difference: {difference}"

        else:
            status = "Matched"
            explanation = (
                "Within individual tolerance; "
                "aggregate difference checked separately"
            )

        results.append([
            tid, status, explanation,
            str(company_amount), str(bank_amount)
        ])

    # Create report
    report = pd.DataFrame(
        results,
        columns=[
            "Transaction ID",
            "Status",
            "Explanation",
            "Company Amount",
            "Bank Amount"
        ]
    )

    # Aggregate payment totals
    payments = tx[
        tx["type"].str.upper() == "PAYMENT"
    ]

    payment_ids_for_total = set(
        payments["transaction_id"]
    )

    bank_payments = (
        bank[
            bank["transaction_id"].isin(payment_ids_for_total)
        ]
        .drop_duplicates("transaction_id", keep="first")
    )

    company_total = sum(
        (money(x) for x in payments["amount"]),
        Decimal("0")
    )

    bank_total = sum(
        (money(x) for x in bank_payments["amount"]),
        Decimal("0")
    )

    aggregate_difference = abs(
        company_total - bank_total
    )

    summary = {
        "company_total": str(company_total),
        "bank_total": str(bank_total),
        "aggregate_difference": str(aggregate_difference),
        "aggregate_rounding_difference": (
            aggregate_difference > TOLERANCE
        )
    }

    return report, summary
