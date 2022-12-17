distancia = float(input("Qual a distancia da sua viagem? "))
print("Voce esta prestes a começar uma viagem de {}km ".format(distancia))
if distancia <= 200:
        p = distancia * 0.50
else:
        p = distancia * 0.45

print("E o preço da sua passagem sera de R${:.2f}".format(p))