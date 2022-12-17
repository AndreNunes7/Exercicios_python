tot = 0
t = int(input("Digite um numero: "))
for c in range(1, t + 1):
    if t % c == 0:
        print("\033[33m", end=' ')
        tot += 1
    else:
        print("\033[31m", end=' ')
    print("{}".format(c), end= ' ')
print("\n\033[mO numero {} foi divido {} vezes!".format(t, tot))
if tot == 2:
    print("E por isso ele é primo!")
else:
    print("E por isso ele nao é primo!")