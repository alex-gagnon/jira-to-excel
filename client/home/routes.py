from flask import render_template, request, send_from_directory

from . import bp, forms, controllers

methods = ['GET', 'POST']


@bp.route('/', methods=methods)
@bp.route('/index', methods=methods)
@bp.route('/home', methods=methods)
def index():
    form = forms.Base()
    if form.validate_on_submit():
        project = request.form.get('project')
        version = request.form.get('version')
        filter_by = request.form.get('filter_by')

        response = controllers.get_jira_data(project=project, version=version, filter_by=filter_by)
        return send_from_directory(directory=response.get("directory"), filename=response.get("filename"))
    return render_template('index.html', form=form)
