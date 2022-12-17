from time import sleep

cores = [
    "\033[m",  # 0 - sem cor
    "\033[0;30;41m",  # 1 - vermelho
    "\033[0;30;42m",  # 2 - verde
    "\033[0;30;43m",  # 3 - Amarelo
    "\033[0;30;44m",  # 4 - Azul
    "\033[7;40m"  # 5 - Branco
]


def ajuda(txt):
    titulo(f"Acessando manual do comando \'{txt}\'", 4)
    print(cores[5], end='')
    help(txt)
    print(cores[0], end='')


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print("~" * tam)
    print(f"  {msg}")
    print("~" * tam)
    print(cores[0], end='')
    sleep(1)


# programa principal


comando = ''
while True:

    titulo("SISTEMA DE AJUDA PYHELP", 2)
    comando = str(input("Função ou biblioteca > "))
    if comando.upper() == "SAIR":
        break
    else:
        ajuda(comando)
titulo("Fim!! ", 1)
