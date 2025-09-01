import os 
os.system("cls")

# Dada as listas de "preços" e "porcentuais de aumento", gerar uma lista com os preços atualizados.
# precos = [2.50, 11, 21, 16.79, 9.99]
# porcentuais = [3, 1.5, 3, 4.7, 1.5]

precos = [2.50, 11, 21, 16.79, 9.99]
porcentuais = [3, 1.5, 3, 4.7, 1.5]

precos_atualizados = map(lambda x, y: x + x * y/100, precos, porcentuais)
print(list(precos_atualizados))