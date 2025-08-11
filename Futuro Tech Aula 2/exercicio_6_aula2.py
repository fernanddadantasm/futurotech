import os 
os.system("cls")

login_correto = "admin" 
senha_correta = "12345"

nome_usuario = input("Digite o seu login: ").lower()

if nome_usuario != login_correto:
    print("Usuário não autorizado!")
else:
    senha = input("Digite sua senha: ")
    if senha == senha_correta:
        print("""Login realizado com sucesso!
=== Seja bem vindo! ===   
            """)
    else:
        print("Senha incorreta!")
        # 4
        