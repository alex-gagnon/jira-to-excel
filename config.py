import os

PROJECT_PATH = os.path.dirname(__file__)
FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets')


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my_secret_key_here'
    DEBUG = True

    user = os.environ.get('JIRA_USER')
    password = os.environ.get('JIRA_PASSWORD')
    server = os.environ.get('JIRA_SERVER')
