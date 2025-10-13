from flask import Flask
ex5 = Flask(__name__)

@ex5.route('/')
def home():
    return """
        <h1 style="text-align: center;">Página Principal</h1>
        <a href='/produtos'>Lista de Produtos</a>
 
"""

@ex5.route('/produtos')
def produtos():
    lista_produtos = ["Teclado", "Monitor 27", "Mouse Gamer", "Mouse Pad"]
    produtos = "".join(f"<li>{p}</li>" for p in lista_produtos)
    return f'<ol>{produtos}</ol>'

   
 

    
if __name__ == '__main__':
    ex5.run(debug=True)