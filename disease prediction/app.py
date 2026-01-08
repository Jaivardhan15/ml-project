import os
import pickle
import streamlit as st

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Disease Prediction System",
    page_icon="🧑‍⚕️",
    layout="wide"
)

# ------------------ MODEL LOADING ------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "saved_models")

def load_model(model_name):
    try:
        with open(os.path.join(MODEL_DIR, model_name), "rb") as file:
            return pickle.load(file)
    except Exception as e:
        st.error(f"Error loading {model_name}: {e}")
        return None

diabetes_model = load_model("diabetes_model.sav")
heart_model = load_model("heart_disease_model.sav")
parkinsons_model = load_model("parkinsons_model.sav")

# ------------------ SIDEBAR NAVIGATION ------------------
st.sidebar.title("🩺 Disease Prediction")
selected = st.sidebar.radio(
    "Select Prediction Type",
    (
        "Diabetes Prediction",
        "Heart Disease Prediction",
        "Parkinsons Prediction"
    )
)

# ==================================================
# DIABETES PREDICTION
# ==================================================
if selected == "Diabetes Prediction" and diabetes_model:
    st.title("🩸 Diabetes Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        pregnancies = st.number_input("Pregnancies", min_value=0)
    with col2:
        glucose = st.number_input("Glucose Level", min_value=0)
    with col3:
        blood_pressure = st.number_input("Blood Pressure", min_value=0)
    with col1:
        skin_thickness = st.number_input("Skin Thickness", min_value=0)
    with col2:
        insulin = st.number_input("Insulin Level", min_value=0)
    with col3:
        bmi = st.number_input("BMI", min_value=0.0)
    with col1:
        dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0)
    with col2:
        age = st.number_input("Age", min_value=1)

    if st.button("Diabetes Test Result"):
        result = diabetes_model.predict([[pregnancies, glucose, blood_pressure,
                                          skin_thickness, insulin, bmi, dpf, age]])
        st.success("🧪 Diabetic" if result[0] == 1 else "✅ Not Diabetic")

# ==================================================
# HEART DISEASE PREDICTION
# ==================================================
if selected == "Heart Disease Prediction" and heart_model:
    st.title("❤️ Heart Disease Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age", min_value=1)
    with col2:
        sex = st.selectbox("Sex", ["Male", "Female"])
    with col3:
        cp = st.number_input("Chest Pain Type", min_value=0)
    with col1:
        trestbps = st.number_input("Resting Blood Pressure", min_value=0)
    with col2:
        chol = st.number_input("Cholesterol (mg/dl)", min_value=0)
    with col3:
        fbs = st.number_input("Fasting Blood Sugar (>120)", min_value=0)
    with col1:
        restecg = st.number_input("Rest ECG", min_value=0)
    with col2:
        thalach = st.number_input("Max Heart Rate", min_value=0)
    with col3:
        exang = st.number_input("Exercise Induced Angina", min_value=0)
    with col1:
        oldpeak = st.number_input("ST Depression", min_value=0.0)
    with col2:
        slope = st.number_input("Slope", min_value=0)
    with col3:
        ca = st.number_input("Major Vessels", min_value=0)
    with col1:
        thal = st.number_input("Thal", min_value=0)

    sex_val = 1 if sex == "Male" else 0

    if st.button("Heart Disease Test Result"):
        result = heart_model.predict([[age, sex_val, cp, trestbps, chol,
                                       fbs, restecg, thalach, exang,
                                       oldpeak, slope, ca, thal]])
        st.success("💔 Heart Disease Detected" if result[0] == 1 else "✅ Healthy Heart")

# ==================================================
# PARKINSONS PREDICTION
# ==================================================
if selected == "Parkinsons Prediction" and parkinsons_model:
    st.title("🧠 Parkinson's Disease Prediction")

    labels = [
        "Fo", "Fhi", "Flo", "Jitter %", "Jitter Abs", "RAP", "PPQ", "DDP",
        "Shimmer", "Shimmer dB", "APQ3", "APQ5", "APQ", "DDA",
        "NHR", "HNR", "RPDE", "DFA", "Spread1", "Spread2", "D2", "PPE"
    ]

    inputs = []
    cols = st.columns(5)

    for i, label in enumerate(labels):
        with cols[i % 5]:
            inputs.append(st.number_input(label))

    if st.button("Parkinson's Test Result"):
        result = parkinsons_model.predict([inputs])
        st.success("🧠 Parkinson's Detected" if result[0] == 1 else "✅ No Parkinson's")

