import time
from utilidadescev import Sistema
from utilidadescev import Dado



# programa principal
Arquivo = "MeuMenuPy.txt"
if not Sistema.ArquivoExiste(Arquivo):
    Sistema.abrir(Arquivo)





while True:
    Sistema.painel()
    resposta = Sistema.menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    print("\033[32m-\033[m" * 42)
    if resposta == 1:
        print(f"\033[31m{f'A opção escolhida foi {resposta}'.center(35)}\033[m")
        Sistema.ler(Arquivo)
        Sistema.traco()

    elif resposta == 2:
        print(f"\033[31m{f'A opção escolhida foi {resposta}'.center(35)}\033[m")
        print("Adicione os dados do usuario: ".center(35))
        print()
        nome = str(input("Nome: "))
        idade = Dado.leiaint("Idade: ")
        Sistema.cadastra(Arquivo, nome, idade)




        Sistema.traco()
    elif resposta == 3:
        print("\033[31mSaindo do sistema!!! ....\033[m".center(50))
        Sistema.traco()
        time.sleep(1.)
        break
    else:
        print(f"\033[31mOpção invalida tente novamente!!\033[m")
    time.sleep(2)
