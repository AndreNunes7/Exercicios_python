num = [0, 2, 5, 1]
num[0] = 10  # substitui um valor no caso no numero 0 ira ficar o 10
num.append(1)  # adiciona um numero na ultima posiçao
num.sort(reverse=True)  # coloca os numeros em ordem reversa
num.insert(2, 2)  # adiciona um valor no lugar de outro nesse caso na posição 1 ira colocar o 3 e o numero que estava
# vai para direita ou esquerda
num.pop()  # elimina o ultimo valor
if 4 in num:  # se tiver 4 em num ele remove o 4
    num.remove(4)  # remove um valor especificado se ja houver um numero semelhante ele remove o primeiro
# da esquerda pra direita
else:
    print("Nao achei numero 4 na sequencia!")
print(num)
print(f"Essa função tem {len(num)} elementos!")