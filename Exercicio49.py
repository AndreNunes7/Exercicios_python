import time
print("{:=^40}".format("Calculadora de Tabuada V2.0"))
print("-="*20)
num = int(input("Digite um numero para ver sua tabuada: "))
print("Calculando...")
time.sleep(1)
print("-="*20)
for c in range(1, 11):
    print("{} X {} = {}".format(num, c, c * num))
print("-="*20)
