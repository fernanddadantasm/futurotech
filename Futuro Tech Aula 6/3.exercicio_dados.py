import os 
os.system("cls")

def endereco():
    rua = input("Digite o nome da rua: ")
    numero = int(input("Digite o número: "))
    bairro = input("Digite o nome do bairro: ")
    return f"Endereço: {rua}, nº {numero}, {bairro}"

print(endereco())

