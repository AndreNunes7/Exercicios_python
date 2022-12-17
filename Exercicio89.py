import time
ficha = []
print(f"{'-=' * 3} Calculador de MEDIA ESCOLAR {'-=' * 3}")
while True:
    print("-=" * 21)
    nome = str(input("Nome do aluno: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    print("-=" * 21)
    resp = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    if resp not in "SN":
        print("Resposta invalida tente novamente! ")
    if resp in "Nn":
        print("Obtendo resultados...")
        time.sleep(1)
        break
print("-=" * 21)
print(f"NO.{' '*7} NOME {' '* 7} MEDIA")
print("=" * 30)
for pessoas, i in enumerate(ficha):
    print(f"{pessoas:<10} {i[0]:<10} {i[2]:>7.1f}")
print("=" * 30)
while True:
    perg = int(input("Deseja ver alguma nota? [999 para sair]: "))
    if perg == 999:
        print("Finalizando .... \n"
              "Volte sempre! :D")
        break
    if perg <= len(ficha) - 1:
        print("-=" * 15)
        print(f"As notas de {ficha[perg][0]} são: {ficha[perg][1]}")
        print("-=" * 15)