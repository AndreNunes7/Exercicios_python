jogador = {}
partidas = []
lista = []
total_gols = 0
while True:
    jogador.clear()
    jogador['nome'] = str(input("Nome do jogador: "))
    tot_partidas = int(input(f"Quantas partidas {jogador['nome']} jogou?: "))
    partidas.clear()
    for p in range(tot_partidas):
        partidas.append(int(input(f"Quantos gols na partida {p + 1}?: ")))
        jogador['gols'] = partidas[:]
        jogador['total'] = sum(partidas)
    lista.append(jogador.copy())

    while True:
        rsp = str(input("Deseja continuar ? [S/N]: ")).upper()[0]
        if rsp in "SN":
            break
        print("ERRO! resposta invalida digite apenas S ou N")
    if rsp in "Nn":
        break


print("-=" * 20)
print("cod", end=' ')
for k in jogador.keys():
    print(f"{k:<14}", end='')
print()
print("-=" * 20)
for k, v in enumerate(lista):
    print(f"{k:<3} ", end='')
    for d in v.values():
        print(f"{str(d):<13}", end=' ')
    print()
print("-=" * 20)
while True:
    perg = int(input("Deseja ver as informaçoes de algum jogador? (999 para sair)!: "))
    if perg == 999:
        print("Finalizando...")
        break
    if perg >= len(lista):
        print(f"ERRO! Não existe jogador com o codigo {perg}")
    else:
        print("-=" * 20)
        print(f"-- Levantamento do jogador {lista[perg]['nome']}:")
        for i, g in enumerate(lista[perg]['gols']):
            print(f"----> Na partida {i + 1} fez {g} gols")
    print("-=" * 20)
print("<<< ENCERRADO >>>")