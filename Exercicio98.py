import time


def contador(inicio, fim, passo):
    print("-=" * 20)
    print(f"Contador de {inicio} ate {fim} pulando de {passo} em {passo}: ")
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1  # aqui é para jogar o numero para negativo
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f"{cont}", end=' ')
            time.sleep(0.25)
            cont += passo
        print("FIM!!")

    else:

        cont = inicio
        while cont >= fim:
            print(f"{cont}", end=' ')
            time.sleep(0.25)
            cont -= passo
        print("FIM!!")
        print("-=" * 20)


# programa principal


contador(1, 10, 1)
contador(10, 0, 2)
print("Agora é sua vez de personalizar a contagem: ")
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)
