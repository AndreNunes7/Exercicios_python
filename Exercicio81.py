lista = []
while True:
    print("-="*15)
    num = int(input("Digite um numero: "))
    lista.append(num)
    print("-="*15)
    resp = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    if resp not in "SN":
        print("Opção invalida! tente novamente!")
    if resp in "Nn":
        print("Finalizando...")
        break
print("-="*20)
if 5 in lista:
    print("Existe o numero 5 na lista!")
else:
    print("Nao existe o numero 5 na lista!")
print(f"Foram digitados {len(lista)} numeros!")
print(f"A lista em forma decrescente é: {sorted(lista,reverse=True)}")
