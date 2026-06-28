# Data Analytics Portfolio – Sangeon An

**Master of IT Business Informatics (Business Analytics)** | Yoobee College, Auckland (2025–2026)

Background in process engineering and production data analysis at Corning Japan (2019–2023), currently transitioning into data analytics and business intelligence.

- Email: ansang1002@gmail.com
- Location: Auckland, New Zealand

---

## Project: Customer Churn Prediction & Revenue Risk Analysis

> **Context:** This project was completed as part of the MBI806B Business Data Analysis, Visualisation & Decision Making course at Yoobee College. The goal was to go beyond descriptive reporting and build an end-to-end analytical pipeline — from synthetic data generation through to an executive-level Power BI dashboard.

---

### Objectives

- Analyse Salesforce's 8% annual churn rate to identify why high-value customers leave
- Build a predictive ML model to flag at-risk customers before churn occurs
- Quantify revenue exposure by risk segment
- Identify the highest-ROI retention action to support C-level decision-making

---

### Data Source

The dataset was synthetically generated using Python to simulate a realistic Salesforce FY25 SaaS environment. No real customer data was used.

**Dataset size:** 20,000 customer records

**Why synthetic?**
Real Salesforce customer data is not publicly available. The dataset was engineered with realistic distributions, pricing tiers, and behavioural patterns to closely reflect actual SaaS dynamics — including Salesforce's reported 8% annual attrition rate.

**Variables used in the model:**

| Variable | Description |
|---|---|
| `Tenure_Months` | Duration of customer relationship (months) |
| `Usage_Activity_Score` | Product usage intensity score (0–100) |
| `Support_Tickets_Last_Month` | Number of support requests raised in the last month |
| `CSAT_Score` | Customer Satisfaction Score (0–10); measures overall service satisfaction |
| `Last_Interaction_Days` | Days since last customer interaction with the platform |
| `Monthly_Revenue` | Monthly recurring revenue per customer, mapped to Salesforce FY25 pricing tiers ($25–$330) |

**Additional columns (not used as model features):**

| Variable | Description |
|---|---|
| `Customer_ID` | Unique customer identifier (Salesforce-style format) |
| `Customer_Segment` | Small / Medium / Enterprise |
| `Subscription_Tier` | Starter / Professional / Enterprise / Unlimited |
| `Contract_Type` | Monthly / Annual / Multi-year |
| `Joining_Date` | Customer start date |
| `Churn` | Binary target variable (1 = churned, 0 = retained) |

**Data generation approach:**
- Monthly revenue mapped to subscription tier pricing: Starter ($25), Professional ($105), Enterprise ($165), Unlimited ($330)
- CSAT scores derived from usage activity and support ticket volume with added noise to reflect real-world variability
- Churn probability calibrated using a weighted risk score across customer segment, CSAT, usage activity, and support tickets — then thresholded at the 92nd percentile to produce an 8% churn rate

---

### Tools

| Tool | Purpose |
|---|---|
| **Python – Pandas, NumPy** | Data generation, cleaning, feature engineering |
| **Python – Scikit-learn** | Logistic Regression modelling, train/test split, class weighting, StandardScaler |
| **Python – Matplotlib, Seaborn** | EDA visualisations, sigmoid curve, confusion matrix, coefficient chart, correlation heatmap |
| **Power BI + DAX** | Interactive KPI dashboard, risk segmentation, revenue impact simulation |

---

### Methodology

#### 1. EDA & Data Cleaning

Before model training, Exploratory Data Analysis was conducted to understand the data structure and identify any issues.

**Data cleaning steps:**
- `Monthly_Revenue` was originally stored as a string with a `$` symbol — converted to float using regex replacement
- Verified no missing values across all 20,000 records
- Checked for outliers in continuous variables (Tenure_Months, Usage_Activity_Score, Last_Interaction_Days)

**Distribution analysis:**
- Compared distributions of key variables between churned (Churn=1) and retained (Churn=0) customers
- Churned customers showed consistently lower CSAT scores and higher support ticket counts

**Correlation analysis:**
- Generated a feature correlation heatmap to check for multicollinearity
- Confirmed no significant multicollinearity between independent variables
- CSAT_Score and Usage_Activity_Score showed a strong positive correlation (0.91) — both act as protective factors against churn
- Support_Tickets_Last_Month showed a positive correlation with churn (0.17)

#### 2. Model Selection

Logistic Regression was chosen over more complex alternatives for the following reasons:

- **Interpretability:** Coefficients and odds ratios directly quantify each variable's impact on churn probability — essential for communicating findings to non-technical C-level stakeholders
- **Appropriateness:** Churn is a binary outcome, which maps naturally to Logistic Regression's output structure
- **Transparency:** Unlike Random Forests or Gradient Boosting, the model's decision logic is fully explainable, which is critical in a business decision-support context

Other models considered:

| Model | Reason not selected |
|---|---|
| Decision Tree / Random Forest | Higher accuracy but lower interpretability; more prone to overfitting |
| Clustering (K-Means) | Useful for segmentation but cannot predict a labelled binary outcome |
| Reinforcement Learning | Not appropriate for static tabular data with a fixed target variable |

#### 3. Model Training

- **Train/test split:** 80% training, 20% test (stratified to preserve churn ratio)
- **Class imbalance handling:** `class_weight='balanced'` applied to prevent the model from being biased toward the majority class (non-churned customers)
- **Feature scaling:** StandardScaler applied to normalise feature magnitudes and prevent variables with larger ranges from dominating the model
- **Solver:** `lbfgs` with `max_iter=1000` to ensure convergence stability

#### 4. Risk Segmentation & KPI Design

Churn probabilities from the model were converted into business-usable KPIs:

**Risk segments (defined by churn probability threshold):**

| Segment | Churn Probability | Customer Count |
|---|---|---|
| Low | 0.0 – 0.4 | 15,547 |
| Medium | 0.4 – 0.7 | 1,466 |
| High | 0.7 – 1.0 | 2,987 |

**Expected Loss (DAX measure):**
```
Expected Loss = SUMX(Table, [Monthly_Revenue] * [Churn_Probability])
```
This metric combines churn probability with revenue to quantify financial exposure per customer and per segment.

**Immediate Intervention flag:**
Customers with Churn_Probability ≥ 0.5 were flagged for immediate retention action (3,964 customers, 19.8% of total).

---

### Model Performance

| Metric | Value |
|---|---|
| Accuracy | 87.58% |
| ROC-AUC | 0.9503 |
| Recall (churn class) | 0.99 |
| Precision (churn class) | 0.39 |

**Interpretation:**
- The high Recall (0.99) means the model correctly identified 316 out of 320 actual churned customers — very few were missed
- The low Precision (0.39) means the model also flags many retained customers as high-risk — a deliberate trade-off in a SaaS context where the cost of missing a churning customer outweighs the cost of over-intervention
- ROC-AUC of 0.95 indicates strong discriminative ability across all decision thresholds

---

### Key Results

- **$560.4K total revenue at risk** — quantified across all 20,000 customers
- **High-risk segment: $344.9K** potential loss | Medium: $122.5K | Low: $93.0K
- **10% CSAT improvement protects $180.4K** in revenue — 4x more effective than a 10% reduction in support tickets ($45.9K)
- **3,964 customers (19.8%)** flagged for immediate retention intervention
- **Top churn driver:** Support_Tickets_Last_Month (coefficient: +0.82, odds ratio: 2.27)
- **Strongest protective factor:** CSAT_Score (odds ratio: 0.04)

---

### Power BI Dashboard

![Dashboard Overview](images/dashboard_overview.png)

*Strategic Revenue Retention: Churn Drivers & Prevention Impact Analysis*

The dashboard includes:
- Core KPIs: total customers, churn rate, average churn probability, average tenure, revenue at risk, customers requiring action
- CSAT Score vs Churn Probability scatter plot (by customer segment)
- Expected Loss by risk segment (bar chart with dollar values)
- Feature impact chart: risk vs protective factors (coefficient strength)
- Action comparison: revenue impact of CSAT improvement vs support ticket reduction
- Interactive filters: Action Needed, Risk Segment, Contract Type, Subscription Tier

---

### Limitations

These limitations are worth noting when interpreting the results:

1. **Synthetic data** — the dataset was engineered rather than drawn from real customer records. Real-world data would contain more noise, edge cases, and unexpected patterns that this model has not been exposed to.

2. **Low precision** — at 0.39, the model flags a significant number of retained customers as high-risk. In a live environment, this could lead to unnecessary retention spend if interventions are applied without further filtering.

3. **Linear decision boundary** — Logistic Regression assumes a linear relationship between features and log-odds of churn. Non-linear interactions (e.g. low usage combined with rising support tickets) may not be fully captured.

4. **Static model** — customer behaviour and market conditions change over time. This model was trained on a fixed dataset and would require periodic retraining to remain accurate in a live deployment.

5. **No temporal features** — the model does not incorporate time-series patterns (e.g. declining usage trend over the past 3 months), which could improve predictive accuracy in a real SaaS setting.

---

### Files in This Repository

| File | Description |
|---|---|
| `Logistic_Regression_for_Salesforce.py` | Full Python code: data loading, EDA, model training, KPI generation |
| `Salesforce_Churn_PowerBI_Final.csv` | Final dataset with churn probabilities, risk segments, and intervention flags — ready for Power BI |
| `images/dashboard_overview.png` | Power BI dashboard screenshot |

---

## Skills

| Area | Tools |
|---|---|
| Machine Learning | Scikit-learn, Logistic Regression, EDA |
| Data Wrangling | Python, Pandas, NumPy |
| Visualisation | Power BI, Matplotlib, Seaborn, DAX |
| Database | SQL |
| Other | Excel (VBA, Pivot Tables), Jupyter Notebook, Google Colab |

---

## Background

Before transitioning into analytics, I spent four years as a Process Engineer at Corning Japan, where data analysis was part of daily operations: monitoring real-time sensor data, analysing microscope defect images, and adjusting production processes to maintain yield above 90% across lines producing around 2,500 units per day.

I am currently also working as a data entry operator at One Picture, processing Auckland Transport customer satisfaction survey data across bus, train, and ferry services, which has given me hands-on exposure to how real-world survey data is collected, structured, and prepared for analysis.

---

## Contact

ansang1002@gmail.com
