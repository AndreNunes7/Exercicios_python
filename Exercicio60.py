print("---- Calculando fatorial!! ----")
numero = int(input("Digite um numero: "))
print("Calculando {}! = ".format(numero), end=' ')
c = numero
f = 1
while c > 0:
    print("{}".format(c), end=' ')
    print(" x " if c > 1 else ' = ', end=' ')
    f *= c
    c -= 1
print("{}".format(f), end=' ')

