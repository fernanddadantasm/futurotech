import os 
os.system("clear || cls")

# Declarando variáveis
nome = input("Digite o nome do estudante: ").strip().capitalize()
nota_1 = float(input("Digite sua primeira nota: "))
nota_2 = float(input("Digite sua segunda nota: "))
media = (nota_1 + nota_2) / 2 

# Estrutura condicional
if media >= 6:
    print("Aluno aprovado!")
elif media >= 4: 
    print("Aluno de recuperação!")
else:
    print(f"Olá, {nome}! Você ficou com média = {media}")

# Usar exit() quando quiser testar partes do codigo sem rodar ele todo. O comando exit()
# deve ficar sempre em baixo do codigo que você quer testar;
# strip() retira o espaço antes e depois