import os 
os.system("cls")

def calcular_tempo_paradas(tempos_paradas):
    tempo_total = sum(tempos_paradas)
    
    if len(tempos_paradas) > 0:
        tempo_medio = tempo_total / len(tempos_paradas)
    else:
        tempo_medio = 0
    
    return tempo_total, tempo_medio

tempos_paradas = [5, 10, 3, 7, 12]  
tempo_total, tempo_medio = calcular_tempo_paradas(tempos_paradas)
print(f"Tempo total de paradas: {tempo_total} minutos")
print(f"Tempo médio por parada: {tempo_medio:.2f} minutos")

