from utilidadescev import Dado


def painel():
    print("\033[32m-\033[m" * 42)
    print(f"\033[1;31m{'MENU PRINCIPAL':^35}\033[m")
    print("\033[32m-\033[m" * 42)


def menu(lista):
    c = 1
    for i in lista:
        print(f"\033[1;33m{c} -\033[m \033[1;34m{i}\033[m")
        c += 1
    print('\033[32m-\033[m' * 42)
    rsp = Dado.leiaInt2("\033[1;33mSua opção >>> \033[m")
    return rsp


def traco():
    print("\033[32m-\033[m" * 42)


def ArquivoExiste(txt):
    try:
        a = open(txt, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        print(f"Arquivo {txt} aberto com sucesso!")
        return True


def abrir(txt):
    try:
        a = open(txt, "wt+")
        a.close()
    except:
        print("ERRO ao abrir o arquivo!")
    else:
        print(f"O arquivo {txt} foi criado com sucesso!")


def ler(txt):
    try:
        a = open(txt, "rt")
    except:
         print("Erro ao ler o arquivo!")
    else:
        print("Pessoas Cadastradas:".center(35))
        for l in a:
            dado = l.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f"Nome: {dado[0]:<15} Idade: {dado[1]:>3} anos")
    finally:
        a.close()


def cadastra(Arquivo, nome='desconhecido', idade=0):
    try:
        a = open(Arquivo, "at")
    except:
        print("ERRO na abertura dos dados!")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print("Erro nos dados inseridos!!")
        else:
            print(f"Novo registro de {nome} Adicionado com sucesso!")
            a.close()
