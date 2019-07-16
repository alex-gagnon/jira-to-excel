from config import FILE_PATH, Config
from services import CreateExcelFile, JiraProjectIssues


def write_data(project, version, issues):
    filename = f'{project} {version}'
    excel = CreateExcelFile(filename=filename,
                            sheetname=version)
    excel.create_excel_book(data_list=issues)
    latest_file = excel.get_recent_file()

    return latest_file


def get_jira_data(*args, **kwargs):
    project = kwargs.get('project')
    version = kwargs.get('version')
    filter_by = kwargs.get('filter_by')

    init_jira = JiraProjectIssues(url=Config.server,
                                  username=Config.user,
                                  password=Config.password,
                                  project=project)

    filter_function = {'fix_version': by_fix_version,
                       'latest_version': by_latest_version}

    issues = filter_function[filter_by](init_jira, version)

    latest_file = write_data(project=project, version=version, issues=issues)

    return {"Successful": 200, "directory": FILE_PATH, "filename": latest_file}


def by_fix_version(j, version):
    fix_version_issues = j.filter_by_fix_version(fix_version=version)
    detailed_issues = j.detailed_filter_by_fix_version(fix_version_issues)
    print(FILE_PATH)
    return detailed_issues


def by_latest_version(j, version):
    return j.filter_by_latest_version_delivered(latest_version=version)


if __name__ == '__main__':
    p = 'TM'
    f = '10.4'
    get_jira_data(project=p, fix_version=f)
