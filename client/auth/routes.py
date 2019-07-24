from flask import render_template, request, url_for, redirect, flash
from werkzeug.security import generate_password_hash

from client import db
from client.models import User
from . import bp, forms


@bp.route('/login', methods=('GET', 'POST'))
def login():
    form = forms.Auth()
    if form.validate_on_submit():
        pass
    return render_template(template_name_or_list='login.html',
                           form=form,
                           title='Login')


@bp.route('/signup')
def signup():
    form = forms.Auth()
    return render_template(template_name_or_list='signup.html',
                           form=form,
                           title='Signup')


@bp.route('/signup', methods=['POST'])
def signup_post():
    name = request.form.get('username')
    password = request.form.get('password')

    username = User.query.filter_by(username=name).first()

    if username:
        flash('Username already in use')
        return redirect(url_for('auth.signup'))

    new_user = User(username=name, password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@bp.route('/logout')
def logout():
    return 'Logout'
