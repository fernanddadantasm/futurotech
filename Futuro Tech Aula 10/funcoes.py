import sys
import os
import sqlite3 as sql
from sql import (strings_sql, )


COLUNAS = 70
def pausa(): 
    input("Presione enter para continuar...")


def limpar_tela():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")



def criar_tabelas( con ):
    cursor = con.cursor()
    cursor.execute( strings_sql["criar_tabela_clientes"])



def conectar_banco():
    conexao = sql.connect("Estoque.db")
    return conexao



def salvar_cliente( dados: tuple ):
    conexao = conectar_banco()
    criar_tabelas( conexao )
    conexao.cursor().execute(strings_sql["inserir_cliente"], dados)
    conexao.commit()


def validacao (codigo, tabela)-> tuple:
    texto = f"SELECT * FROM {tabela} WHERE codigo = {codigo}"
    conexao = conectar_banco()
    tupla_dados = conexao.cursor().execute(texto).fetchone()
    return tupla_dados if tupla_dados else None 


def incluir_clientes():
    nome = input("Informe o NOME do cliente: ").strip().upper()    
    cpf = input("Informe o CPF (somente números): ").strip()
    esta_ativo = True
    salvar_cliente( (nome, cpf, esta_ativo) )


def alterar_clientes():
    codigo = int (input("Informe o código do cliente: "))
    tupla_dados = validacao(codigo, "Clientes")
    if tupla_dados:
        print(f"Nome: {tupla_dados[1]}, CPF: {tupla_dados[2]}, Ativo: {tupla_dados[3]}")
    else:
        print("Código Inválido! ")
        return None 
    
    conexao = conectar_banco()
    
    campo_alterar = input("Alterar: [1] - Nome, [2] - CPF e [3] - Ativo: ")
    match (campo_alterar):
        case "1": #Alterar nome do cliente
            nome_novo = input("Digite um novo nome: ").strip().upper()
            conexao.cursor().execute(strings_sql["alterar_nome_cliente"], (nome_novo, codigo))
            conexao.cursor().execute()
            conexao.commit()


def excluir_clientes(): 
     codigo = int(input("Informe o CÓDIGO do Cliente: "))
     tupla_dados = validacao(codigo, "Clientes")
     if tupla_dados: 
        print(f"Nome:  {tupla_dados[1]}, CPF:  {tupla_dados[2]}, Ativo: {tupla_dados[3]}")
     else:    
         print("Código Inválido!")
         return None
    
confirma = input("Confirma (S/N) ? ").strip().upper()
#if not confirma == "S" :  return None

conexao = conectar_banco()
conexao.cursor().execute(strings_sql["excluir_cliente"])


