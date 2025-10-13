from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1 style='color:blue'>Hello, World!</h1>"

@app.route('/teste')
def teste():
    return "<h3 style='color:green'>Teste</h3>"

