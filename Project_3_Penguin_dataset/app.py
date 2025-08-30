# app.py

import streamlit as st
import pandas as pd
import pickle

# Load the saved pipeline model using pickle
with open('logisticreg_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("🐧 Penguin Species Prediction - Logistic Regression")

# User inputs
culmen_length_mm = st.number_input("Culmen Length (mm)", min_value=30.0, max_value=60.0, step=0.1)
culmen_depth_mm = st.number_input("Culmen Depth (mm)", min_value=13.0, max_value=22.0, step=0.1)
flipper_length_mm = st.number_input("Flipper Length (mm)", min_value=170.0, max_value=235.0, step=1.0)
body_mass_g = st.number_input("Body Mass (g)", min_value=2700.0, max_value=6300.0, step=10.0)

island = st.selectbox("Island", ['Biscoe', 'Dream', 'Torgersen'])
sex = st.selectbox("Sex", ['Male', 'Female'])

# Prediction button
if st.button("Predict"):
    # Create input dataframe
    input_data = pd.DataFrame({
        'island': [island],
        'culmen_length_mm': [culmen_length_mm],
        'culmen_depth_mm': [culmen_depth_mm],
        'flipper_length_mm': [flipper_length_mm],
        'body_mass_g': [body_mass_g],
        'sex': [sex]
    })

    # Make prediction
    prediction = model.predict(input_data)[0]
    species_map = {0: 'Adelie', 1: 'Chinstrap', 2: 'Gentoo'}
    predicted_species = species_map.get(prediction, "Unknown")

    # Show result
    st.success(f"Predicted Species: 🐧 {predicted_species}")
