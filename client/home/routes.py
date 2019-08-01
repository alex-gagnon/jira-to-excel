from flask import render_template, request, send_from_directory, redirect, url_for
from flask_login import login_required

from . import bp, forms, controllers

methods = ['GET', 'POST']


@bp.route('/', methods=methods)
@bp.route('/index', methods=methods)
def index():
    return redirect(url_for('home.jxl'))


@bp.route('/jxl', methods=methods)
def jxl():
    form = forms.Base()
    if form.validate_on_submit():
        project = request.form.get('project')
        version = request.form.get('version')
        filter_by = request.form.get('filter_by')

        response = controllers.get_jira_data(project=project,
                                             version=version,
                                             filter_by=filter_by)
        return send_from_directory(directory=response.get("directory"),
                                   filename=response.get("filename"),
                                   as_attachment=True)
    return render_template(template_name_or_list='index.html',
                           title='JXL',
                           form=form)
