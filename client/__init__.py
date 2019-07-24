from flask import Flask
from flask_login import LoginManager
from flask_nav import Nav
from flask_nav.elements import *
from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()
nav = Nav()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    navbar = Navbar('', View('Login', 'auth.login'))
    secnavbar = Navbar('', View('Logout', 'auth.logout'))
    nav.register_element('navbar', navbar)
    nav.register_element('secnavbar', secnavbar)

    nav.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from client.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from client.errors import bp as error_bp
    app.register_blueprint(error_bp)

    from client.home import bp as home_bp
    app.register_blueprint(home_bp)

    return app
