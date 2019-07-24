from flask import Blueprint

bp = Blueprint('auth', __name__)

from client.auth import routes, forms
