# 📧 Email Spam Detection System

An end-to-end Machine Learning web application that classifies emails as Spam or Not Spam using Natural Language Processing (NLP).
The project includes a trained ML model, a Flask backend, and a simple frontend with prediction confidence display.

## 🚀 Features

🧠 Machine Learning–based spam classification

📊 Confidence score using probability prediction

🌐 Web interface built with Flask

🧹 Clean and simple UI

📁 Modular and scalable project structure

🧪 Trained on a real-world spam dataset

## 🛠️ Tech Stack

Programming Language: Python

Web Framework: Flask

Machine Learning: Scikit-learn

NLP: TF-IDF Vectorization

Model: Multinomial Naive Bayes

Frontend: HTML, CSS

Data Handling: Pandas

## 📂 Project Structure
email-spam-detector/
│

├── backend/

│   ├── app.py               # Flask backend

│   ├── model.pkl            # Trained ML model

│   └── vectorizer.pkl       # TF-IDF vectorizer

│
├── templates/

│   └── index.html           # Frontend UI

│

├── static/

│   └── style.css            # Styling

│
├── spam.csv                 # Dataset

├── train_model.py           # Model training script

├── requirements.txt

## ⚙️ How It Works

Email text is entered via the web interface

Text is transformed using TF-IDF Vectorization

Trained Naive Bayes model predicts:

  -Spam / Not Spam

  -Confidence score (%)

Result is displayed on the UI

## 📦 Installation & Setup

1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/email-spam-detector.git
cd email-spam-detector
```
2️⃣ Create Virtual Environment (Recommended)
```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
## 🧠 Train the Model

Run this once to generate model files:
```bash
python train_model.py
```
This will create:

model.pkl

vectorizer.pkl

## ▶️ Run the Application
```bash
python backend/app.py
```
Open in browser:
```bash
http://127.0.0.1:5000/
```
## 📈 Future Enhancements

🔐 User authentication

📁 Email file upload (.txt / .eml)

📊 Model comparison dashboard

☁️ Deployment on cloud platforms

🧪 API endpoint for predictions

## 🎯 Use Cases

Email filtering systems

Cybersecurity and phishing detection

NLP and ML learning projects

Resume & portfolio projects
