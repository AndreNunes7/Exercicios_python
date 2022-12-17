num = str(input("Digite sua expressão matematica: "))
lista = []
for sim in num:
    if sim == "(":
        lista.append("(")
    elif sim == ")":
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(")")
            break
if len(lista) == 0:
    print("Sua expressão esta valida!! ")
else:
    print("Sua expressão é invalida!! ")
