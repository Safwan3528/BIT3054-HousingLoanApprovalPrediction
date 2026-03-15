from app import db
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='user')
    
    applications = db.relationship('LoanApplication', backref='applicant', lazy=True)

class LoanApplication(db.Model):
    __tablename__ = 'loan_applications'
    application_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    income = db.Column(db.Float, nullable=False)
    coapplicant_income = db.Column(db.Float, nullable=False)
    loan_amount = db.Column(db.Float, nullable=False)
    loan_term = db.Column(db.Float, nullable=False)
    credit_history = db.Column(db.Float, nullable=False)
    education = db.Column(db.String(50), nullable=False)
    married = db.Column(db.String(10), nullable=False)
    dependents = db.Column(db.String(10), nullable=False)
    property_area = db.Column(db.String(50), nullable=False)
    prediction = db.Column(db.String(50), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    prediction_details = db.relationship('Prediction', backref='application', lazy=True)

class Prediction(db.Model):
    __tablename__ = 'predictions'
    id = db.Column(db.Integer, primary_key=True)
    application_id = db.Column(db.Integer, db.ForeignKey('loan_applications.application_id'), nullable=False)
    result = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
