
def leiadinheiro(txt):
    check = False

    while not check:    # enquanto nao checar
        entrada = str(input(txt)).replace(",", ".").strip()
        if entrada.isalpha() or entrada == "":
            print(f"\033[0;31mErro o valor \'{entrada}\' nao é um valor correspondente!\033[m")
            # aparece uma mensagem de erro
        else:
            check = True
            return float(entrada)   # retorna o valor float da entrada


def leiaint(n):
    check = False
    valor = 0
    while True:
        n = str(input(n))
        if n.isnumeric():
            valor = int(n)
            check = True
        else:
            print("Você precisar digitar apenas numeros!!: ")
        if check:
            break
    return valor




def leiaInt2(n):
    while True:

        try:
            n = int(input(n).strip())

        except (ValueError, TypeError):
            print(f"\033[0;31mERRO!! O valor INTEIRO digitado nao é valido.\033[m")
            continue
        except (KeyboardInterrupt):
            print("O usuario decidiu não colocar valor !!")

            return 0
        else:
            return n


def leiafloat(n):
    while True:

        try:
            n = float(input(n).strip())

        except (ValueError, TypeError):
            print("\033[0;31mERRO!! O valor REAL nao é valido.\033[m")
            continue
        except KeyboardInterrupt:
            print("O usuario deciniu nao colocar valor!!")
            return 0

        else:
            return n