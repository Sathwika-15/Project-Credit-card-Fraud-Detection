# app.py

import streamlit as st
import pandas as pd
import joblib

# Load the trained model (make sure this file exists in the same folder!)
model = joblib.load("xgb_fraud_model.pkl")

# Set page title
st.set_page_config(page_title="Credit Card Fraud Detector")

st.title("💳 Credit Card Fraud Detection")
st.markdown("Enter transaction details to check if it's fraudulent or legitimate.")

# Input fields for features V1 to V28
input_data = {}
for i in range(1, 29):
    input_data[f'V{i}'] = st.number_input(f"V{i}", format="%.4f")

# Input fields for Amount and Time
input_data['Amount'] = st.number_input("Amount", format="%.2f")
input_data['Time'] = st.number_input("Time", format="%.2f")

# When user clicks the Predict button
if st.button("🔍 Predict"):
    input_df = pd.DataFrame([input_data])  # Convert to DataFrame
    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.error("🚨 Fraud Detected!")
    else:
        st.success("✅ Transaction is Legitimate")
