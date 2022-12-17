matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = sterc = maiorsegunda = 0
#  for abaixo é pra adicionar os valores
for L in range(0, 3):   # para cada linha[L] in range(0,3) faça:
    for c in range(0, 3):   # para cada coluna[c] in range(0,3) faça:
        matriz[L][c] = int(input(f"Digite um valor na posiçao [{L, c}]: "))
print("-="*19)
#   for abaixo é para mostrar a estrutura!
for L in range(0, 3):   # REPETIÇAO do for acima para mostra o resultado !
    for c in range(0, 3):
        print(f"[{matriz[L][c]:^5}]", end=' ')
        if matriz[L][c] % 2 == 0:
            spar += matriz[L][c]
    print()
print("-="*20)
print(f"A soma dos valores pares é {spar}")
for L in range(0, 3):
    sterc += matriz[L][2]
print(f"A soma dos numeros da TERCEIRA coluna é {sterc}")
for c in range(0, 3):
    if matriz[1][c] > maiorsegunda:
        maiorsegunda = matriz[1][c]
print(f"O maior valor da SEGUNDA LINHA é {maiorsegunda}")
