import os 
os.system("cls")

print("=== TRIAGEM PARA DOAÇÃO DE SANGUE ===")
idade = int(input("Digite a sua idade: "))
peso = float(input("Digite seu peso: "))
jejum = input("Você está em jejum? (S/N): ").upper()

if 16 <= idade <= 69 and peso > 50 and jejum == "N":
    print("LIBERADO!")
else:
    print("NEGADO!")
