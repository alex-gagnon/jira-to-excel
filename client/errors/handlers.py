from flask import render_template

from . import bp


@bp.app_errorhandler(400)
def handle_400(e):
    return render_template('default_errors.html', error=e)


@bp.app_errorhandler(404)
def handle_400(e):
    return render_template('default_errors.html', error=e)


@bp.app_errorhandler(500)
def handle_500(e):
    return render_template('default_errors.html', error=e)
