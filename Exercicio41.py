from datetime import date
atual = date.today().year
nascimento = int(input("Digite seu ano de nascimento: "))
idade = atual - nascimento
print("O atleta tem {} anos ".format(idade))
if idade <= 9:
    print("Classificação: MIRIM")
elif idade <= 14:
    print("Classificação: INFANTIl")
elif idade <= 19:
    print("CLassificação: JUNIOR")
elif idade <= 25:
    print("Classificação: SENIOR")
elif idade > 25:
    print("Classificação: MASTER")