def linha():
    print("-=" * 20)


def maior(*valores):
    cont = maior = 0
    linha()
    print(f"Analisando os valores: ")
    for num in valores:
        print(f"{num} ", end=' ')
        if cont == 0:
            maior = num
        else:
            if num > maior:
                maior = num
        cont += 1
    print(f"\nO maior valor é {maior}")
    print(f"Ao todo existem {len(valores)} numeros!!")


maior(2, 3, 5, 7, 1, 9, 0)
maior(5, 1, 6, 2)
maior(10, 2, 4, 6, 0)
maior(8)

linha()
