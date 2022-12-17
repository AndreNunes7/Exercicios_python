def fatorial(num, show):
    """
    fatorial(n, show=False)
    -> CALCULA o fatorial de um numero
    :param num: O numero a ser calculado
    :param show: (opcional) Mostrar ou nao a conta!


    """

    i = 1

    for n in range(num, 0, -1):
        if show:
            print(f"{n} ", end=' ')
            if n > 1:
                print(" x ", end=' ')
            else:
                print(" = ",end=' ')
        i *= n
    print(i)


help(fatorial)
fatorial(5, show=True)
