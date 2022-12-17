#calculo de PA
print("{:=^40}".format("Calculo de PA"))
p = int(input("Digite um termo: "))
r = int(input("Digite uma RAZAO: "))
decimo = p + (10 - 1) * r
for c in range(p, decimo + r, r):
    print("{}".format(c), end=' -> ')
print("Acabou!")