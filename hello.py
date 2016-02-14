# -*- coding: utf-8 -*-
# __author__ = 'Fakegit'

from flask import Flask, request
from flask.ext.script import Manager

app = Flask(__name__)
manager = (app)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s.' % user_agent
    
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello %s!</h1>' % name

if __name__ == '__main__':
    manager.run(debug=True)