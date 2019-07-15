from flask import Flask

from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from client.errors import bp as error_bp
    app.register_blueprint(error_bp)

    from client.home import bp as home_bp
    app.register_blueprint(home_bp)

    return app
