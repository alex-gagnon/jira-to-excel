from excel_scripts.create_excel_file import CreateExcelFile
from jira_scripts.jira_project_issues import JiraProjectIssues


def write_jira_data(project, fix_version):
    filename = f'{project} {fix_version}'
    excel = CreateExcelFile(filename=filename, sheetname=fix_version)
    init_jira = JiraProjectIssues(project=project, fix_version=fix_version)
    init_jira.auth_jira()
    fix_version_issues = init_jira.filter_by_fix_version()
    detailed_issues = init_jira.detailed_filter_by_fix_version(fix_version_issues)
    excel.create_excel_book(data_list=detailed_issues)


if __name__ == '__main__':
    p = 'TM'
    f = '10.4'
    write_jira_data(project=p, fix_version=f)
