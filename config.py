import os
from dotenv import load_dotenv

load_dotenv()
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_very_secret_key'
    # Fallback to sqlite for simple testing if DATABASE_URL isn't set, although PostgreSQL is required.
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///housing_loan_db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
