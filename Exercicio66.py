cont = soma = 0
while True:
    numero = int(input("Digite um valor (999 para parar):  "))
    cont += 1
    if numero == 999:
        break
    soma += numero
print(f"foram digitados {cont} e a soma de todos é {soma}")
