# Housing Loan Approval Prediction System

This is a student data science project for the course BIT3054 Data Science.

## Goal
Build a web system that predicts whether a housing loan application should be Approved or Rejected using a machine learning model.

## Tech Stack
- Python, Flask
- Scikit-learn, Pandas, NumPy
- Bootstrap (UI)
- PostgreSQL (database)

## Setup
1. Create a virtual environment and install dependencies: `pip install -r requirements.txt`
2. Initialize database with `database/schema.sql` (Assume PostgreSQL is set up).
3. Train the model: `python ml_model/train_model.py`
4. Run the application: `python run.py`
