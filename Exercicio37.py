import time
n = int(input("Escreva um numero inteiro: "))
print("Digite 1 para binario \n 2 para Octal \n 3 para Hexadecimal")
e = int(input("Qual o numero escolhido? "))
print("Aguarde....")
time.sleep(1.5)
if e == 1:
    print("A conversão do numero ficará: {}".format(bin(n)[2:]))
elif e == 2:
    print("A conversão do numero ficará: {}".format(oct(n)[2:]))
elif e == 3:
    print("A conversão do numero ficará: {} ".format(hex(n)[2:]))
else:
    print("Você escolheu uma opção invalida!")
