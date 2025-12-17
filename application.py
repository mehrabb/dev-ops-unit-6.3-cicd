from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello():
    return '<h1>Hello World! from the Development Server!</h1>'
