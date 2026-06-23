import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score
from sklearn.preprocessing import StandardScaler

# 1. Load Dataset
df = pd.read_csv("Salesforce_Customer_Dataset.csv")

# 2. Monthly_Revenue Preprocessing
# Cleaning currency symbols and converting to float if necessary
if df['Monthly_Revenue'].dtype == 'object':
    df['Monthly_Revenue'] = df['Monthly_Revenue'].replace(r'[\$, ]', '', regex=True).astype(float)

# 3. Feature Selection for Churn Prediction
features = [
    'Tenure_Months',
    'Usage_Activity_Score',
    'Support_Tickets_Last_Month',
    'CSAT_Score',
    'Last_Interaction_Days',
    'Monthly_Revenue'
]

X = df[features]
y = df['Churn']

# 4. Train/Test Split (Stratified to maintain churn ratio)
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 5. Feature Scaling (Standardization)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 6. Logistic Regression (With Class Balancing)
model = LogisticRegression(
    class_weight='balanced',
    max_iter=1000,
    solver='lbfgs'
)
model.fit(X_train_scaled, y_train)

# 7. Prediction and Probability Calculation
y_prob = model.predict_proba(X_test_scaled)[:, 1]
threshold = 0.5
y_pred = (y_prob >= threshold).astype(int)

# --- Model Performance Metrics ---
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(f"ROC-AUC Score: {roc_auc_score(y_test, y_prob):.4f}")
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# =================================================================
# 8. Sigmoid S-Curve Visualization (Strategic Decision Support)
# =================================================================
# Calculate Logit values (Z)
z = np.dot(X_test_scaled, model.coef_.T) + model.intercept_

plt.figure(figsize=(10, 6))
sns.scatterplot(
    x=z.flatten(),
    y=y_prob,
    hue=y_test.values,
    palette='coolwarm',
    alpha=0.5
)

# Plotting the mathematical Sigmoid Curve
line_z = np.linspace(z.min(), z.max(), 200)
line_p = 1 / (1 + np.exp(-line_z))
plt.plot(line_z, line_p, color='green', label='Sigmoid Function')

plt.axhline(y=threshold, color='red', linestyle='--', label=f'Threshold ({threshold})')
plt.xlabel('Logit (Z Value)')
plt.ylabel('Churn Probability')
plt.title('Sigmoid S-Curve: Probability Structure of Attrition')
plt.legend()
plt.show()

# =================================================================
# 9. Generating Predictive KPIs for Power BI Integration
# =================================================================
# Scale the entire dataset for deployment
all_scaled = scaler.transform(X)
df['Churn_Probability'] = model.predict_proba(all_scaled)[:, 1]

# Define Predictive KPI Segments (Risk Groups)
df['Risk_Segment'] = pd.cut(
    df['Churn_Probability'],
    bins=[0, 0.4, 0.7, 1.0],
    labels=['Low', 'Medium', 'High'],
    include_lowest=True
)

# Action Trigger: Flagging customers for immediate intervention
df['Immediate_Intervention'] = np.where(
    df['Churn_Probability'] >= threshold,
    'Yes',
    'No'
)

# Export finalized dataset for Business Intelligence
df.to_csv("Salesforce_Churn_PowerBI_Final.csv", index=False)
print("\n[Complete] Final dataset with Revenue & ML KPIs saved for Power BI.")

# =================================================================
# 10. Driver Analysis & Feature Importance
# =================================================================

# Driver Analysis Data Frame
importance_df = pd.DataFrame({
    'Feature': features,
    'Coefficient': model.coef_[0],
    'Odds_Ratio': np.exp(model.coef_[0])
}).sort_values(by='Coefficient', ascending=False)

# Visualization: Strategic Impact of Variables
plt.figure(figsize=(10, 6))
sns.barplot(x='Coefficient', y='Feature', data=importance_df, palette='RdYlGn_r')
plt.axvline(x=0, color='black', linestyle='-', linewidth=1)
plt.title('Churn Drivers: Risk Factors (+) vs. Protective Factors (-)', fontsize=13)
plt.show()

# Print Odds Ratio for Business Interpretation
print("\n--- Odds Ratio Analysis (Impact Magnitude) ---")
for index, row in importance_df.iterrows():
    print(f"{row['Feature']}: Changes churn risk by a factor of {row['Odds_Ratio']:.2f}")

# =================================================================
# 11. Model Parameters for Power BI DAX Calculation
# =================================================================
print("\n--- Parameters for DAX Implementation ---")
print(f"Intercept: {model.intercept_[0]}")
for feature, coef in zip(features, model.coef_[0]):
    print(f"{feature} Coefficient: {coef}")