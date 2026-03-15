import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib
import os
from preprocessing import preprocess_training_data

def train_and_save():
    base_dir = os.path.dirname(__file__)
    data_path = os.path.join(base_dir, 'loan_data.csv')
    
    if os.path.exists(data_path):
        df = pd.read_csv(data_path)
    else:
        print("Dataset not found. Generating dummy housing loan data for demonstration...")
        np.random.seed(42)
        n = 600
        df = pd.DataFrame({
            'Loan_ID': [f'LP00{i}' for i in range(n)],
            'Gender': np.random.choice(['Male', 'Female'], n),
            'Married': np.random.choice(['Yes', 'No'], n),
            'Dependents': np.random.choice(['0', '1', '2', '3+'], n),
            'Education': np.random.choice(['Graduate', 'Not Graduate'], n),
            'Self_Employed': np.random.choice(['No', 'Yes'], n),
            'ApplicantIncome': np.random.randint(2000, 20000, n),
            'CoapplicantIncome': np.random.randint(0, 10000, n),
            'LoanAmount': np.random.randint(50, 500, n),
            'Loan_Amount_Term': np.random.choice([120, 240, 360, 480], n),
            'Credit_History': np.random.choice([0.0, 1.0], n, p=[0.2, 0.8]),
            'Property_Area': np.random.choice(['Urban', 'Rural', 'Semiurban'], n),
            'Loan_Status': np.random.choice(['Y', 'N'], n, p=[0.7, 0.3])
        })
        df.to_csv(data_path, index=False)

    print("Preprocessing data...")
    X, y = preprocess_training_data(df)
    
    print("Training RandomForestClassifier...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    save_path = os.path.join(base_dir, 'model.pkl')
    joblib.dump(model, save_path)
    print(f"Model saved to {save_path}")

if __name__ == '__main__':
    train_and_save()
