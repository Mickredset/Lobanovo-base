import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'lobanovo-secret-key-2024'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///lobanovo.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10MB limit
