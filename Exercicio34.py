import time
v = float(input("Qual o seu salario atual?: "))
print("Analisando...")
time.sleep(1.5)
if v > 1250:
    novo = v + (v * 10 / 100)
else:
    novo = v + (v * 15 / 100)
print("Quem ganhavá R${:.2f} passa a ganhar R${:.2f} agora!".format(v, novo))