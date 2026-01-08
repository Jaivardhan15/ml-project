from flask import Flask, render_template, request
import pickle
import os

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "model.pkl"), "rb") as f:
    model = pickle.load(f)

with open(os.path.join(BASE_DIR, "vectorizer.pkl"), "rb") as f:
    vectorizer = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    confidence = None     
    email_text = ""

    if request.method == "POST":
        email_text = request.form.get("message")

        if email_text and email_text.strip():
            data = vectorizer.transform([email_text])
            proba = model.predict_proba(data)[0]
            label = model.predict(data)[0]

            if label == 1:
                prediction = "🚨 Spam Email"
                confidence = round(proba[1] * 100, 2)
            else:
                prediction = "✅ Not Spam"
                confidence = round(proba[0] * 100, 2)

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        email_text=email_text
    )

if __name__ == "__main__":
    app.run(debug=True)
