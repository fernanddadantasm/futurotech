from fastapi import FastAPI, Form, Request
#from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import sqlite3 as sql

app = FastAPI()

# Configura o diretório ondee estão os templates HTML:
templates = Jinja2Templates(directory="templates")

# Criação da tabela Clientes:
def criar_tabela():
    conexao = sql.connect("estoque.db")
    conexao.cursor().execute("""
        CREATE TABLE IF NOT EXISTS Clientes (
            codigo INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE,
            idade INTEGER CHECK (idade < 150 AND idade > 0)
        )
    """)
    conexao.commit()
    conexao.close()

criar_tabela()


# Rota GET → exibe o formulário HTML:
@app.get("/") # Opcional agora c/Jinja --> , response_class=HTMLResponse)
def enviar_form(request: Request):
    # 'request' é obrigatório no Jinja2Templates
    return templates.TemplateResponse("formularios.html", {"request": request})


# Rota POST → insere o cliente e mostra mensagem de sucesso/erro
@app.post("/cliente/",  response_class=HTMLResponse) # Opcional agora c/Jinja --> , response_class=HTMLResponse)
def criar_cliente(request: Request, nome: str = Form(...), email: str = Form(None), idade: int = Form(...)  ):
    try:
        conn = sql.connect("estoque.db")
        conn.cursor().execute(
            "INSERT INTO Clientes (nome, email, idade) VALUES (?, ?, ?)",
            (nome, email, idade)
        )
        conn.commit()
        mensagem = f"✅ Cliente {nome} cadastrado com sucesso!"
        cor = "green"
    except Exception as erro:
        mensagem = f"❌  Erro ao cadastrar: {erro}"
        cor = "red"
    finally:
        conn.close()

    # Renderiza a página resposta.html com variáveis do Python
    '''
    Fluxo com Jinja (Renderização no Servidor)
    . O cliente (navegador) faz uma requisição HTTP para o servidor (GET / ou POST /cliente/).
    . O FastAPI executa a função Python da rota.
    . O Jinja2 abre o template (formulario.html), processa as variáveis ({{ mensagem }}, {{ cor }}, etc).
    . O FastAPI retorna o resultado já “renderizado” (HTML puro).
    . O navegador exibe esse HTML.
    '''
    return templates.TemplateResponse(
        "resposta.html",
        "formularios.html",
        {"request": request, "mensagem": mensagem, "cor": cor}
    )

@app.get("/alterar_idade/")
def alterar_idade(request:Request):
    return templates.TemplateResponse("alterar_idade.html", {"request": request}, status_code=203)

@app.post("/resposta_alterar_idade/")
def resposta_alterar_idade(request: Request, nome: str = Form(...), nova_idade: int = Form(...)):
    try:
        conn = sql.connect("estoque.db")
        conn.cursor().execute(
            "UPDATE Clientes SET idade = ? WHERE nome = ?",
            (nova_idade, nome)
        )
        conn.commit()
        mensagem = f"✅ Idade de {nome} alterada para {nova_idade} anos!"
        cor = "green"
    except Exception as erro:
        mensagem = f"❌  Erro ao alterar idade: {erro}"
        cor = "red"
    finally:
        conn.close()

    return templates.TemplateResponse(
        "resposta.html",
        {"request": request, "mensagem": mensagem, "cor": cor}
    )

