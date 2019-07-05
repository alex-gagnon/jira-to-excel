import os


class Config:
    user = os.environ.get('JIRA_USER')
    password = os.environ.get('JIRA_PASSWORD')
    server = os.environ.get('JIRA_SERVER')
