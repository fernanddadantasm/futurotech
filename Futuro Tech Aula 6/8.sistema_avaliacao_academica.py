import os 
os.system("cls")

def calcular_media_ponderada(notas, pesos):
    produtos = list(map(lambda x, y: x * y, notas, pesos))
    media = sum(produtos) / sum(pesos)
    return media
notas = [8, 7.5, 9, 6]
pesos = [2, 1, 3, 1]    
media_ponderada = calcular_media_ponderada(notas, pesos)
print(f"Média Ponderada: {media_ponderada:.2f}")