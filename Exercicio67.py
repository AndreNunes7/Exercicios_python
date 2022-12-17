while True:
    print("--"*20)
    num = int(input("Digite um numero para ver sua tabuada: "))
    if num < 0:
        break
    print("--" * 20)
    for c in range(1, 11):
        mult = num * c
        print(f"{num} x {c} = {mult}")
print("Programa encerrado!")
# programa se encerra quando o valor digitado for menor que 0
