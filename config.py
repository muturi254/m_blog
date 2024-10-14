import os

# configurations
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'