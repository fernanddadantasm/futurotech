
from flask import Flask

app = Flask(__name__)


@app.route('/principal')
def principal():
    return "<h1>Olá,mundo!</h1><br/><strong><em>Futuro Tech</em><strong/>"

if __name__ == '__main__':
    app.run(debug=True)
