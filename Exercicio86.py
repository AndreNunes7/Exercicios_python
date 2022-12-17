matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#  for abaixo é pra adicionar os valores
for L in range(0, 3):   # para cada linha[L] in range(0,3) faça:
    for c in range(0, 3):   # para cada coluna[c] in range(0,3) faça:
        matriz[L][c] = int(input(f"Digite um valor na posiçao [{L, c}]: "))
print("-="*19)
#   for abaixo é para mostrar a estrutura!
for L in range(0, 3):   # REPETIÇAO do for acima para mostra o resultado !
    for c in range(0, 3):
        print(f"[{matriz[L][c]:^5}]", end=' ')
    print()
