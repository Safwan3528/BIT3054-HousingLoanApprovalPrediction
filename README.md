# 🏠 AI-Powered Malaysian Housing Loan Approval Prediction System

**Course:** BIT3054 - Data Science  
**Prediction Type:** Binary Classification — `Approved (1)` / `Rejected (0)`

---

## 📌 Project Goal

A full-stack intelligent web system for **Housing Loan Analysts and Property Agents** to instantly predict client loan approval probability using machine learning. The system also provides AI-powered financial insights, maximum property price recommendations, and bank-matching for rejected applicants.

---

## 🛠️ Tech Stack

| Layer | Technology |
|:---|:---|
| **Backend** | Python 3, Flask |
| **Machine Learning** | Scikit-learn, XGBoost, Pandas, NumPy, Matplotlib, Seaborn |
| **Database** | MongoDB (NoSQL) via MongoEngine — MongoDB Atlas in production |
| **Frontend UI** | HTML5, Bootstrap 5, Jinja2 |
| **Deployment** | Render.com (connected to GitHub for CI/CD) |

---

## 🚀 Setup & Run Locally

```bash
# 1. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 2. Install all dependencies
pip install -r requirements.txt

# 3. Train the ML model (generates model.pkl)
python ml_model/train_model.py

# 4. Run the Flask development server
python run.py
```

> **Note:** The app uses **MongoDB Atlas** in production. For local development, it automatically falls back to `mongomock` (no local MongoDB installation required).

---

## 🤖 Machine Learning Models

- **Baseline:** Logistic Regression (`max_iter=1000`)
- **Improved:** Random Forest Classifier (`n_estimators=100, random_state=42`)
- **Advanced:** XGBoost / HistGradientBoosting (fallback)
- **Train/Test Split:** 80:20 on 5,000 simulated Malaysian bank records
- **Key Metrics (Random Forest):** Accuracy: 71.8% | F1: 0.7427 | AUC-ROC: 0.7706

---

## 👥 Role-Based Access

| Role | Capabilities |
|:---|:---|
| **Admin** | Manage users, upload dataset, clean data, retrain ML model, view evaluation plots |
| **User (Agent)** | Submit loan assessment form, view prediction + AI insights, view history |

---

## 📁 Project Structure

```
├── app/                    # Flask routes, auth, models (MongoEngine)
├── ml_model/
│   ├── train_model.py      # ML training script
│   ├── evaluate_model.py   # Evaluation metrics
│   ├── generate_plots.py   # Matplotlib/Seaborn chart generation
│   ├── preprocessing.py    # Feature engineering pipeline
│   └── loan_data.csv       # Simulated Malaysian loan dataset (5,000 records)
├── static/                 # CSS, plots
├── templates/              # Jinja2 HTML pages
├── generate_realistic_data.py  # Dataset simulation script
├── config.py               # MongoDB Atlas configuration
└── run.py                  # App entry point
```
