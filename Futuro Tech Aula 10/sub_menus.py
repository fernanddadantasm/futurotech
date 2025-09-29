from funcoes import *


def menu_clientes():
    print(" ***   M E N U   C L I E N T E S   ***")
    print('=' * COLUNAS)
    print("1 - Inclusão de Clientes")
    print("2 - Alteração de Clientes")
    print("3 - Exclusão de Clientes")
    print('=' * COLUNAS)
    print("S - Sair para Menu Principal")
    print('=' * COLUNAS)
    opcao = input("Digite opção acima: ").strip().upper()
    limpar_tela()
    match (opcao):
        case '1':
            incluir_clientes()
        case 'S':
            return None