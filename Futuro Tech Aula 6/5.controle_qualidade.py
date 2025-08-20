import os
os.system("cls")


def inspecionar(garrafas: list): 
    total_fora_padrao = 0
    for tamanho_garrafa in garrafas:
        if (tamanho_garrafa<19.5) or (tamanho_garrafa>20.5):
            total_fora_padrao += 1
    return total_fora_padrao

print(inspecionar([20, 3, 44, 21.5]))


    
    




