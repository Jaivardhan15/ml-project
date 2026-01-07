import streamlit as st
import numpy as np
import pickle

# Load trained model
with open("sonar_model.pkl", "rb") as f:
    model = pickle.load(f)

# Page config
st.set_page_config(
    page_title="Sonar Rock vs Mine Prediction",
    page_icon="🛥️",
    layout="centered"
)

# Title
st.title("🛥️ Sonar Rock vs Mine Prediction")
st.write(
    """
    This application uses a **Machine Learning model** to predict whether
    an object detected by sonar signals is a **Rock** or a **Mine**.
    """
)

st.markdown("---")

# Input section
st.subheader("📥 Input Sonar Data")
st.write("Enter **60 comma-separated numerical values**:")

input_data = st.text_area(
    "Example: 0.02, 0.03, 0.04, ...",
    height=120
)

# Prediction
if st.button("🔍 Predict"):
    try:
        values = list(map(float, input_data.split(",")))

        if len(values) != 60:
            st.error("❌ Please enter exactly **60 values**.")
        else:
            input_array = np.array(values).reshape(1, -1)
            prediction = model.predict(input_array)[0]

            if prediction == "M":
                st.error("🚨 **Prediction: MINE**")
            else:
                st.success("🪨 **Prediction: ROCK**")

    except ValueError:
        st.error("❌ Invalid input. Please enter numeric values only.")

st.markdown("---")

# Footer
st.caption("Built using Python, Scikit-learn & Streamlit")
