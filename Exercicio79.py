#  valores unicos em uma lista
lista = []
print("----- CONSULTANDO VALORES -----")
print("-=" * 18)
resp = ' '
while True:
    valor = int(input("Digite um valor: "))
    if valor not in lista:
        lista.append(valor)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado não adicionado!")
    resp = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    if resp not in "SN":
        print("Digito invalido tente novamente!")
    if resp in "Nn":
        print("Finalizando...")
        break
print("-="*20)
lista.sort()
print(f"Você digitou os numeros: {lista}")
