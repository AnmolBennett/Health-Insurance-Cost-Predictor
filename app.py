import streamlit as st
import joblib
import pickle

# Load the pre-trained Gradient Boosting Regressor model
model = joblib.load('model_joblib_gr')

st.title("Insurance Cost Predictor")

# Get user input
age = st.number_input("Enter your age", min_value=0.0, step=1.0)
sex = st.number_input("Male or Female [0/1]", min_value=0.0, max_value=1.0, step=1.0)
bmi = st.number_input("Enter your BMI Value", min_value=0.0, step=0.1)
children = st.number_input("Enter Number of Children", min_value=0.0, step=1.0)
smoker = st.number_input("Smoker or not [0/1]", min_value=0.0, max_value=1.0, step=1.0)
region = st.number_input("Region [1-4]", min_value=1.0, max_value=4.0, step=1.0)

# Predict the insurance cost
if st.button("Predict"):
    result = model.predict([[age, sex, bmi, children, smoker, region]])
    st.write(f"Insurance Cost: {result[0]:.2f}")