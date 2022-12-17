def ficha(nome=str("<desconhecido>"), gols=str(0)):
    if not gols.isnumeric():
        print(f"O jogador {nome} fez 0 gols no campeonato")

    elif nome == "" and gols == "":
        print(f"O jogador <desconhecido> fez 0 gols no campeonato")
        return

    elif nome == "":
        print(f"O jogador <desconhecido> fez {gols} gols no campeonato")
        return
    elif gols == "":
        print(f"O jogador {nome} fez 0 gols no campeonato")
        return
    else:
        print(f"O jogador {nome} fez {gols} gol(s) no campeonato!!")
        return


n = str(input("Nome do jogador?: "))
g = str(input("Quantos gols na temporada?: "))
ficha(n, g)
