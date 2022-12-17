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


n = leiaInt2("Digite um numero inteiro: ")
fl = leiafloat("Digite um numero real: ")
print(f"\033[1;30;42mOs numeros digitados foram: inteiro: {n} real: {fl}\033[m")
