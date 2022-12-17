import time
import random

jogos = []
lista = []

print("-=" * 15)
print(f"        Jogo da MEGA     ")
print("-=" * 15)
perg = int(input("Quantos jogos você quer jogar?: "))
print(f"{'-=' * 5} SORTEANDO {perg} JOGOS! {'-=' * 5} ")
tot = 1
while tot <= perg:
    cont = 0
    while True:
        num = random.randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for i, l in enumerate(jogos):
    time.sleep(1)
    print(f"JOGO {i + 1}: {l}")
print(f"{'-='*4} JOGOS SORTEADOS {'-='*4}")
