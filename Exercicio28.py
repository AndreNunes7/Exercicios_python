import random
e = int(input("Digite um numero de 0 ate 5: "))
print("Analisando...")
s = random.choice([0, 5])
random.shuffle([s])
if e == s:
    print("O numero era {} VOCÊ ACERTOU PARABENS!".format(s))
else:
    print("Você errou, o numero escolhido era: {}".format(s))

