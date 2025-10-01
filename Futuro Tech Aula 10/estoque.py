#Código Principal (Estoque.py)

from funcoes import *
from sub_menu_cliente import *

# Menu Principal:
def menu_principal():
    while True:
        print(" ***   M E N U   P R I N C I P A L   ***")
        print('*' * COLUNAS)
        print("1 - Cadastro de Clientes")
        print("2 - Cadastro de Produtos")
        print("3 - Cadastro de Pedidos")
        print('.' * COLUNAS)
        print("4 - Relatórios")
        print('-' * COLUNAS)
        print("S - Sair")
        opcao = input("Digite opção acima: ").strip().upper()
        limpar_tela()
        match(opcao):
            case '1':
                menu_clientes()
            case '4':
                relatorios()
            case 'S':
                exit()

# Ponto de Início do App:A
menu_principal()