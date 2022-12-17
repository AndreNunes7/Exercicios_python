def leiaint(n):
    check = False
    valor = 0
    while True:
        n = str(input(n))
        if n.isnumeric():
            valor = int(n)
            check = True
        else:
            print("Você precisar digitar apenas numeros!!: ")
        if check:
            break
    return valor


# Programa principal
num = leiaint("Digite um numero: ")
print(f"O valor digitado foi {num}")
