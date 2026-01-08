# Sonar Rock vs Mine Prediction using Machine Learning

A Machine Learning web application that predicts whether an object detected by sonar signals is a Rock or a Mine, built using Python, Scikit-learn, and Streamlit.

This project demonstrates an end-to-end ML pipeline, from data preprocessing and model training to deployment using a clean and interactive web interface.

## 📌 Project Overview

Sonar systems are widely used in underwater exploration and defense to detect objects. This application uses sonar signal frequency data to classify objects into:

🪨 Rock

🚨 Mine

The model is trained on the Sonar Dataset and deployed as a Streamlit web app for real-time predictions.

## 🚀 Key Features

End-to-end Machine Learning pipeline

Logistic Regression–based classification model

Real-time predictions through a web interface

Streamlit-based UI (no HTML/CSS required)

Input validation and error handling

Model persistence using Pickle

Easy to run and deploy

## 🧠 Machine Learning Workflow

Dataset Loading

Feature & Label Separation

Train-Test Split

Model Training (Logistic Regression)

Model Evaluation

Model Serialization

Web App Deployment

## 🗂️ Folder Structure

sonar-streamlit-app/

│

├── app.py                  # Streamlit application

├── train_model.py          # Model training script

├── sonar_model.pkl         # Saved ML model

├── requirements.txt        # Dependencies

│

└── dataset/Sonar dataset.csv   # Dataset

## 🛠️ Tech Stack

Programming Language: Python

Machine Learning: Scikit-learn

Data Processing: Pandas, NumPy

Web Framework: Streamlit

Model Serialization: Pickle

### ⚙️ Installation & Setup

1️⃣ Clone the Repository 
```bash
git clone https://github.com/Jaivardhan15/sonar-rock-mine-prediction.git
cd sonar-rock-mine-prediction
```
2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
3️⃣ Train the Model
```bash
python train_model.py
```
4️⃣ Run the Application
```bash
streamlit run app.py
```

The application will open automatically at:
```bash
http://localhost:8501
```

## 🧪 How to Use

Enter 60 comma-separated numeric values representing sonar signals.

Click on Predict.

The app will classify the object as:

🪨 Rock

🚨 Mine

### 📊 Model Performance

Algorithm: Logistic Regression

Accuracy: ~85% (may vary due to random split)

## 🌟 Use Cases

Educational ML demonstrations

Underwater object classification

Defense and naval research simulations

Machine learning deployment practice

## 🔮 Future Enhancements

CSV file upload support

Probability score display

Model comparison (SVM, Random Forest)

Improved UI with charts

Cloud deployment (Streamlit Cloud / Render)

REST API integration
