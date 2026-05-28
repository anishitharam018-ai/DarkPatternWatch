# 🔍 DarkPatternWatch — Multi-class NLP Dark Pattern Classifier

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Accuracy](https://img.shields.io/badge/Accuracy-97.5%25-brightgreen)
![Streamlit](https://img.shields.io/badge/Deployed-Streamlit-red)
![Dataset](https://img.shields.io/badge/Dataset-400%2B%20examples-orange)
![Status](https://img.shields.io/badge/Status-Live-success)

> Paste any website text and instantly find out if it's manipulating you.

---

## 🎯 What is this?

Websites use psychological tricks called **dark patterns** to manipulate users into
doing things they didn't intend — subscribing, paying hidden fees, or staying
trapped in services they want to leave.

**DarkPatternWatch** is an NLP-powered classifier that detects 5 types of dark
patterns in real-time from raw text input.

---

## 🧠 Dark Pattern Categories

| Category           | Description                    | Example                                              |
| ------------------ | ------------------------------ | ---------------------------------------------------- |
| ⏰ False Urgency   | Fake scarcity or time pressure | _"Only 2 left in stock!"_                            |
| 😔 Confirmshaming  | Guilt-trips you into accepting | _"No thanks, I hate saving money."_                  |
| 💸 Hidden Costs    | Fees hidden until checkout     | _"Service fee added at checkout."_                   |
| 🔀 Trick Questions | Confusing double negatives     | _"Uncheck if you don't want to not receive emails."_ |
| 🪤 Roach Motel     | Easy in, hard to leave         | _"Cancellation requires calling our support line."_  |

---

## 📊 Model Performance

| Metric            | Score                           |
| ----------------- | ------------------------------- |
| Accuracy          | **97.5%**                       |
| Macro F1          | **0.97**                        |
| Training Examples | **400+**                        |
| Classes           | **6** (5 dark patterns + clean) |

---

## 🏗️ How It Works

Raw Text Input
↓
TF-IDF Vectorizer (bigrams, 5000 features)
↓
Logistic Regression Classifier
↓
Predicted Category + Confidence Score

---

## 🛠️ Tech Stack

- **Language:** Python 3.12
- **ML:** Scikit-learn (TF-IDF + Logistic Regression)
- **NLP:** TF-IDF bigrams + regex-based feature engineering
- **Dataset:** 400+ manually annotated real-world examples
- **Deployment:** Streamlit web app
- **Serialization:** Pickle (model + vectorizer)

---

## 🚀 Run Locally

```bash
# Clone the repo
git clone https://github.com/anishitharam018-ai/DarkPatternWatch.git
cd DarkPatternWatch

# Install dependencies
pip install pandas scikit-learn streamlit

# Train the model
python dataset.py
python expand_data.py
python model.py

# Launch the app
streamlit run app.py
```

---

## 📁 Project Structure

DarkPatternWatch/
├── app.py # Streamlit web app
├── model.py # Model training + evaluation
├── dataset.py # Base dataset (60 examples)
├── expand_data.py # Dataset expansion (400+ examples)
├── darkpatterns.csv # Full labeled dataset
├── model.pkl # Trained classifier
├── vectorizer.pkl # Fitted TF-IDF vectorizer
└── README.md # You are here

---

## 💡 Key ML Concepts Demonstrated

- End-to-end ML pipeline from raw data to deployment
- Custom dataset curation and manual annotation
- TF-IDF bigram feature engineering
- Multi-class text classification
- Model serialization and loading
- Interactive web app deployment

---

## 👩‍💻 Author

**Pathakota Sri Anishitha Rani**  
B.Tech CSE | Geethanjali Institute of Science and Technology  
[GitHub](https://github.com/anishitharam018-ai)
[LinkedIn](https://www.linkedin.com/in/anishitharam/)
