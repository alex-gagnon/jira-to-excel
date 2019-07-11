from flask import render_template

from . import bp, forms


@bp.route('/')
@bp.route('/index')
@bp.route('/home')
def index():
    form = forms.Base()
    return render_template('index.html', form=form)
