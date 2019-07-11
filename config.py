import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my_secret_key_here'
    DEBUG = True

    user = os.environ.get('JIRA_USER')
    password = os.environ.get('JIRA_PASSWORD')
    server = os.environ.get('JIRA_SERVER')
