import os 
os.system("cls")
 
# UDF - user defined 

def soma(x,y):
    return x + y

def media(n1, n2):
    return soma(n1, n2) / 2

# Chamada de Função
valor_1 = float(input("Digite o primeiro valor: "))
valor_2 = float(input("Digite o segundo valor: "))
resultado = media(valor_1, valor_2)
print(f"A média é: {resultado}")





