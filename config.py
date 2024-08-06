from dotenv import load_dotenv
import os

load_dotenv()
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecret')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///recipes.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
