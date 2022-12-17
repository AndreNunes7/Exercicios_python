maior18 = conthomem = contmulher = 0
print("-="*20)
print("Cadastramento pessoal...")
print("-="*20)
while True:
    idade = int(input("Digite sua idade: "))
    sexo = ' '
    while sexo not in "MF":
        sexo = str(input("Digite seu sexo [M/F]: ")).strip().upper()[0]
    continuar = ' '
    while continuar not in "SN":
        continuar = str(input("Deseja continuar cadastrando? [S/N]: ")).strip().upper()[0]
    if idade >= 18:
        maior18 += 1
    if sexo == "M":
        conthomem += 1
    if sexo == "F" and idade < 20:
        contmulher += 1
    if continuar == "N":
        print("Finalizando...")
        break
print(f"Foram cadastrados {maior18} PESSOAS maiores de 18!")
print(f"Tem {contmulher} MULHERES menores de 20")
print(f"Foram cadastrados {conthomem} HOMENS!!")