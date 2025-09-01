import os
os.system("cls")

# Uma loja possui os preços base de produtos em uma lista: [100, 250.80, 400, 50]
# Use map() com lambda para retornar os preços finais, adicionando 15% de imposto em cada item 

lista_precos = [100, 250.80, 400, 80]

imposto = list(map(lambda n: n + n * 0.15, lista_precos))
print(imposto)