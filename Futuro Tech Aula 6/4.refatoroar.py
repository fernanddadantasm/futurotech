import os 
os.system("cls")
# """
# """
# Essa estrutura acima se chama doc string. Ela serve para explicar ao usuário alguma coisa  

# Refatorar 
# Sum - Função que soma 
# len - Retorna o tamanho da lista 
def media (lista): 
    return sum(lista)/len(lista)

lista_numero = []
for i in range(5):
    lista_numero.append(float(input("Digite um número: ")))
    
print(media(lista_numero))

