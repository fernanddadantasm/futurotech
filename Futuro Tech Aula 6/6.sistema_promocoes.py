
import os 
os.system("cls")  

def descontar(lista_produto):
    for produto in lista_produto:
        if produto["categoria"] == "eletronico":
            produto["preco_com_desconto"] = produto["preco"] * 0.9
        elif produto["categoria"] == "roupa":
            produto["preco_com_desconto"] = produto["preco"] * 0.95
        else:
            produto["preco_com_desconto"] = produto["preco"]

    return lista_produto  

produtos = [
    {'nome': 'Smartphone', 'preco': 1000, 'categoria': 'eletronico'},
    {'nome': 'Camiseta', 'preco': 50, 'categoria': 'roupa'},
    {'nome': 'Livro', 'preco': 30, 'categoria': 'outro'}
]

print(descontar(produtos))

          

            
            


 


