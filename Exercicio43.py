import time
p = float(input("Digite seu peso (Kg): "))
a = float(input("Digite  sua altura: "))
c = p / (a * a)
print("Carregando....")
time.sleep(1.1)
print("-="*20)
print("PESO DE ACORDO COM A TABELA IMC " )
print("-="*20)
if 18.5 <= c < 25:
 print("Seu peso é de {:.3} você esta na FAIXA DE PESO IDEAL!!".format(c))
elif c < 18.5:
    print("Seu peso é de {:.1f} você esta ABAIXO DO PESO IDEAL".format(c))
elif 25 <= c < 30:
    print("Seu peso é de {:.1f} você esta com SOBREPESO".format(c))
elif 30 <= c < 40:
    print("Seu peso é de {:.1f} Você esta com OBESIDADE".format(c))
else:
    v = c > 40
    print("SEU peso é de {:.1f} Você esta com OBESIDADE MORBIDA".format(c))