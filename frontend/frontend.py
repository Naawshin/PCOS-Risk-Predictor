import streamlit as st
import requests

st.title("PCOS Risk Predictor")
st.markdown("Enter the following details to predict your risk of having PCOS:")

# input fields  
age = st.number_input("Age", min_value=1, max_value=120, step=1)
bmi = st.selectbox("BMI", ["Normal", "Overweight", "Underweight", "Obese"])
menstrual_regularity = st.selectbox("Menstrual Regularity", ["Regular", "Irregular"])
hirsutism = st.selectbox("Hirsutism", ['Yes', 'No'])
acne_severity = st.selectbox("Acne Severity", ['Unknown', 'Mild', 'Moderate', 'Severe'])
family_history_of_pcos = st.selectbox("Family History of PCOS", ['Yes', 'No'])
insulin_resistance = st.selectbox("Insulin Resistance", ['Yes', 'No'])
stress_levels = st.selectbox("Stress Levels", ['Low', 'Medium', 'High'])
urban_or_rural = st.selectbox("Urban/Rural", ['Urban', 'Rural'])
socioeconomic_status = st.selectbox("Socioeconomic Status", ['Low', 'Middle', 'High'])


# button to trigger prediction
if st.button("predict"):
    data = {
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
    }

    # send post request to fastapi
    try:
        response = requests.post("http://localhost:8000/predict", json=data)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Prediction: {result['prediction']}")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
