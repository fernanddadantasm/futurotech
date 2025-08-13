# Existem duas formas de criar uma lista vazia:
# lista_produtos = []
# lista_clientes = ["Pedro", "Ana", "Marta"]
# lista_vazia = list()

# CRUD = CREATE, READ, UPDATE, DELETE
import os
os.system("cls")
# Adicionando dados nas listas:
lista_produtos = []
lista_clientes = ["Pedro", "Ana", "Marta"]

lista_produtos.append("Parafuso 3/8")
print(lista_produtos)

lista_clientes.append("Ricardo")
print(lista_clientes)

# Alterar dados em uma lista:
lista_clientes[1] = "Ana Maria"
print(lista_clientes)

# Excluir dados da lista:
del lista_clientes[0]
print(lista_clientes)
# backup = lista_clientes.pop(0) Outra forma de excluir dados de uma lista 
# print("Backup = ", backup)



matriz = [ ["Ana", 22, 1.65], ["Pedro", 27, 1.76], ["Marta", 34, 1.78] ]
print(matriz[1][2])

