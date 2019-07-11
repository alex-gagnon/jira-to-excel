import pytest

from scripts.jira_scripts.jira_project_issues import JiraProjectIssues

project_and_fix_version = (
    ("TM", "10.4"),
)


class TestJiraProjectIssues:
    @pytest.mark.parametrize("project, fix_version", project_and_fix_version)
    def test_without_connection(self, project, fix_version):
        response = JiraProjectIssues(project=project, fix_version=fix_version)
        assert response.project == project
        assert response.fix_version == fix_version
        assert response.__repr__() == f'<JiraProjectIssues Object: project="{project}", fix_version="{fix_version}">'

    @pytest.mark.parametrize("project, fix_version", project_and_fix_version)
    def test_with_connection(self, project, fix_version):
        response = JiraProjectIssues(project=project, fix_version=fix_version)
        jira_cnx = response.auth_jira()
        filtered = response.filter_by_fix_version()
        assert jira_cnx
        assert response.project_issues()
        assert filtered
        assert response.detailed_filter_by_fix_version(filtered)
