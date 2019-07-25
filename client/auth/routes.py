from flask import render_template, request, url_for, redirect, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash

from client.models import User
from . import bp, forms


@bp.route('/login')
def login():
    form = forms.Auth()
    return render_template(template_name_or_list='login.html',
                           form=form,
                           title='Login')


@bp.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        flash('Invalid username/password')
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)
    return redirect(url_for('home.jxl'))


"""Uncomment if a new user needs to be added. otherwise,
this route should not be enabled."""


@bp.route('/signup')
def signup():
    form = forms.Auth()
    return render_template(template_name_or_list='signup.html',
                           form=form,
                           title='Signup')
#
#
# @bp.route('/signup', methods=['POST'])
# def signup_post():
#     name = request.form.get('username')
#     password = request.form.get('password')
#
#     username = User.query.filter_by(username=name).first()
#
#     if username:
#         flash('Username already in use')
#         return redirect(url_for('auth.signup'))
#
#     new_user = User(username=name, password=generate_password_hash(password, method='sha256'))
#
#     db.session.add(new_user)
#     db.session.commit()
#
#     return redirect(url_for('auth.login'))


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
