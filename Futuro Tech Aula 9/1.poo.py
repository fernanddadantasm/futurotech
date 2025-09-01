# poo = Programação orientada a objetos 
# Pilares:
# a) abstração = Levar para programção só as "caracteristicas" e os "comportamentos" relevantes do objeto.
    # ex: controle ar condicionado: 
        # visor, carregamento (pilha, bateria). 

import os
os.system("cls")


class Veiculos:
    # Atributos 
    def __init__(self, cor, marca,maxima):
        self.cor = cor
        self.marca = marca
        self.velocidade_maxima = maxima
        self.velocidade_atual = 0
        self.ligado = False
    # Acelerar
    def acelerar(self, valor):
        if (velocidade_atual + valor) <= self.velocidade_maxima:
            velocidade_atual += valor
    # Frear   
    def frear(self,valor):
        if (self.velocidade_atual - valor) >= 0:
            self.velocidade_atual -= valor
    # Ligar/Desligar
    def ligar_desligar(self):
        if esta_ligado and self.velocidade_atual == 0:
            esta_ligado = False
        elif not esta_ligado and self.velocidade_atual == 0:
            esta_ligado = True