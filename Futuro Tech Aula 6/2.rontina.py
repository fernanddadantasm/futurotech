def incluir_produto():
    descricao = input("Digite a descrição do produto: ").strip().upper()
    preco = float(input("Digite o preço do produto: "))
    
    print(f"Produto {descricao} adicionado com sucesso!")

incluir_produto()