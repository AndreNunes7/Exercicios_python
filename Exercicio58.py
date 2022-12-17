# jogo da adivinhaçao V2.0
import random

cont = 0
computador = random.randint(0, 10)
print("---- jogo da adivinhação ----")
print("Escolha um numero de 0 a 10 para começar: ")
acertou = False
while not acertou:
    escolha = int(input("Seu numero: "))
    cont += 1
    if escolha == computador:
        acertou = True
    else:
        if escolha > computador:
            print("Menos... Tente mais uma vez!")
        elif escolha < computador:
            print("Mais... Tente mais uma vez!")
print("Você acertou parabéns! você precisou de {} palpites!".format(cont))
