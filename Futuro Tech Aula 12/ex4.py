from flask import Flask
ex4 = Flask(__name__)

@ex4.route('/')
def principal():
    return """
   <header>
        <h1 style="text-align: center;">Página Principal</h1>
        <nav style="border:3px solid black; display: flex; justify-content: space-around;">
            <a href="/cadastro">Cadastro</a>
            <a href="/contatos">Contatos</a>
        </nav>
    </header>
"""

@ex4.route('/cadastro')
def cadastro():
    return """
    <form action="">
        <input type="text" placeholder="Nome:">
        <input type="text" placeholder="Email:">
        <input type="text" placeholder=" CPF:">
        <button type="button">Salvar</button>
    </form>
    """
@ex4.route('/contatos')
def contatos():
     return "<h1>Página de Contatos</h1>"

    
if __name__ == '__main__':
    ex4.run(debug=True)