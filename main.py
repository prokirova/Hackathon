from flask import Flask, render_template, request, redirect, url_for

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

if __name__ == '__main__':
    app.run()