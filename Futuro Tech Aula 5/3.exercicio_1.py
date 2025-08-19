
# A O formato ':02d' formata um número inteiro para ter pelo menos 2 dígitos,
# preenchendo com zero à esquerda se necessário.
# Exemplo: 5 será exibido como '05', 12 será exibido como '12'.
import os
os.system("cls")  

em_estoque = True if input("Produto em estoque (S/N)? ").strip().upper() == "S" else False

produtos = {
    "descricao": input("Digite a descrição do produto: ").title().strip(),
    "codigo": int(input("Digite o código do produto: ")),
    "preco": float(input("Digite o preço do produto: ")),
    "unidade": int(input("Digite a unidade do produto: ")),
    "quantidade": int(input("Digite a quantidade do produto: ")),
    "validade": [
        {
            "data": int(input("Digite o dia da validade: ")),
            "mes": int(input("Digite o mês da validade: ")),
            "ano": int(input("Digite o ano da validade: "))
        },
    ],
    "peso": float(input("Digite o peso do produto (kg): ")),
}

print("\n--- Dados do Produto ---")
print(f"Descrição: {produtos['descricao']}")
print(f"Código: {produtos['codigo']}")
print(f"Preço: R$ {produtos['preco']:.2f}")
print(f"Peso: {produtos['peso']} kg")
print(f"Unidade: {produtos['unidade']}")
print(f"Quantidade: {produtos['quantidade']}")
validade = produtos['validade'][0]
print(f"Validade: {validade['data']:02d}/{validade['mes']:02d}/{validade['ano']}")

if em_estoque:
    print("O produto está disponível em estoque.")
else:
    print("O produto não está disponível em estoque.")