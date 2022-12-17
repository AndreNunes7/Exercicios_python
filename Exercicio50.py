soma = 0
cont = 0
for c in range(1, 7):
    n = int(input("Digite {} numero: ".format(c)))
    if n % 2 ==0:
        cont = cont + 1
        soma = soma + n
print("Você informou {} numeros pares e a soma foi {} ".format(cont, soma))