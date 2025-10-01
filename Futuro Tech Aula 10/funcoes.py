#Funções (funcoes.py)

#Funções

import sys
import os
import sqlite3 as sql
from sql import (strings_sql, )


COLUNAS = 70


def pausa():
    input("Pressione qq tecla p/continuar...")


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


def validacao( codigo, tabela ) -> tuple:
    conexao = conectar_banco()
    texto = f"SELECT * FROM {tabela} WHERE codigo = {codigo}"
    tupla_dados = conexao.cursor().execute( texto ).fetchone()
    return tupla_dados if tupla_dados else None


def incluir_clientes():
    nome = input("Informe o NOME do cliente: ").strip().upper()    
    cpf = input("Informe o CPF (somente números): ").strip()
    esta_ativo = True
    salvar_cliente( (nome, cpf, esta_ativo) )


def alterar_clientes():
    codigo = int( input("Informe o CÓDIGO do Cliente: ") )
    tupla_dados = validacao( codigo, "Clientes")
    if tupla_dados:
        print(f"Nome: {tupla_dados[1]}, CPF: {tupla_dados[2]}, Ativo: {tupla_dados[3]}")
    else:
        print("Código inválido!!")
        return None
    campo_alterar = input("Alterar: [1] - Nome, [2] - CPF e [3] - Ativo: ")
    
    # Abrir conexão com o banco de dados:
    conexao = conectar_banco()

    match (campo_alterar):
        case '1':   # Alterar NOME do Cliente
            novo_nome = input("Informe o NOVO Nome: ").strip().upper()
            conexao.cursor().execute(strings_sql["alterar_nome_cliente"], (novo_nome, codigo) )
            conexao.commit() 


def excluir_clientes():
    codigo = int( input("Informe o CÓDIGO do Cliente: ") )
    tupla_dados = validacao( codigo, "Clientes")
    if tupla_dados:
        print(f"Nome: {tupla_dados[1]}, CPF: {tupla_dados[2]}, Ativo: {tupla_dados[3]}")
    else:
        print("Código inválido!!")
        return None
    confirma = input("Confirma (S/N) ? ").strip().upper()
    if not confirma == 'S': return None 

    conexao = conectar_banco()
    conexao.cursor().execute(strings_sql["excluir_cliente"], (codigo, ) )
    conexao.commit()
    print("Registro Excluído!")
    pausa()


def rel_geral():
    conexao = conectar_banco()
    # Lista de Tuplas c/ dados dos Clientes
    lista_clientes = conexao.cursor().execute(
        """
            SELECT * FROM Clientes
        """                                      
    ).fetchall()
    for cliente in lista_clientes:
        print(f"Código: {cliente[0]}, Cliente: {cliente[1]}, CPF: {cliente[2]}, ATIVO: {'Sim' if cliente[3] else 'Não'}")
    pausa()
    

def rel_cliente():
    codigo = int(input("Informe o CÓDIGO do Cliente: "))
    tupla_dados = validacao(codigo, "Clientes")
    if tupla_dados:
        print(f"Código do Cliente: {tupla_dados[0]}")
        print(f"Nome do Cliente: {tupla_dados[1]}")
        print(f"C.P.F do Cliente: {tupla_dados[2]}")
        print(f"Cliente ATIVO? {'Sim' if tupla_dados[3] else 'Não'}")
        print('')
        print('-' * COLUNAS)
        print('')
    else:
        print("Código inválido!")
    pausa()


def pesquisar(strPesquisa: str, nome_tabela: str, indice_campo: int) -> list:
    conexao = conectar_banco()
    lista_dados = conexao.cursor().execute(f"SELECT * FROM {nome_tabela}").fetchall()
    return lista_dados
    
   
    
