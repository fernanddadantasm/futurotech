from flask  import Flask
app = Flask(__name__)

ex2 = Flask(__name__)

@ex2.route('/')
def aplicacao():
    nome_completo = "Fernanda Dantas"
    return f"""
    <h1 style="color:red; border: 3px solid black;">Minha pagina!</h1>
    <h3>Olá, {nome_completo}!</h3>
    <br/>
  
    """