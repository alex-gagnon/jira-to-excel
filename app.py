from flask import Flask
from werkzeug.exceptions import NotFound
from werkzeug.middleware.dispatcher import DispatcherMiddleware

from backend import app as backend
from client import create_app

application = Flask(__name__)
frontend = create_app()
application.wsgi_app = DispatcherMiddleware(NotFound(), {
    '': frontend,
    '/auth': backend
})

if __name__ == '__main__':
    application.run()
