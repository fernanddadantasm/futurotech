import os 
os.system(" clear || cls")

nota_um = float(input("Digite sua primeira nota: "))
nota_dois = float(input("Digite sua segunda nota: "))

media = (nota_um + nota_dois) / 2

if media >= 7 and nota_um >= 4 and nota_dois >= 4: 
    print("Parabéns! Você foi aprovado.")
else:
    print("Aluno reprovado.")    
