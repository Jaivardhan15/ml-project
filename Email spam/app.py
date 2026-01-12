import streamlit as st
import pickle

# Load model & vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Page config
st.set_page_config(page_title="Email Spam Detector", page_icon="📧")

st.title("📧 Email Spam Detection")
st.write("Paste an email message below to check whether it is **Spam** or **Not Spam**.")

# Input
email_text = st.text_area("Email content", height=200)

# Predict
if st.button("Check Email"):
    if email_text.strip() == "":
        st.warning("Please enter an email message.")
    else:
        data = vectorizer.transform([email_text])
        prediction = model.predict(data)[0]
        probability = model.predict_proba(data)[0]

        if prediction == 1:
            st.error("🚨 Spam Email")
            st.write(f"Confidence: **{probability[1]*100:.2f}%**")
        else:
            st.success("✅ Not Spam")
            st.write(f"Confidence: **{probability[0]*100:.2f}%**")
