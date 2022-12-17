lista = [[], []]    # lista separada, par e impar
valor = 0       # serve para pegar os valores digitados pelo usuario
for v in range(1, 8):
    valor = int(input(f"Digite o {v}° valor: "))
    if (valor % 2) == 0:
        lista[0].append(valor)  # para dizer ao python em qual lista quer jogar o elemento usa o valor antes do append
        # na variavel!
    else:
        lista[1].append(valor)
lista[0].sort()     # aqui é colocado os valores da lista 0 em forma crescente
lista[1].sort()      # aqui é colocado os valores da lista 1 em forma crescente
print(f"Os valores pares são : {lista[0]}")
print(f"Os valores impares são: {lista[1]}")
