galera = [["Ana", 19], ["Gabriel", 18], ["Andre", 19], ["beatriz", 45]]  # Aqui é outra forma para criar uma estrutura
# colocando uma grande estrutura dentro de pequenas gerando uma lista dentro da outra
for p in galera:  # ---->  "para cada pessoa em galera" , aqui ele ira gerar uma "lista" em colunas com o nome de
    # cada pessoa
    print(p[0]) # se quiser apenas os nomes e so usar [0] , se nao quiser basta tirar!

    print(f"{p[0]} tem {p[1]} anos de idade!")  # aqui é uma fstring formatada para mostrar o nome e a idade das pessoas
    # utilizando o p[0] mostra as pessoas no elemento 0 e p[1] mostra a idade que esta no elemento 1

print(galera[2][1])  # aqui é para escolher o que mostrar dentro dos elementos da lista
