import os 
import time
os.system("cls")


lista_produtos = []
while True:
    print("======PRODUTOS======")
    opcao = input("""     
1 - Adicionar produto
2 - Alterar produtos 
3 - Excluir produto
4 - Listar produtos 
5 - Sair

Digite a opção desejada: 

""")
    os.system("cls")
    
    match opcao:
        case "1":
            print("===Adicionar produto===")
            codigo = int(input("Digite o código do produto: "))
            produto_nome = (input("Digite o nome do produto: ")).upper().strip()
            preco = float(input("Digite o preço do produto: "))
            quantidade = int (input("Digite a quantidade do produto: "))
            lista_produtos.append([codigo, produto_nome, preco, quantidade])
            print("Produto adicionado com sucesso!")
            time.sleep(2)
            os.system("cls")
        case "2":
            print("Alterar produto")
            if len(lista_produtos) == 0:
                print("Nenhum produto cadastrado.")
                input("Pressione ENTER para voltar ao menu...")
                os.system("cls")
            else:
                codigo_alterar = int(input("Digite o código do produto que deseja alterar: "))
                for i in lista_produtos:
                    if i[0] == codigo_alterar:
                        novo_nome = input("Digite o novo nome do produto: ").upper().strip()
                        novo_preco = float(input("Digite o novo preço do produto: "))
                        nova_quantidade = int(input("Digite a nova quantidade do produto: "))
                        i[1] = novo_nome
                        i[2] = novo_preco
                        i[3] = nova_quantidade
                        print("Produto alterado com sucesso!")
                        break
                    else:
                        print("Produto não encontrado.")
                        input("Pressione ENTER para voltar ao menu...")
                    time.sleep(2)
                os.system("cls")
          
        case "3":
            print("Excluir produto")
            if len(lista_produtos) == 0:
                print("Nenhum produto cadastrado.") 
            else:
                codigo_excluir = int(input("Digite o código do produto que deseja excluir: "))
                for i in lista_produtos:
                    if i[0] == codigo_excluir:
                        lista_produtos.remove(i)
                        print("Produto excluído com sucesso!")
                        break
                    else:
                        print("Produto não encontrado.")
                        input("Pressione ENTER para voltar ao menu...")
                    time.sleep(2)
                    os.system("cls")
     
        case "4":
            for i in lista_produtos:
                print("===Lista de produtos===")
                print(f"Código: {i[0]}\n Produto: {i[1]}\n Preço: R${i[2]}\n Quantidade: {i[3]}\n ")
            time.sleep(2)
            input("Pressione ENTER para voltar ao menu...")
            os.system("cls")         
                
        case "5":
            print("Saindo do sistema...")
            break
            
        case _: 
            print("Opção inválida, tente novamente.")





