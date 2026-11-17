

\# ReconAI – Intelligent Payment Reconciliation System



\## 1. Project Overview



ReconAI is an AI-ready payment reconciliation platform designed to identify discrepancies between a company's transaction records and bank settlement records.



The application compares payment transactions with bank settlements, detects mismatches, identifies duplicates, validates refunds, and highlights aggregate rounding differences.



\## 2. Problem Statement



Payment platforms record transactions immediately, whereas banks generally settle payments in batches after one or two days.



This creates challenges during month-end reconciliation.



ReconAI helps identify:

\- Transactions settled in the following month.

\- Duplicate settlement records.

\- Refunds without matching original transactions.

\- Aggregate rounding differences.

\- Missing or mismatched settlements.



\## 3. Features



\- Automated payment reconciliation.

\- Company and bank CSV file uploads.

\- Duplicate transaction detection.

\- Next-month settlement detection.

\- Orphan refund detection.

\- Aggregate rounding analysis using Decimal.

\- Interactive financial dashboard.

\- Downloadable reconciliation reports.



\## 4. Technology Stack



\- Python 3.13

\- Streamlit

\- Pandas

\- Plotly

\- Pytest



\## 5. Project Structure



ReconAI/

\- app.py

\- reconciliation.py

\- data\_generator.py

\- requirements.txt

\- README.md

\- data/

&#x20; - transactions.csv

&#x20; - settlements.csv

\- tests/

&#x20; - test\_reconciliation.py



\## 6. Installation



Clone or download the project.



Install dependencies:



pip install -r requirements.txt



Generate sample datasets:



python data\_generator.py



\## 7. Run the Application



Execute:



python -m streamlit run app.py



Open the local URL displayed in the terminal.



\## 8. Run Automated Tests



Execute:



python -m pytest tests/ -v



\## 9. Sample Assessment Scenarios



1\. Next-month settlement: T104

2\. Aggregate rounding difference: T103, T107 and T108

3\. Duplicate bank settlement: T105

4\. Orphan refund: T106



Expected aggregate difference: ₹0.015.



\## 10. Production Limitations



1\. The current application uses synthetic sample data and does not connect directly to live banking systems.

2\. The reconciliation logic uses transaction IDs and a fixed tolerance; production systems may require more advanced matching rules.

3\. The application does not currently provide authentication, role-based access, or a complete audit trail.



\## 11. Future Enhancements



\- Secure bank API integration.

\- Advanced transaction matching.

\- Automated reconciliation scheduling.

\- Audit logs and user authentication.

\- AI-assisted anomaly investigation.



