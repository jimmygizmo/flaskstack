from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>REST API & Data Manager App (Python) - The Nucleus Stack</h1>'


@app.route('/vehicle/<vin>')
def user(vin):
    return f"<h1>Vehicle with VIN#: {vin}</h1>"

