lista_impar = []
lista_par = []
lista_todos = []
while True:
    print("-="*20)
    num = int(input("Digite um numero: "))
    print("-=" * 20)
    lista_todos.append(num)
    resp = str(input("Você quer continuar? [S/N]: ")).strip().upper()[0]
    if resp not in "SN":
        print("Opção invalida! Tente novamente")
    if (num % 2) == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)
    if resp in "Nn":
        print("Finalizando...")
        break
print("-="*20)
print(f"Todos os valores digitados foram: {lista_todos}! ")
print(f"Os valores pares digitados foram: {lista_par}")
print(f"Os valores impares digitados foram: {lista_impar}")
