# 🧠 AI Tag Prediction Web App

This project is a **full-stack web application** that predicts **programming topic tags** (e.g., `python`, `machine-learning`, `algorithms`) from user-input questions.  
It uses **multi-label Logistic Regression** trained on text data, achieving **85%+ accuracy**.  

Users can enter a programming-related question, and the app predicts relevant tags along with explanations and helpful external links.

---

## 🚀 Features
- Multi-label classification of programming questions.
- TF-IDF vectorization for feature extraction.
- Logistic Regression for prediction.
- Web app interface for interactive use.
- Tag explanations + external learning resources.

---

## 🛠️ Tech Stack
- **Frontend:** HTML / CSS / JavaScript (or React, if applicable)
- **Backend:** Flask / FastAPI (depending on your setup)
- **ML Model:** Scikit-learn (TF-IDF + Logistic Regression)
- **Deployment:** (Heroku / Render / Localhost — specify if you deployed)

---

## 📖 Notebook
You can explore the model training and evaluation in the Colab notebook below:

👉 [Open in Google Colab](https://colab.research.google.com/drive/1V1thiJyv3Arc8oHCzjQ5kBptmo1bVCcq?usp=sharing)

---

## ⚙️ Setup Instructions

1. **Clone the Repository**
    ```bash
    git clone https://github.com/ristasubedi/AI-Tag-Predictor.git
    cd AI-Tag-Predictor
    ```

2. **Create a Virtual Environment** (optional but recommended)
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # Mac/Linux
    venv\Scripts\activate      # Windows
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the App**
    ```bash
    python app.py
    ```
    Then open `http://127.0.0.1:5000/` in your browser.

---

## 📊 Model Performance
- **Algorithm:** Logistic Regression  
- **Vectorization:** TF-IDF  
- **Accuracy:** 85%+ (multi-label prediction)  


---

## 👩‍💻 Author
**Rista Subedi**  
- 🌐 [GitHub](https://github.com/ristasubedi)  

---
