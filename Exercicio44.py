import time
print("{:=^40}".format(" LOJAS NUNES "))
v = float(input("Qual o Valor da compra? R$ "))
print("Escolha uma opção de pagamento!")
print(" [ 1 ] a vista dinheiro/cheque \n [ 2 ] a vista cartão \n [ 3 ] 2x no cartão \n [ 4 ] 3x ou mais no cartão ")
o = int(input("Digite sua escolha: "))
print("Processando...")
time.sleep(1.1)
if o == 1:
    c = v - (v * 10 / 100)
    print("O valor a vista ficará {} com desconto de 10%".format(c))
elif o == 2:
    c = v - (v * 5 / 100)
    print("O valor com pagamento em cartão ficara {} com desconto de 5% ".format(c))
elif o == 3:
    c = (v / 2)
    print("O valor pagando em 2x sem juros no cartão ficara {}".format(c))
elif o == 4:
    total = v + (v * 20 / 100)
    parc = int(input("Quantas parcelas?: "))
    parcela = (total / parc)
    print("Sua compra sera parcelada em {}x de R${:.2f}".format(parc, parcela))
    print("Sua compra de {:.2f} ira custar R${:.2f} com juros no final ".format(v, total))
else:
    print("Opção invalida tente novamente!")
