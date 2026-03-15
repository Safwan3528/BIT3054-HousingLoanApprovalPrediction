from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import LoanApplication, Prediction, User
from app import db
import joblib
import os
import pandas as pd
from ml_model.preprocessing import preprocess_input

main_bp = Blueprint('main', __name__)

MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'ml_model', 'model.pkl')

@main_bp.route('/dashboard')
@login_required
def dashboard():
    if current_user.role == 'admin':
        return redirect(url_for('main.admin_dashboard'))
        
    user_apps = LoanApplication.query.filter_by(user_id=current_user.id).order_by(LoanApplication.created_at.desc()).all()
    approved_count = sum(1 for app in user_apps if app.prediction == 'Approved')
    rejected_count = sum(1 for app in user_apps if app.prediction == 'Rejected')
    
    return render_template('dashboard.html', 
                           applications=user_apps, 
                           approved=approved_count, 
                           rejected=rejected_count)

@main_bp.route('/loan_form', methods=['GET', 'POST'])
@login_required
def loan_form():
    if request.method == 'POST':
        # Retrieve form data
        income = float(request.form.get('income'))
        coapplicant_income = float(request.form.get('coapplicant_income'))
        loan_amount = float(request.form.get('loan_amount'))
        loan_term = float(request.form.get('loan_term'))
        credit_history = float(request.form.get('credit_history'))
        education = request.form.get('education')
        married = request.form.get('married')
        dependents = request.form.get('dependents')
        property_area = request.form.get('property_area')
        
        # Save application
        application = LoanApplication(
            user_id=current_user.id,
            income=income,
            coapplicant_income=coapplicant_income,
            loan_amount=loan_amount,
            loan_term=loan_term,
            credit_history=credit_history,
            education=education,
            married=married,
            dependents=dependents,
            property_area=property_area
        )
        db.session.add(application)
        db.session.commit()
        
        # ML Prediction
        try:
            model = joblib.load(MODEL_PATH)
            
            input_data = pd.DataFrame([{
                'ApplicantIncome': income,
                'CoapplicantIncome': coapplicant_income,
                'LoanAmount': loan_amount,
                'Loan_Amount_Term': loan_term,
                'Credit_History': credit_history,
                'Education': education,
                'Married': married,
                'Dependents': dependents,
                'Property_Area': property_area
            }])
            
            processed_data = preprocess_input(input_data)
            pred = model.predict(processed_data)[0]
            
            result = 'Approved' if pred == 1 else 'Rejected'
            
        except Exception as e:
            result = 'Error'
            
        application.prediction = result
        
        pred_record = Prediction(application_id=application.application_id, result=result)
        db.session.add(pred_record)
        db.session.commit()
        
        return redirect(url_for('main.result', id=application.application_id))
        
    return render_template('loan_form.html')

@main_bp.route('/result/<int:id>')
@login_required
def result(id):
    application = LoanApplication.query.get_or_404(id)
    if application.user_id != current_user.id and current_user.role != 'admin':
        flash("Unauthorized access", "danger")
        return redirect(url_for('main.dashboard'))
        
    return render_template('result.html', application=application)

@main_bp.route('/admin_dashboard')
@login_required
def admin_dashboard():
    if current_user.role != 'admin':
        flash('Access denied.', 'danger')
        return redirect(url_for('main.dashboard'))
        
    applications = LoanApplication.query.order_by(LoanApplication.created_at.desc()).all()
    return render_template('admin_dashboard.html', applications=applications)
