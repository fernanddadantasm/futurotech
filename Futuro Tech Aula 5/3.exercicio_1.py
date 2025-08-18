# Criar um dicionário

import os
os.system("cls")
em_estoque:bool = True if input("Produto em estoque (S/N)?").title().strip() == "S" else False
produtos = {
    "descricao": input("Digite a descrição do produto: ").title().strip(),
    "codigo": int(input("Digite o código do produto: ")),
    "preco": float(input("Digite o preço do produto: ")),
    "unidade": int(input("Digite a unidade do produto")),
    "quantidade": int(input("Digite a quantidade do produto")),
    "validade": [ 
        {
            "data": int(input("Digite a data: ")), 
            "mes": int(input("Digite o mês: ")),
            "ano": int(input("Digite o ano: "))
        },
    ],
    "peso": float(input("Digite o peso do produto: ")),

}

print(f"Produto {produtos["descricao"]}\nCódigo {produtos["codigo"]} \nPreço R${produtos["preco"]} \
    \nTem o peso de {produtos["peso"]} \nNo valor de R${produto["preco"]} a")

   
