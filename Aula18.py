dados = []
pessoas = []
pessoas.append(dados[:])  # : aqui vc consegue criar uma copia de uma lista que ja existe e jogar toda a
# estrutura dentro dela, gerando uma lista dentro de outra lista

pessoas = [["pedro", 25], ["maria", 19]]  # aqui você consegue declarar a estrutura de uma vez só
print(pessoas[0][0])  # serve para printar na tela o elemento zero e o que esta na posição zero
print(pessoas[1]) # vai mostrar todos os itens que estao dentro da lista
