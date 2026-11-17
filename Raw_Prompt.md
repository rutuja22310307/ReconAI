\# Raw Prompt – ReconAI



I want to build a Python-based payment reconciliation application called ReconAI for a payments company.



\## Problem



A payments company has two datasets:

1\. Company transaction records, which record payments immediately.

2\. Bank settlement records, which contain funds settled by the bank after 1–2 days.



At month end, both datasets should reconcile. However, there may be discrepancies. Build an application that compares these datasets and identifies the reasons for differences.



\## Requirements



\### 1. Synthetic Data Generation

Generate your own sample datasets because no input files are provided.



Include these scenarios:

\- A transaction recorded in one month but settled in the following month.

\- Small individual rounding differences that become significant when summed.

\- A duplicate record in one dataset.

\- A refund without a matching original payment.



\### 2. Reconciliation Engine

Build the reconciliation logic using Python and Pandas.



The engine should:

\- Match transactions using transaction IDs.

\- Identify matched transactions.

\- Detect missing settlements.

\- Detect duplicate records.

\- Identify next-month settlements.

\- Identify orphan refunds.

\- Detect amount mismatches.

\- Calculate aggregate financial differences accurately using Decimal.



\### 3. Dashboard

Build an interactive dashboard using Streamlit.



It should display:

\- Company transaction records.

\- Bank settlement records.

\- Total transaction counts.

\- Matched transactions.

\- Discrepancies.

\- Company payment total.

\- Bank payment total.

\- Aggregate difference.

\- Detailed discrepancy report.



Allow users to upload CSV files and download reconciliation reports.



\### 4. Testing

Create automated tests using pytest.



Test the following:

\- Next-month settlement.

\- Duplicate settlement.

\- Orphan refund.

\- Aggregate rounding difference.



\### 5. Project Structure

Keep the project modular with separate files for:

\- Dashboard.

\- Reconciliation engine.

\- Synthetic data generator.

\- Automated tests.

\- Requirements.

\- Project documentation.



\### 6. Technology Constraints

Use Python, Pandas, Streamlit, Plotly and Pytest.



Do not require paid services or external banking APIs for the demonstration.



\### 7. Expected Output

Deliver a working application with sample data, automated tests, a downloadable reconciliation report and clear explanations of discrepancies.



Explain assumptions and identify limitations that would need to be addressed before production deployment.



Guide me through implementation step by step, explaining code and helping debug errors.



