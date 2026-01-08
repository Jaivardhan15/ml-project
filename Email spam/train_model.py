import pandas as pd
import pickle
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load dataset
df = pd.read_csv("spam.csv", encoding="latin-1")

# Keep first two columns only
df = df.iloc[:, :2]
df.columns = ["label", "message"]

# Encode labels
df["label"] = df["label"].map({"ham": 0, "spam": 1})

# Vectorization
vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(df["message"])
y = df["label"]

# ✅ MODEL IS DEFINED HERE
model = MultinomialNB()

# ✅ MODEL IS TRAINED HERE
model.fit(X, y)

# Ensure backend folder exists
os.makedirs("backend", exist_ok=True)

# Save model and vectorizer
with open("backend/model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("backend/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Model and vectorizer saved successfully")
