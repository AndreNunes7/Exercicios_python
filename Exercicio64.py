# tratando varios valores V1.0

print("~~"*20)
numero = cont = soma = 0
numero = int(input("Digite um numero [999 para parar]: "))
while not numero == 999:
    cont += 1
    soma += numero
    numero = int(input("Digite um numero [999 para parar]: "))
    if numero == 999:
        print("Você digitou {} numeros e a soma entre eles foi {}.".format(cont, soma))
        