temp = []
princ = []
cont = 0
mai = men = 0
while True:
    temp.append(str(input("Nome: ")))
    temp.append(float(input("Peso: ")))
    print("Pessoa cadastrada com sucesso!")
    cont += 1
    resp = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    if resp not in "SN":
        print("Resposta invalida tente novamente!")
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]

        if temp[1] < men:
            men = temp[1]
    princ.append((temp[:]))
    temp.clear()
    if resp in "Nn":
        print("Finalizando...")
        break
print(f"Foram registradas {cont} pessoas!")
print(f"O mair peso foi de {mai}Kg e a pessoa é :", end=" ")
for p in princ:
    if p[1] == mai:
        print(f"{p[0]}", end=" ")
print(f"\nO menor peso foi de {men}Kg e a pessoa é:", end=" ")
for p in princ:
    if p[1] == men:
        print(f"{p[0]}", end=" ")
