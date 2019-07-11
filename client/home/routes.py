from flask import render_template, request, jsonify

from . import bp, forms, controllers

methods = ['GET', 'POST']


@bp.route('/', methods=methods)
@bp.route('/index', methods=methods)
@bp.route('/home', methods=methods)
def index():
    form = forms.Base()
    if form.validate_on_submit():
        project = request.form.get('project')
        fix_version = request.form.get('fix_version')
        response = controllers.write_jira_data(project=project, fix_version=fix_version)
        return jsonify(response)
    return render_template('index.html', form=form)
