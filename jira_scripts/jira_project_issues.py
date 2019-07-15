import re

from jira import JIRA


class JiraProjectIssues:

    def __init__(self, *args, **kwargs):
        self.args = args
        self.url = kwargs.get('url')
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')
        self.project = kwargs.get('project')
        self.fix_version = kwargs.get('fix_version')

        options = {'server': self.url}
        self.cnx = JIRA(options=options, auth=(self.username, self.password))

    def __call__(self, *args, **kwargs):
        self.args = args
        self.url = kwargs.get('url')
        self.project = kwargs.get('project')
        self.fix_version = kwargs.get('fix_version')
        print(f'JiraProjectIssues Object values redefined... Project= {self.project}, Fix Version= {self.fix_version}')

    def __repr__(self):
        return f'JiraProjectIssues(url="{self.url}", project="{self.project}", fix_version="{self.fix_version}")'

    def __str__(self):
        return f'Project "{self.project}", Fix Version "{self.fix_version}"'

    def project_issues(self) -> list:
        return self.cnx.search_issues(f'project={self.project}')

    def filter_by_fix_version(self) -> list:
        return [list_issues for list_issues in self.project_issues()
                for issues in list_issues.fields.fixVersions
                if issues.name == self.fix_version]

    def detailed_filter_by_fix_version(self, issue_list) -> [dict]:
        detailed_info = [{
            'Jira Case': issue.key,
            'Description': issue.fields.summary,
            'Sprint': self.get_sprint(issue=issue)
        } for issue in issue_list]

        return detailed_info

    @staticmethod
    def get_sprint(issue):
        return [issue_sprint.replace('name=', '')
                # customfield must match element id in jira
                for issue_sprint in re.findall(r"name=[^,]*", str(issue.fields.customfield_10000))]
