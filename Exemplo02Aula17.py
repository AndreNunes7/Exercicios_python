# valores = list()  # pode se criar uma lista assim <<<<<<<<
valores2 = []  # ou assim colocando os valores dentro do []
# valores2.append(9)
# valores2.append(2)
# valores2.append(3)
for cont in range(0, 6):  # pra cada cont de 0,6 faça :
    valores2.append(int(input("Digite um valor: ")))  # ele ira pegar os valores digitados é jogar dentro
    # da lista valores2


for c, v in enumerate(valores2):  # pra cada valor em valores2, o enumerate ira contar os valores o C é a
    # variavel do enumerate ele vai contar os numeros que ele achou em tal posição
    print(f"Na posiçao {c} encontrei o valor {v}")

