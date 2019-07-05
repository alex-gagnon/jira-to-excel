from jira import JIRA

from config import Config


class JiraProjectIssues(Config):

    def __init__(self, *args, **kwargs):
        self.args = args
        self.project = kwargs.get('project')
        self.fix_version = kwargs.get('fix_version')

    def __repr__(self):
        return f'<Jira Scrape Object: project="{self.project}"", fix_version="{self.fix_version}">'

    def __str__(self):
        return f''

    def auth_jira(self):
        options = {
            'server': self.server
        }
        return JIRA(options, auth=(self.user, self.password))

    def project_issues(self) -> list:
        jira = self.auth_jira()
        return jira.search_issues(f'project={self.project}')

    def filter_by_fix_version(self) -> list:
        return [list_issues for list_issues in self.project_issues()
                for issues in list_issues.fields.fixVersions
                if issues.name == self.fix_version]
