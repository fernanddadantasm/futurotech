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
    match opcao:
        case "1":
            print("===Adicionar produto===")
            codigo = int(input("Digite o código do produto: "))
            produto_nome = (input("Digite o nome do produto: ")).upper().strip()
            preco = float(input("Digite o preço do produto: "))
            quantidade = int (input("Digite a quantidade do produto: "))
            lista_produtos.append([codigo, produto_nome, preco, quantidade])
        
        case "2":
            print("Alterar produto")    
          
        case "3":
            print("Excluir produto")
     
        case "4":
            for i in lista_produtos:
                print(f"Código: {i[0]}\n Produto: {i[1]}\n Preço: R${i[2]}\n Quanttidade: {i[3]}\n ")
                sleep.time(4)
        case "5":
            print("Saindo do sistema...")
            break
            
        case _: 
            print("Opção inválida, tente novamente.")
    


    

