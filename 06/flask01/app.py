from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hola Mundo!</h1>'


@app.route('/about')
def about():
    return '<p style="background-color:red"> Hola mi nombre es  </p> '
