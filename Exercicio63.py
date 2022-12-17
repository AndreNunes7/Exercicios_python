#sequencia fibonacci

print("-="*4, "Sequencia fibonacci", "-="*4)
numero = int(input("Digite um termo para ver a sequencia: "))
print("-="*19)
n1 = 0
n2 = 1
cont = 3
print("{} -> {}".format(n1, n2), end=' ')
while cont <= numero:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    cont += 1
    print(" -> {} ".format(n3), end=' ')
print("-> Fim")
