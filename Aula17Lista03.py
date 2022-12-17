a = [2, 3, 4, 5, 6]
b = a[:]     # mas se usar esse comando o A que esta dentro de B ira fazer uma copia dele mesmo fazendo com que nao
# altere seu valor
b[2] = 8     # a partir do momento que igualar uma lista na outra o python cria uma ligaçao entre elas dessa forma
# nesse caso o b[2] = 8 ira mexer nos valores dos dois A e B

print(f"Lista A: {a}")
print(f"Lista B: {b}")