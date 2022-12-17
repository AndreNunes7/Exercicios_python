import random
import time
print("{:=^40}".format(" VAMOS JOGAR ? "))
print("Comece escolhendo uma das opções abaixo:")
print(""" [ 0 ] PEDRA \n [ 1 ] PAPEL \n [ 2 ] TESOURA """)
itens = ("PEDRA", "PAPEL", "TESOURA")
computador = random.randint(0, 2)
e = int(input("Qual sua jogada?: "))
print("JO")
time.sleep(1)
print("Ken")
time.sleep(1)
print("PÔ")
print("-="*15)
if e == 0:
    print("O jogador escolheu PEDRA")
    print("O computador escolheu {}".format(itens[computador]))
    if computador == 0:
        print("-="*15)
        print("Houve um EMPATE!!")
    elif computador == 1:
        print("-="*15)
        print("O computador VENCEU!!")
    elif computador == 2:
        print("-=" * 15)
        print("O jogador VENCEU!!")
elif e == 1:
    print("O jogador escolheu PAPEL")
    print("O computador escolheu {}".format(itens[computador]))
    if computador == 0:
        print("-=" * 15)
        print("O jogador VENCEU!!")
    elif computador == 1:
        print("-=" * 15)
        print("Houve um EMPATE!!")
    elif computador == 2:
        print("-=" * 15)
        print("O computador VENCEU!!")
elif e == 2:
    print("O jogador escolheu TESOURA")
    print("O computador escolheu {}".format(itens[computador]))
    if computador == 0:
        print("-=" * 15)
        print("O computador VENCEU!!")
    elif computador == 1:
        print("-=" * 15)
        print("O jogador VENCEU!!")
    elif computador == 2:
        print("-=" * 15)
        print("Houve um EMPATE!!")
else:
    print("Opção invalida, Tente novamente!")
