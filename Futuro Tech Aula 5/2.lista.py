import os
os.system("cls")

clientes = {
    "nomes": ["Vinicius", "Ana", "Carla"],
    "idades": [55, 22, 33],
    "alturas": [1.60, 1.65, 1.80],
    "tem_cnh": [True, False, True],
    "dependentes": [
        {
        "conjungue": "Maria",
        "filhos": ["Marcelo", "Márcia"]
            
        },

    ]

}

print(clientes["nomes"][2])
print(clientes["alturas"][1])
print(clientes["dependentes"][0]["filhos"])
