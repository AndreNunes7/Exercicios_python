# maior e menor valor

soma = cont = media = maior = menor = 0
escolha = "s"
while escolha in "Ss":
    num = int(input("digite um numero: "))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    escolha = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
media = soma / cont
print(f"Você digitou {cont} numeros e a media é {media}! ")
print("O maior valor foi {} e o menor é {}".format(maior, menor))
