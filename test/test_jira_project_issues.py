import pytest

from jira_scripts.jira_project_issues import JiraProjectIssues

project_and_fix_version = (
    ("project1", "fix_version"),
)


class TestJiraProjectIssues:
    @pytest.mark.parametrize("project, fix_version", project_and_fix_version)
    def test_without_connection(self, project, fix_version):
        response = JiraProjectIssues(project=project, fix_version=fix_version)
        assert response.project == project
        assert response.fix_version == fix_version
        assert response.__repr__() == f'<Jira Scrape Object: project="{project}"", fix_version="{fix_version}">'

    @pytest.mark.parametrize("project, fix_version", project_and_fix_version)
    def test_with_connection(self, project, fix_version):
        response = JiraProjectIssues(project=project, fix_version=fix_version)
        jira_cnx = response.auth_jira()
        assert jira_cnx
        assert response.project_issues()
        assert response.filter_by_fix_version()
