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
        print(f'JiraProjectIssues Object values redefined... Project= {self.project}')

    def __repr__(self):
        return f'JiraProjectIssues(url="{self.url}", project="{self.project}")'

    def __str__(self):
        return f'Project "{self.project}"'

    def project_issues(self) -> list:
        return self.cnx.search_issues(f'project={self.project}')

    def filter_by_fix_version(self, fix_version) -> list:
        return [list_issues for list_issues in self.project_issues()
                for issues in list_issues.fields.fixVersions
                if issues.name == fix_version]

    def detailed_filter_by_fix_version(self, issue_list) -> [dict]:
        detailed_info = [{
            'Jira Case': issue.key,
            'Description': issue.fields.summary,
            'Sprint': self.get_sprint(issue=issue)
        } for issue in issue_list]

        return detailed_info

    def filter_by_latest_version_delivered(self, latest_version):
        return [{'Jira Case': list_issues.key,
                 'Description': list_issues.fields.summary,
                 'Latest Version': list_issues.fields.customfield_10911}
                for list_issues in self.project_issues()
                if list_issues.fields.customfield_10911 is not None
                and re.findall(r"{0}(.*)".format(latest_version), list_issues.fields.customfield_10911)]

    @staticmethod
    def get_sprint(issue):
        return [issue_sprint.replace('name=', '')
                # customfield must match element id in jira
                for issue_sprint in re.findall(r"name=[^,]*", str(issue.fields.customfield_10000))]

    @staticmethod
    def get_latest_version(issue):
        return [issue_version for issue_version in str(issue.fields["custom_field_10911-val"])]
