galera = []  # lista primaria
dado = []  # lista secundaria
totmaior = totmen = 0
for c in range(0, 3):
    dado.append(str(input("Nome: ")))  # ler o nome
    dado.append(float(input("Idade: ")))  # Ler a idade
    galera.append(dado[:])  # jogando os dados dentro da "galera" e com uma copia [:]
    dado.clear()  # excluindo o dado para ir pro proximo
# print(galera)
for p in galera:
    if p[1] >= 21:  # se p[1] que no caso é a idade for maior igual a 21 faça:
        print(f"{p[0]} é maior de idade!")
        totmaior += 1
    else:
        print(f"{p[0]} é menor de idade!")
        totmen += 1
print(f"Temos {totmaior} maiores de idade e {totmen} menores de idade!")