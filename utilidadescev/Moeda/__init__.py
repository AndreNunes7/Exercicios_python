def dobro(num=0, show=False):
    d = num * 2
    if show:
        return cifrao(num)
    else:
        return d


def metade(num=0, show=False):  # o show serve para mostrar ou nao os numeros formatados em formato de dinheiro!!
    m = num / 2
    if show:  # aqui é feito se é para mostrar ou nao
        return cifrao(num)
    else:
        return m


def aumento(num=0, aumento=80, show=False):  # o aumento neste caso foi um aumento de 10%
    a = num + (num * aumento / 100)
    if show:
        return cifrao(num)
    else:
        return a


def diminui(num=0, menor=35, show=False):
    di = num - (num * menor / 100)
    if show:
        return cifrao(num)
    else:
        return di


def cifrao(num=0, moeda="R$", show=False):
    return f"{moeda}{num:.2f}".replace(".", ",")


def resumo(num=0, moeda="R$"):
    print("-=" * 20)
    print(f"{'Resumo do valor':^35}")
    print("-=" * 20)

    print(f"Preço analisado:     \t{moeda}{num:.2f}".replace(".", ","))
    print(f"Dobro do preço:      \t{moeda}{dobro(num):.2f}".replace(".", ","))
    print(f"Metade do preço:     \t{moeda}{metade(num):.2f}".replace(".", ","))
    print(f"80% de aumento:      \t{moeda}{aumento(num):.2f}".replace(".", ","))
    print(f"35% de redução:      \t{moeda}{diminui(num):.2f}".replace(".", ","))
    print("-=" * 20)



    # outra forma de se fazer >>>>

# def dobro(num=0, show=False):
#     d = num * 2
#     return d if show is False else cifrao(d)
#
#
# def metade(num=0, show=False):
#     m = num / 2
#     return m if show is False else cifrao(m)
#
#
# def aumento(num=0, aumento=10, show=False):
#     a = num + (num * aumento / 100)
#     return a if show is False else cifrao(a)
#
#
# def diminui(num=0, menor=13, show=False):
#     di = num - (num * menor / 100)
#     return di if show is False else cifrao(di)
#
#
# def cifrao(num=0, moeda="R$", show=False):
#     return f"{moeda}{num}".replace(".", ",0")
