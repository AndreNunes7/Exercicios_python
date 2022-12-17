estado = {}
brasil = []
for c in range(0, 3):
    estado["Uf"] = str(input("Unidade federativa: "))
    estado["Sigla"] = str(input("Sigla do Estado: "))
    brasil.append(estado.copy())    # utiliza - se o (.copy) para fazer uma copia dos dados semelhante ao (:)
    # porem no dicionario nao pode usar o (:)
print(brasil)
for e in brasil:
    # print(e)
    for k, v in e.items():  # 1° opçao
        print(f"O campo {k} tem valor de {v}")
    for v in e.values():  # 2° opçao
        print(v, end=' ')
    print()