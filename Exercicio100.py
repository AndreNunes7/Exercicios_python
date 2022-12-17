import random
import time


def sorteio():
    print("Sorteando 5 valores da lista: ", end=' ')
    for n in range(0, 5):
        num = random.randint(1, 10)
        numeros.append(num)
        time.sleep(0.5)
        print(f"{num} ", end=' ')


numeros = []
sorteio()


def somaPar(lst):
    soma = 0
    for n in lst:
        if n % 2 == 0:
            soma += n
    print(f"\nA soma dos valores pares da lista é {soma}")


somaPar(numeros)
