import os 
os.system("cls")

# caixa eletronico 

saldo = 1000
saque =saldo+1 

while saque>saldo:
    saque = float(input(f"Informe o valor do seu saque (saldo = R${saldo}): "))
saldo -= saque

print(f"Novo Saldo = R${saldo}")