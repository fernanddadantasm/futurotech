#Sub Menus

from funcoes import *


def menu_clientes():
    while True:
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
            case '2':
                alterar_clientes()
            case '3':
                excluir_clientes()
            case 'S':
                limpar_tela()
                return None
        limpar_tela()
        

def relatorios():
    while True:
        print(" ***   M E N U   RELATÓRIOS  ***")
        print('=' * COLUNAS)
        print("1 - Relatório Geral de Clientes")
        print("2 - Relatório Cliente")
        print("3 - Relatórios de Clientes por nome")
        print('.' * COLUNAS)
        print("S - Sair para Menu Principal")
        print('=' * COLUNAS)
        opcao = input("Digite opção acima: ").strip().upper()
        limpar_tela()
        match (opcao):
            case '1':
                # Gera o relatório geral de Clientes
                rel_geral()
            case '2':
                # Gera um relatório específico de Cliente pelo código
                rel_cliente()
            case '3':
                strPesquisa = (input("Digite o NOME do cliente: ")).strip().upper()
                lista_dados = pesquisar(strPesquisa, "Clientes", 1)
                for dados in lista_dados:
                    if strPesquisa in dados[1]:
                        print(f"Código: {dados[0]}, Cliente: {dados[1]}, CPF: {dados[2]}, ATIVO: {'Sim' if dados[3] else 'Não'}")
            # Gera relatório por pesquisa de nome
            case 'S':
                limpar_tela()
                return None
            case _:
                print("Opção inválida !!")
        pausa()
        limpar_tela()