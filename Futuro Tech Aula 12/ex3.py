from flask import Flask
ex3 = Flask(__name__)

@ex3.route('/')
def principal():
    return """
    <h1 style='text-align:center';>Página Principal</h1>
    <a><a href="/produtos">Produtos</a></a> |
"""

@ex3.route('/produtos')
def produtos():
    return """
    <form action="">
        <input type="text">
        <input type="text">
        <input type="text">
        <button type="button">Salvar</button>
    </form>
    """

if __name__ == '__main__':
    ex3.run(debug=True)