#   Obs>:  SEMPRE AO USAR O DEF PULE 2 LINHA EMBAIXO DO COMANDO

def lin():  # este comando serve para simplificar, neste caso o print("-"), ele serve para criar rotinas e
    # comandos personalizados
    print("-" * 30)


lin()  # aqui é a variavel lin que esta carregando o comando print("-"), fazendo assim simplificar este comando
print(f"{'Aprendendo...':^30}")
lin()


def titulo(txt):  # outra forma de usar o def
    print("-" * 30)
    print(txt)
    print("-" * 30)


#   cada um dos nomes dentro de titulo ira ser armazenado dentro de (txt), e sera mostrado em ordem pela funçao def
#   azendo assim simplica-la


titulo("Aluno")
titulo("Curso")
titulo("OI")


def soma(a, b):  # outra forma de se usar o def dessa vez para criar uma simplificaçao de uma soma,
    print("-" * 30)
    print(f"A = {a} e B = {b}")
    s = a + b
    print(f"A soma entre A + B é {s}")  # pode tambem usar uma F string dentro do def
    print("-" * 30)


soma(a=10, b=2)  # posso tambem deixar explicito qual valor é o (a) e qual valor é o (b), desta forma
soma(3, 4)
soma(1, 2)


def contador(*num):  # este este parametro serve para dizer que ao def que ira receber varios numeros

    print(num)  # dessa forma ele ira mostrar todos os numeros dentro de uma tupla!!

    for valor in num:  # dessa forma ele ira organizar os numeros fora da tupla ficando melhor a visualizaçao
        print(f"{valor}", end=' ')
    print("Fim")  # aqui é um quebra linha somente no final!

    tam = len(num)  # este metodo pode se usar para contar quantos numeros tem usando o LEN
    print(f"Recebi os valores {num} e sao ao todo {tam}")
    print("-" * 30)


contador(4, 3, 2)
contador(2, 1)
contador(1, 2, 4, 5, 6, 7)


def dobro(lst):  # utilizando a funçao def com lista, fazendo dobrar os valores que estao dentro dela!!
    pos = 0
    while pos < len(lst):  # enquanto pos for menor que len na posiçao da lista(lst)
        lst[pos] *= 2  # aqui é onde esta fazendo a conta para dobrar
        pos += 1


valores = [4, 5, 6, 7, 10]
dobro(valores)
print(valores)


def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f"A soma entre os valores {valores} é {s}")


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
