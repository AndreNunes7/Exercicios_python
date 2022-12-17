valor = float(input("Qual o valor da casa? "))
salario = float(input("Qual o valor do seu salario? "))
anos = int(input("Em quantos anos você ira pagar? "))
meses = anos * 12
parcelas = valor / meses
minimo = (salario / 100)*30
print("O valor da casa dividido em {} anos  e de {} parcelas".format(anos, meses))
if parcelas < minimo:
    print("Parabéns seu emprestimo será realizado ")
else:
    print("Sua prestação excedeu o limite de 30% do salario, o emprestimo foi cancelado!")