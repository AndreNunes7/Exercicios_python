jogador = {}
partidas = []
total_gols = 0
jogador['nome'] = str(input("Nome do jogador: "))
tot_partidas = int(input(f"Quantas partidas {jogador['nome']} jogou?: "))
for p in range(tot_partidas):
    partidas.append(int(input(f"    Quantos gols na partida {p + 1}: ")))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
print("-=" * 20)
for k, v in jogador.items():
    print(f"{k} tem valor: {v}")
print("-=" * 20)
print(f"O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas!")
for i, v in enumerate(jogador['gols']):
    print(f"     => Na partida {i + 1}, fez {v} gols.")
print(f"Foi um total de {jogador['total']} gols.")





