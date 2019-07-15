from flask import Blueprint

bp = Blueprint('home', __name__)

from client.home import routes, forms, controllers
