print("---- LOJA DA ECONOMIA ----")
totgasto = tot1000 = cont = totalmenor = 0
# variavel que vai receber o nome do produto!!
nome = ' '
while True:
    produto = str(input("Qual o nome do produto?: "))
    valor = float(input("Qual valor? R$: "))
    totgasto += valor
    # aqui o contador esta contando cada valor colocado!
    cont += 1
    continuar = ' '
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    # aqui é se o valor for mais de 1000 reais
    if valor > 1000:
        tot1000 += 1
    # aqui o produto que é mais barato é qual é o seu nome
    if cont == 1 or valor < totalmenor:  # ( se o contador for igual a 1 ou se o valor for menor que o totalmenor)
        totalmenor = valor
        nome = produto

        # else:
        # if valor < totalmenor:
        # totalmenor = valor           (codigo completo, porem o codigo acima é o mesmo porem simplificado )
        # nome = produto
        # if continuar == "N":

        print("----- Fim do Programa!! -----")
        break
print(f"Tem {tot1000} produto que custam mais de R$1000 reais!!  ")
print(f"O total gasto foi R${totgasto:.2f} reais!")
print(f"O produto mais barato é o {nome} e ele custa R${totalmenor:.2f}")
