Data Analytics Portfolio – VIctor(Sangeon) An

Master of IT Business Informatics (Business Analytics) | Yoobee College, Auckland (2025–2026)

Email: ansang1002@gmail.com
Location: Auckland, New Zealand



Project: Customer Churn Prediction & Revenue Risk Analysis

Executive Summary

This project quantifies financial exposure from customer churn and identifies the highest-ROI retention action using a data-driven approach. Starting from raw customer behavioural data, the analysis produces a client segmentation framework based on revenue risk, and simulates the financial impact of two competing retention strategies — delivering the kind of actionable, numbers-first insight that supports executive decision-making.


Key outcome: $560.4K in revenue at risk identified across 20,000 customers. A 10% improvement in customer satisfaction scores protects $180.4K — four times more effective than reducing support volume by the same margin.




Business Problem

Salesforce reported an 8% annual churn rate in FY25 — above the healthy SaaS benchmark of 4–7%. The underlying problem is not the churn rate itself, but the lack of visibility into which customers are at risk, how much revenue is exposed, and where to allocate retention resources for the greatest financial return.

This analysis addresses that gap by moving from a single aggregate churn metric to a customer-level risk model with direct revenue implications.


Data

Synthetic dataset of 20,000 SaaS customer records, engineered with Python to reflect Salesforce FY25 pricing and behavioural patterns. Key variables: customer satisfaction score (CSAT), usage activity, support ticket volume, contract tenure, and monthly recurring revenue ($25–$330 per customer). Churn rate calibrated to 8% to match reported figures.


Tools


Python (Pandas, NumPy, Scikit-learn) — data preparation, feature engineering, and predictive modelling
Power BI + DAX — interactive dashboard for revenue risk monitoring and retention scenario simulation



Key Findings


$560.4K total revenue at risk — identified by combining individual churn probability with monthly revenue, enabling financial exposure to be tracked at the customer level rather than as an aggregate rate
High-risk segment accounts for the majority of exposure — $344.9K (High) vs $122.5K (Medium) vs $93.0K (Low), enabling prioritised resource allocation
Customer satisfaction is the primary lever — a 10% CSAT improvement protects $180.4K in revenue, compared to $45.9K from an equivalent reduction in support ticket volume; investing in service quality yields four times the financial return
19.8% of customers (3,964) flagged for immediate action — providing a ready-to-use intervention list for account management teams



Power BI Dashboard


Dashboard Preview:
<img width="1276" height="717" alt="image" src="https://github.com/user-attachments/assets/3c39d4eb-b2aa-4a56-b5ab-e5525e66f87e" />

The dashboard is built around four business questions:


Where is the revenue risk concentrated? — KPI cards show total exposure ($560.4K) and the proportion of customers requiring action (19.8%)
Who are the highest-risk customers? — CSAT vs churn probability scatter plot, segmented by customer tier (Enterprise / Medium / Small)
How much is each risk group worth? — Expected loss bar chart broken down by High / Medium / Low segment
Which retention action delivers better ROI? — Side-by-side revenue impact comparison of CSAT improvement vs support ticket reduction


Interactive filters allow analysis by contract type, risk segment, and subscription tier.


Limitations & Next Steps

This analysis is based on synthetic data, which means real-world noise, edge cases, and behavioural patterns not captured in the model design are absent. In a live environment, the model would need periodic retraining as customer behaviour and market conditions shift.

The framework developed here — combining predictive risk scoring with revenue-weighted segmentation — is directly applicable to financial services contexts such as client retention analysis, portfolio-level risk monitoring, and ROI-based resource allocation across client segments.


Skills

AreaToolsData Analysis & ModellingPython, Pandas, Scikit-learnBusiness IntelligencePower BI, DAXData WranglingNumPy, Matplotlib, SeabornOtherSQL, Excel (VBA, Pivot Tables), Jupyter Notebook
