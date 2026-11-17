\# Distilled Prompt – ReconAI



\## Project Title

ReconAI – Intelligent Payment Reconciliation Platform



\## Objective

Develop a Python-based payment reconciliation platform that compares company transaction records against bank settlement records and automatically identifies financial discrepancies.



\## Functional Requirements



\### 1. Data Generation

Generate synthetic company transaction and bank settlement CSV datasets containing:

\- Next-month settlements.

\- Accumulated rounding differences.

\- Duplicate records.

\- Refunds without original transactions.



\### 2. Reconciliation Engine

Implement modular reconciliation logic using Python and Pandas.



Use Python Decimal for accurate monetary calculations.



Identify:

\- Matched transactions.

\- Missing settlements.

\- Duplicate transactions or settlements.

\- Next-month settlements.

\- Orphan refunds.

\- Amount mismatches.

\- Aggregate rounding differences.



\### 3. Interactive Dashboard

Build a Streamlit dashboard displaying:

\- Transaction and settlement datasets.

\- Reconciliation statistics.

\- Company and bank financial totals.

\- Aggregate differences.

\- Detailed discrepancy reports.



Support CSV uploads and downloadable reconciliation reports.



\### 4. Automated Testing

Use Pytest to verify the required discrepancy scenarios and financial calculations.



\### 5. Technology Stack

\- Python

\- Pandas

\- Streamlit

\- Plotly

\- Pytest

\- Decimal



\### 6. Deliverables

\- Working application.

\- Synthetic datasets.

\- Modular source code.

\- Automated tests.

\- Project documentation.

\- Deployable application.



\## Assumptions

\- Transaction IDs are used as the primary matching key.

\- Bank settlements may occur 1–2 days after transactions.

\- A tolerance of ₹0.01 is used for individual amount comparisons.

\- Aggregate differences are calculated separately.

\- Synthetic data is used for demonstration.



\## Production Considerations

The solution should clearly identify limitations involving live banking integration, advanced transaction matching, authentication, audit logging, and financial data security.



