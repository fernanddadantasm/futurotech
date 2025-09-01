import os 
os.system("cls")


# Ex 1
# Dada a lista, ["Ana", "Carlos", "Maria", "João"], gerar uma nova lista com os nomes em letras maiusculas


nomes = ["fernanda", "gabriela", "tamires", "veronica"]
map_nomes = list(map(lambda nomes: nomes.upper(), nomes))

print(map_nomes)


