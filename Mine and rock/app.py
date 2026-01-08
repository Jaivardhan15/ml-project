import streamlit as st
import numpy as np
import pickle

# Load model
with open("sonar_model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="Sonar Prediction", layout="centered")

st.title("🛥️ Sonar Rock vs Mine Prediction")

st.write("Enter 60 comma-separated sonar signal values:")

input_data = st.text_area("Input Values")

if st.button("Predict"):
    try:
        values = list(map(float, input_data.split(",")))
        
        if len(values) != 60:
            st.error("Please enter exactly 60 values.")
        else:
            prediction = model.predict(np.array(values).reshape(1, -1))
            result = "🚨 Mine" if prediction[0] == "M" else "🪨 Rock"
            st.success(f"Prediction: {result}")
    except:
        st.error("Invalid input format.")
