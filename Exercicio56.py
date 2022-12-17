nomevelho = ""
maioridadehomem = 0
mediaidade = 0
somaidade = 0
cont = 0
for c in range(1, 5):
    print("----- {}° PESSOA -----".format(c))
    nome = str(input("Digite seu nome: ")).strip()
    idade = int(input("Sua idade: "))
    sexo = str(input("Seu sexo [M/F]: ")).strip().upper()
    somaidade += idade
    if sexo in "Ff" and idade < 20:
        cont += 1
    elif c == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomevelho = nome
    elif sexo in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
mediaidade = somaidade / 4
print("A  media de idade do grupo é de {} ".format(mediaidade))
print("Ao todo são {} mulheres com menos de 20 anos!".format(cont))
print("O homem mais velho se chama {} e tem {} anos!".format(nomevelho, maioridadehomem))
