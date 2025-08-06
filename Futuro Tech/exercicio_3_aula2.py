import os 
os.system("clear || cls")


print("=== FESTA VIP ===")

idade = int(input("Digite sua idade: "))
traje = (input("Você está usando traje social? (S/N) ")).upper()
lista_vip = (input("Você está na lista vip? (S/N) ")).upper()

if idade >= 18 and traje == "S" or lista_vip == "S":
    print("Acesso liberado!")
else: 
    print("Acesso negado!")


# Outra forma de fazer o exercicio
#idade = int(input("Digite sua idade: ")) 
# traje = True if input("Você está usando traje social? S/N ") == 's' else False
# lista_vip = True if input("Você está na lista vip? S/N ") == 's' else False

# if (idade >= 18) and ((traje_social) or (lista_vip) ):
    # print("Acesso liberado!")
# else:
    # print("Acesso negado!")

# dontpad.com/hub09 (exercicios parea aula)