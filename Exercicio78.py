valores = []

for pos in (range(0, 5)):
    valores.append(int(input(f"Digite um numero na posição {pos}: ")))
print(f"Você digitou os numeros {valores}")
print(f"O maior numero é {max(valores)} na posição: ", end=' ')
for c, v in enumerate(valores):
    if v == max(valores):
        print(f"{c}...", end=' ')
print(f"\nO menor valor é {min(valores)} na posição:  ", end=' ')
for c, v in enumerate(valores):
    if v == min(valores):
        if v == min(valores):
            print(f"{c}...", end=' ')
