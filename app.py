
import streamlit as st
import pandas as pd
from reconciliation import reconcile

st.set_page_config(
    page_title="ReconAI",
    page_icon="💳",
    layout="wide"
)

st.title("💳 ReconAI")
st.caption("Intelligent Payment Reconciliation System")
st.write(
    "Compare company payment records with actual bank settlements "
    "and identify financial discrepancies."
)


def generate_data():

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

    return transactions, settlements


st.sidebar.header("Data Input")

demo = st.sidebar.checkbox(
    "Use sample demonstration data",
    value=True
)

tx_file = st.sidebar.file_uploader(
    "Upload company transactions CSV",
    type=["csv"]
)

bank_file = st.sidebar.file_uploader(
    "Upload bank settlements CSV",
    type=["csv"]
)

if demo:
    tx, bank = generate_data()

elif tx_file is not None and bank_file is not None:
    try:
        tx = pd.read_csv(tx_file, dtype=str)
        bank = pd.read_csv(bank_file, dtype=str)
    except Exception as error:
        st.error(f"Could not read uploaded CSV: {error}")
        st.stop()

else:
    st.info("Upload both CSV files or enable sample demonstration data.")
    st.stop()


st.subheader("Uploaded Data")

col1, col2 = st.columns(2)

with col1:
    st.write("Company Transactions")
    st.dataframe(tx, width="stretch")

with col2:
    st.write("Bank Settlements")
    st.dataframe(bank, width="stretch")


try:
    report, summary = reconcile(tx, bank)
except Exception as error:
    st.error(f"Reconciliation error: {error}")
    st.stop()


st.divider()
st.subheader("Reconciliation Overview")

matched = int((report["Status"] == "Matched").sum())
discrepancies = len(report) - matched

c1, c2, c3, c4 = st.columns(4)

c1.metric("Company Transactions", len(tx))
c2.metric("Bank Settlements", len(bank))
c3.metric("Matched", matched)
c4.metric("Discrepancies", discrepancies)


st.divider()
st.subheader("Financial Summary")

c1, c2, c3 = st.columns(3)

c1.metric(
    "Company Payment Total",
    f"₹{summary['company_total']}"
)

c2.metric(
    "Bank Payment Total",
    f"₹{summary['bank_total']}"
)

c3.metric(
    "Aggregate Difference",
    f"₹{summary['aggregate_difference']}"
)

if summary["aggregate_rounding_difference"]:
    st.warning(
        "Aggregate rounding difference detected. "
        "Individual transaction differences may be within tolerance, "
        "but their combined difference exceeds the permitted tolerance."
    )
else:
    st.success("Aggregate totals are within the configured tolerance.")


st.divider()
st.subheader("Discrepancy Report")

st.dataframe(report, width="stretch")

st.subheader("Discrepancy Distribution")

st.bar_chart(report["Status"].value_counts())


st.divider()
st.subheader("Download Reports")

st.download_button(
    label="Download Reconciliation Report",
    data=report.to_csv(index=False),
    file_name="reconciliation_report.csv",
    mime="text/csv"
)

st.download_button(
    label="Download Company Transactions",
    data=tx.to_csv(index=False),
    file_name="company_transactions.csv",
    mime="text/csv"
)

st.download_button(
    label="Download Bank Settlements",
    data=bank.to_csv(index=False),
    file_name="bank_settlements.csv",
    mime="text/csv"
)

st.success("Reconciliation analysis completed.")
