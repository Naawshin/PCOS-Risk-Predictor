import streamlit as st
import pandas as pd
import joblib
import os

st.title("PCOS Risk Predictor")

# Inputs
age = st.number_input("Age", 1, 120, 25)
bmi = st.selectbox("BMI", ["Normal", "Overweight", "Underweight", "Obese"])
menstrual_regularity = st.selectbox("Menstrual Regularity", ["Regular", "Irregular"])
hirsutism = st.selectbox("Hirsutism", ['Yes', 'No'])
acne_severity = st.selectbox("Acne Severity", ['Unknown', 'Mild', 'Moderate', 'Severe'])
family_history_of_pcos = st.selectbox("Family History of PCOS", ['Yes', 'No'])
insulin_resistance = st.selectbox("Insulin Resistance", ['Yes', 'No'])
stress_levels = st.selectbox("Stress Levels", ['Low', 'Medium', 'High'])
urban_or_rural = st.selectbox("Urban/Rural", ['Urban', 'Rural'])
socioeconomic_status = st.selectbox("Socioeconomic Status", ['Low', 'Middle', 'High'])

# Load the model
model_path = os.path.join("backend", "model", "model.pkl")
model = joblib.load(model_path)

# Prediction button
if st.button("Predict"):
    input_df = pd.DataFrame([{
        "Age": age,
        "BMI": bmi,
        "Menstrual Regularity": menstrual_regularity,
        "Hirsutism": hirsutism,
        "Acne Severity": acne_severity,
        "Family History of PCOS": family_history_of_pcos,
        "Insulin Resistance": insulin_resistance,
        "Stress Levels": stress_levels,
        "Urban/Rural": urban_or_rural,
        "Socioeconomic Status": socioeconomic_status
    }])

    prediction = model.predict(input_df)[0]

    st.success(f"Prediction: {prediction}")



    # send post request to fastapi
    # try:
    #     response = requests.post("http://localhost:8000/predict", json=data)
    #     if response.status_code == 200:
    #         result = response.json()
    #         st.success(f"Prediction: {result['prediction']}")
    #     else:
    #         st.error(f"Error: {response.status_code} - {response.text}")
    # except Exception as e:
    #     st.error(f"An error occurred: {e}")
