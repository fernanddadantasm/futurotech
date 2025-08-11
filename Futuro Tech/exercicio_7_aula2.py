import os 
os.system("cls")

renda_mensal = float(input("Digite sua renda mensal: "))
negativado = input("Você está negativado? (S/N) ").upper()
fiador = input("Você possui um fiador com nome limpo? (S/N) ").upper()

if (renda_mensal > 2.000)and (negativado == "N" or fiador == "S"):
    print("Empréstimo aprovado!")
else:
    print("Empréstimo negado!")    