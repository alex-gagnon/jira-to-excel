import pytest

from excel_scripts.create_excel_file import CreateExcelFile

args = (
    ("TM", "10.4", [{'Col 1': 'data 1', 'Col 2': "data 2", 'Col 3': "data 3"},
                    {'Col 1': 'data 4', 'Col 2': "data 5", 'Col 3': "data 6"}]),
)


class TestJiraProjectIssues:
    @pytest.mark.parametrize("project, fix_version, data_list", args)
    def test_excel_object(self, project, fix_version, data_list):
        response = CreateExcelFile(filename=project + " " + fix_version, sheetname=fix_version)
        assert response.filename == f'{project} {fix_version}'
        response.create_excel_book(data_list=data_list)
