import os
from dotenv import load_dotenv

load_dotenv()
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_very_secret_key'
    MONGODB_SETTINGS = {
        'host': os.environ.get('MONGO_URI') or 'mongodb://localhost:27017/housing_loan_db'
    }
