aluno = {}
aluno["Nome"] = str(input("Nome do aluno: "))
aluno["media"] = float(input("Media : "))
for v in range(0, 1):
    print(f"O nome do aluno é {aluno['Nome']}"
          f"\nA media é igual a {aluno['media']}")
if aluno["media"] >= 7:
    aluno['Situação'] = "Aprovado"
elif 5 <= aluno['media'] < 7:
    aluno['Situação'] = "Recuperação"
else:
    aluno['Situação'] = "Reprovado!"
print()
for k, v in aluno.items():
    print(f"  -{k} é: {v}")
