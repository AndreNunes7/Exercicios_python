import time
v = float(input("Digite a velocidade do carro: "))
print("Processando...")
time.sleep(3)
if v >= 80:
    d = (v-80) *7
    print("Você está acima do limite permitido! você foi multado em R${:.1f}".format(d))
else:
      print("Você esta no limite permitido parabéns!")
