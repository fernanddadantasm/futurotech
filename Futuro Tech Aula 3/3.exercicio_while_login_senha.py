import os
os.system("cls")

login = "hub"
senha = "123456"
senha_pedida = "0"
login_pedido = "0"
while login and senha != senha_pedida and login_pedido:
    login_pedido = input("Digite seu login: ")
    senha_pedida = input("Digite sua senha: ")

print("Login bem sucedido!")