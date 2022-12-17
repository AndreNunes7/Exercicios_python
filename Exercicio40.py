n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
r = (n1 + n2) / 2
if r >= 7.0:
    print("Parabéns você foi aprovado sua nota é de {}".format(r))
elif r < 5.0:
    print("Sua media esta abaixo de {} você foi reprovado!".format(r))
elif r == 6.9 or 5.0:
    print("Sua nota foi {} você esta de recuperação".format(r))
