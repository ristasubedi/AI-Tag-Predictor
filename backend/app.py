from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import re

app = Flask(__name__)
CORS(app)

# 🔄 Load pre-trained model and transformers
model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')
mlb = joblib.load('mlb.pkl')
tag_explanations = joblib.load('tag_explanations.pkl')

# Load difficulty model + label encoder
difficulty_model = joblib.load('difficulty_model.pkl')
difficulty_encoder = joblib.load('difficulty_encoder.pkl')

# 🧹 Text cleaning function
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

# 📍 Prediction Route
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    question = data.get("question", "")
    cleaned = clean_text(question)
    question_vec = vectorizer.transform([cleaned])

    # Predict tags
    probs = model.predict_proba(question_vec)[0]
    top_k = probs.argsort()[-3:][::-1]
    tags = [mlb.classes_[i] for i in top_k if probs[i] > 0.1]

    explained_tags = [
        {
            "tag": tag,
            "explanation": tag_explanations.get(tag, {}).get("explanation", "No explanation available."),
            "link": tag_explanations.get(tag, {}).get("link", "#")
        }
        for tag in tags
    ]

    # Predict difficulty
    difficulty_pred = difficulty_model.predict(question_vec)
    difficulty = difficulty_encoder.inverse_transform(difficulty_pred)[0]


    return jsonify({
        "predicted_tags": explained_tags,
        "predicted_difficulty": difficulty
    })

if __name__ == '__main__':
    app.run(debug=True)
