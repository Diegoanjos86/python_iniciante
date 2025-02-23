#informações do Jogador
#Dicionários armazenam chave e valor

pessoa = {
    "nome": "Diego Oliveira",
    "idade":38,
    "peso": 122.2,
    "formado": True
}

print (pessoa["idade"])
print (pessoa["nome"])
print (pessoa["peso"])
print (pessoa["formado"])

player = {
    "nome": "Diego",
    "level": 1,
    "hp": 100,
    "xp": 0,
    "dano":5,
}

npcs = [
    {"nome":"Monstrinho", "dano": 2, "hp":50, "xp":5},
    {"nome":"Monsto", "dano": 5, "hp":100, "xp":10},
    {"nome":"Monstrão", "dano": 10, "hp":150, "xp":15},
    {"nome":"Chefão", "dano": 25, "hp":200, "xp":20},
]

print(npcs)