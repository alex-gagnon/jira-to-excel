from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    from client.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from client.errors import bp as error_bp
    app.register_blueprint(error_bp)

    from client.home import bp as home_bp
    app.register_blueprint(home_bp)

    return app
