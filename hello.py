from flask import Flask, url_for
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/hello/')
def hello():
    return 'hello'

@app.route('/hello/<name>/')
def hello_with_name(name):
    return 'hello %s' % name

@app.route('/which/hello/')
def which_hello():
    return url_for('hello')


def do_the_login():
    return 'login do'

def show_the_login_form():
    return 'enter credentials'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

@app.route('/hello2/')
@app.route('/hello2/<name>')
def hello_with_template(name=None):
    return render_template('hello.html', name=name)

