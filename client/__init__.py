from flask import Flask

from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from client.home import bp as home_bp
    app.register_blueprint(home_bp)

    return app
