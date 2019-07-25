from flask import Flask, request, flash, redirect, url_for
from flask_login import login_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

from backend.models import User


@app.route('/login', methods=['POST'])
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


@app.route('/signup', methods=['POST'])
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
