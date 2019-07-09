from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return 'Hello'


if __name__ == '__main__':
    app.run()
