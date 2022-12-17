teste = list()
teste.append("Andre")
teste.append("18")
galera = list()  # aqui é criado uma lista para colocar em outra lista
galera.append(teste[:])  # lista dentro da lista <<<--------
teste[0] = "Jose"  # aqui é trocar a posição no caso "andre" passara a ser "jose"
teste[1] = "20"  # aqui para trocar a idade
galera.append(teste[:])  # se caso deixar sem o [:] ele ira fazer uma ligação entre as duas estruturas, mas se utilizar
# o [:] ele ira criar uma "copia" fazendo assim com que mostre na tela sem repetir os que ja foram
print(galera)
