import re

from jira import JIRA

from config import Config


class JiraProjectIssues(Config):

    def __init__(self, *args, **kwargs):
        self.args = args
        self.project = kwargs.get('project')
        self.fix_version = kwargs.get('fix_version')

    def __call__(self, *args, **kwargs):
        self.args = args
        self.project = kwargs.get('project')
        self.fix_version = kwargs.get('fix_version')
        print(f'JiraProjectIssues Object values redefined... Project= {self.project}, Fix Version= {self.fix_version}')

    def __repr__(self):
        return f'<JiraProjectIssues Object: project="{self.project}", fix_version="{self.fix_version}">'

    def __str__(self):
        return f'Project "{self.project}", Fix Version "{self.fix_version}"'

    def auth_jira(self):
        options = {
            'server': self.server
        }
        return JIRA(options=options, auth=(self.user, self.password))

    def project_issues(self) -> list:
        jira = self.auth_jira()
        return jira.search_issues(f'project={self.project}')

    def filter_by_fix_version(self) -> list:
        return [list_issues for list_issues in self.project_issues()
                for issues in list_issues.fields.fixVersions
                if issues.name == self.fix_version]

    @staticmethod
    def detailed_filter_by_fix_version(issue_list) -> [dict]:
        detailed_info = []
        for issue in issue_list:
            detailed_info.append({
                'Jira Case': issue.key,
                'Description': issue.fields.summary,
                'Sprint': [i.replace('name=', '') for i in
                           re.findall(r"name=[^,]*",
                                      str(issue.fields.customfield_10000))]  # customfield must match element id in jira
            })
        return detailed_info
