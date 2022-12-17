lista = []
dicionario = {}
cont = soma_idade = 0
todas_mulheres = []

while True:
    dicionario.clear()
    dicionario['nome'] = str(input("Digite o nome: "))
    dicionario['sexo'] = str(input("Sexo [M/F]: ")).strip().upper()[0]
    if dicionario['sexo'] not in "MmFf":
        print("ERRO! Digito invalido, digite M ou F.")
        dicionario['sexo'] = str(input("Sexo [M/F]: ")).strip().upper()[0]
    dicionario['idade'] = int(input("Idade: "))
    soma_idade += dicionario['idade']
    lista.append(dicionario.copy())
    print("Pessoa cadastrada com sucesso!")
    cont += 1
    rsp = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    if rsp not in "SN":
        print("Opção invalida tente novamente! ")
        rsp = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    if rsp == "N":
        print("Finalizando...")
        break
result = soma_idade / cont
print("-=" * 25)
print("              << RESULTADOS >>")

print("-=" * 25)
print(f"A)  Ao todo foram cadastradas {cont} pessoas!")
print("-=" * 25)
print(f"B)  A media de idade do grupo é de {result:5.2f} anos")
print("-=" * 25)
print("C) Lista somente com as mulheres: ")
for k, p in enumerate(lista):
    if p['sexo'] in "Ff":

        print(f"- Mulher N°{k}... - {p['nome']}")
print("-=" * 25)
print("D) Lista com idade acima da media: ")
for p in lista:
    if p['idade'] >= result:

        print("", end=' ')
        for k, v in p.items():
            print(f"-{k} = {v};", end=' ')
        print()
print("-=" * 25)

