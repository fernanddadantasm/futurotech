# If, Else e Elif 
# Criar um programa que verifica se um número é positivo, negativo ou zero

import os
os.system("clear || cls") 

numero = float(input("Digite um número: "))

if numero > 0:
    print("O número digitado é positivo!")
elif numero < 0:
    print("O número digitado é negativo!")
else: 
    print("Número Nulo!")
    