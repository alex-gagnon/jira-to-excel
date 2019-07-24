import os

PROJECT_PATH = os.path.dirname(__file__)
FILE_PATH = os.path.dirname(os.path.abspath(__file__))
assets = 'assets'
try:
    os.stat(os.path.join(FILE_PATH, assets))
except FileNotFoundError:
    os.mkdir(os.path.join(FILE_PATH, assets))
finally:
    FILE_PATH = os.path.join(FILE_PATH, assets)


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my_secret_key_here'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    user = os.environ.get('JIRA_USER')
    password = os.environ.get('JIRA_PASSWORD')
    server = os.environ.get('JIRA_SERVER')
