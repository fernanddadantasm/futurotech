# Função Lambda
# São funções anônimas, ou seja, funções sem nome.
# São usadas para criar funções simples e rápidas, geralmente em uma única linha de código.
import os 
os.system("cls")

def soma(x:float, y:float) -> float:
    """Função que soma dois números."""
    return x + y

print(soma(20, 30))

print((lambda x, y: x + y)(20, 30))

quadrado = lambda n: n**2

print(quadrado(3))



