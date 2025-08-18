
import os 
os.system("cls")
# Dicionário:
def comprar():
    return None

clientes = {
    "nome": "Fernanda Dantas", 
    "idade": 22,
    "altura": 1.65,
    "tem_CNH": True,
    "efetuar_compra": comprar(),
}

print(f"O cliente {clientes["nome"]} tem CNH? {clientes["tem_CNH"]}")

if clientes["tem_CNH"]:
    print("Cliente tem CNH")
else:
    print("Cliente não tem CNH")

clientes["efetuar_compra"]

# Inclusão 
clientes["saldo"] = 1.400
print(clientes)

# Alteração dicionário
clientes["saldo"] = 1.500
print(clientes)
# Exclusão

del clientes["idade"]