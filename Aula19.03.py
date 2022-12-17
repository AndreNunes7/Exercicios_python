# criando um dicionario dentro de uma lista
brasil = []
estado1 = {"uf": "Rio de Janeiro", "Sigla": "RJ"}  # 0
estado2 = {"Uf": "Sao paulo", "Sigla": "SP"}    # 1
brasil.append(estado1)  # posiçaoo 0
brasil.append(estado2)  # posiçao 1
print(brasil[0]["Sigla"]) 