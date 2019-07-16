import pytest

from config import Config
from services import JiraProjectIssues

project_and_fix_version = (
    ("TM", "10.2"),
    ("TM", "10.3"),
    ("TM", "10.4"),
)


class TestJiraProjectIssues:
    @pytest.mark.parametrize("project, fix_version", project_and_fix_version)
    def test_class(self, project, fix_version):
        response = JiraProjectIssues(url=Config.server,
                                     username=Config.user,
                                     password=Config.password,
                                     project=project)
        assert response.project == project
        assert repr(response) == f'JiraProjectIssues(url="{Config.server}", project="{project}")'

    @pytest.mark.parametrize("project, fix_version", project_and_fix_version)
    def test_filter_by_fix_version(self, project, fix_version):
        response = JiraProjectIssues(url=Config.server,
                                     username=Config.user,
                                     password=Config.password,
                                     project=project)
        filtered = response.filter_by_fix_version(fix_version=fix_version)
        assert response.project_issues()
        assert filtered
        assert response.detailed_filter_by_fix_version(filtered)

    @pytest.mark.parametrize("project, latest_version", (
            ("CUST", "10.1"),
            ("CUST", "10.2"),
            ("CUST", "10.3")
    ))
    def test_filter_by_latest_build(self, project, latest_version):
        response = JiraProjectIssues(url=Config.server,
                                     username=Config.user,
                                     password=Config.password,
                                     project=project)
        filtered = response.filter_by_latest_version_delivered(latest_version=latest_version)
        print(filtered)
