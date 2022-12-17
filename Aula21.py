# interactive help

help(print())
print(input.__doc__)


# Docstrings
def contador(inicio, fim, passo):  # funçao de contador
    # docstring abaixo  use o comando [ help(contador para ve-lo]
    """
    -> Faz uma contagem e mostra na tela
    :parametro inicio: INICIO DA CONTAGEM
    :parametro fim: FIM DA CONTAGEM
    :paramentro passo: PASSO DA CONTAGEM
    :return: SEM RETORNO
    """

    c = inicio
    while c <= fim:
        print(f"{c} ", end=' ')
        c += passo
    print("FIM !!")


contador(0, 10, 2)

help(contador)


def soma2(a, b, c=0):  # funçao de soma com 3 paramentros, porem se o C nao tiver falor ira ser atribuido a ele o 0
    # caso tenha valor ira somar os 3 valores correspondente!
    # pode colocar todos os paramentros dessa forma tambem exemplo: a=0, b=0, c=0
    """
    funçao de soma com 3 paramentros, porem se o C nao tiver falor ira ser atribuido a ele o 0

    caso tenha valor ira somar os 3 valores correspondente!

    pode colocar todos os paramentros dessa forma tambem exemplo: a=0, b=0, c=0

    -> Faz a soma de três valores e mostra o resultado na tela.

    :param A: o primeiro valor
    :param B: o segundo valor
    :param C: o terceiro valor
    """
    s = a + b + c
    print(f"A soma é {s}")


help(soma2)
soma2(1, 4, 3)
soma2(3, 2)
print()


# Escopo de variaveis

def funcao():
    global n1  # se usar o comando global o n1 que esta no escopo local ira usar o escopo global que nesse caso é 2
    # fazendo assim o n1 que antes era 4 virar 2

    n1 = 4
    print(f"Funçao n1 dentro vale: {n1}")  # Escopo local


funcao()
n1 = 2  # escopo global
print(f"Funçao n1 fora vale: {n1}")


# return


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s  # retorna a variavel mais sem mostra-la podendo assim jogar em uma variavel exemplo abaixo


r1 = somar(2, 3, 5)
r2 = somar(3, 2, 1)
r3 = somar(1, 2)

print(f"Os resultados foram {r1}, {r2} e {r3}")


# return def de par ou impar

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input("Digite um numero: "))
if par(num):
    print("é par")
else:
    print("é impar")


# return def de factorial

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input("Digite um numero: "))
print(f"O fatorial de {n} é {fatorial(n)}")  # primeira forma de se usar

f1 = fatorial(4)
f2 = fatorial(5)    # segunda forma
f3 = fatorial(9)

print(f"O fatorial de é {f1}, {f2} e {f3}")
