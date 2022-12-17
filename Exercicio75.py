num = int(input("Digite o 1° valor: ")), int(input("Digite o 2° valor: ")), int(input("Digite o 3° valor: ")), \
      int(input("Digite o 4° valor: "))
print(f"Os valores digitados foram: {num}")
print(f"Apareceu o numero 9, {num.count(9)} vezes!")
if 3 in num:
    print(f"O numero 3 apareceu na {num.index(3) + 1}° posição")
else:
    print("O valor 3 nao foi digitado!")
print(f"Os numeros pares foram:", end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
