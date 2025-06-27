# Credit Card Fraud Detection with XGBoost
Detect fraudulent credit card transactions using machine learning and deploy it with a Streamlit dashboard.

# Overview
This project uses the **Kaggle Credit Card Fraud Detection dataset** to:
- Identify fraudulent transactions
- Apply both **anomaly detection** (Isolation Forest, LOF)
- Train a supervised model using **XGBoost**
- Provide a user-friendly dashboard using **Streamlit**


# Dataset

Source: [Kaggle Credit Card Fraud Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
Records: 284,807 transactions
Class Imbalance: Only 0.17% frauds

# Tools Used
- Python
- Pandas, NumPy
- Scikit-learn
- XGBoost
- SHAP (Explainability)
- Streamlit (Dashboard)
- Joblib (Model Saving)

## Models Used

# Anomaly Detection
- Isolation Forest
- Local Outlier Factor (LOF)

# Supervised Learning
- XGBoost Classifier  
  - Oversampled data to handle class imbalance  
  - Evaluated using **F1, F2, ROC-AUC**

# Performance

| Metric         | Value (XGBoost) |
|----------------|----------------|
| Precision      | ~0.92          |
| Recall         | ~0.95          |
| F2-score       | ~0.93          |
| ROC-AUC        | ~0.99          |


# SHAP Explainability

Used SHAP to interpret model predictions:
- Identified key features: `V15`, `V17`, `Amount`, `Time`, etc.
- Plotted SHAP summary plots

# Dashboard Demo
Streamlit app allows users to input transaction features and predict fraud.

*Live App*: https://credit-card-fraud-detecton-jxuurnivebarakehppswxr.streamlit.app/


