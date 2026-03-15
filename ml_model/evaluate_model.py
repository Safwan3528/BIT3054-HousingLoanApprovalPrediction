import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import os
from preprocessing import preprocess_training_data

def evaluate():
    base_dir = os.path.dirname(__file__)
    data_path = os.path.join(base_dir, 'loan_data.csv')
    
    if not os.path.exists(data_path):
        print("Dataset not found. Run train_model.py first to generate or place dataset.")
        return
        
    df = pd.read_csv(data_path)
    X, y = preprocess_training_data(df)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    print("--- Model Evaluation Metrics ---")
    print(f"Accuracy:  {accuracy_score(y_test, y_pred):.4f}")
    print(f"Precision: {precision_score(y_test, y_pred):.4f}")
    print(f"Recall:    {recall_score(y_test, y_pred):.4f}")
    print(f"F1 Score:  {f1_score(y_test, y_pred):.4f}")
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

if __name__ == '__main__':
    evaluate()
