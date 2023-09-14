import os
from flask import Flask, render_template, request, redirect, url_for

DEBUG = int(os.environ.get("DEBUG", 1))
PORT = os.environ.get("PORT", 12345)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('page.html')

@app.route('/start')
def start():
    return render_template('start.html')

@app.route('/factory')
def factory():
    return render_template('factory.html')

@app.route('/cathedral')
def cathedral():
    return render_template('cathedral.html')

@app.route('/houseoflat')
def houseoflat():
    return render_template('houseoflat.html')

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT, host='0.0.0.0')