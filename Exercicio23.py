num = int(input("Digite um numero: "))
u = num // 1 % 10
p = num // 10 % 10
q = num // 100 % 10
t = num // 1000 % 10
print("Analisando o numero...")
print("Unidade: {}".format(u))
print("dezena:  {}".format(p))
print("Centena: {}".format(q))
print("Milhar:  {}".format(t))
