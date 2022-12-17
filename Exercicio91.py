import random
from time import sleep
from operator import itemgetter
jogadores = {"Jogador1": random.randint(1, 6),
             "Jogador2": random.randint(1, 6),
             "Jogador3": random.randint(1, 6),
             "Jogador4": random.randint(1, 6)}
ranking = {}
print("Valores sorteados: ")
print("-="*15)
for p, v in jogadores.items():
    print(f"{p} tirou: {v}")
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)  # serve para sortear e ordenar o valor em forma
#  decrescente, o (1) e do random.randint(1,6)
print("-="*15)
print("== Ranking dos jogadores!: ==")
print("-="*15)

for p, v in enumerate(ranking):
    print(f"{p + 1}° lugar:  {v[0]} tirou o dado: {v[1]}  ")
print("-="*15)