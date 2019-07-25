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
    DEBUG = False
    TESTING = False

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my_secret_key_here'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URI') or 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    user = os.environ.get('JIRA_USER')
    password = os.environ.get('JIRA_PASSWORD')
    server = os.environ.get('JIRA_SERVER')


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    Debug = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
