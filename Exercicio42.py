t1 = float(input("Digite um segmento: "))
t2 = float(input("Digite o segundo segmento: "))
t3 = float(input("Digite o terceiro segmento: "))
if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    print("Os segmentos acima  podem formar um triangulo!", end=' ')
    if t1 == t2 == t3:
        print("EQUILATERO")
    elif t1 != t2 != t3 != t1:
        print("ESCALENO")
    else:
        print("ISÓSCELES")
else:
    print("Os segmentos acima nao podem formar um TRIANGULO!")
