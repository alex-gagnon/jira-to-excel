from config import FILE_PATH
from excel_scripts import CreateExcelFile
from jira_scripts import JiraProjectIssues


def write_jira_data(*args, **kwargs):
    project = kwargs.get('project')
    fix_version = kwargs.get('fix_version')
    filename = f'{project} {fix_version}'
    excel = CreateExcelFile(filename=filename, sheetname=fix_version)
    init_jira = JiraProjectIssues(project=project, fix_version=fix_version)
    init_jira.auth_jira()
    fix_version_issues = init_jira.filter_by_fix_version()
    detailed_issues = init_jira.detailed_filter_by_fix_version(fix_version_issues)
    excel.create_excel_book(data_list=detailed_issues)
    latest_file = excel.get_recent_file()
    print(FILE_PATH)
    return {"Successful": 200, "directory": FILE_PATH, "filename": latest_file}


if __name__ == '__main__':
    p = 'TM'
    f = '10.4'
    write_jira_data(project=p, fix_version=f)
