# EXemplo de utilizaçao de dicionario

filme = {"Titulo": "Star Wars",
         "Ano": 1977,
         "Diretor": "George Lucca"
         }

print(filme.values())  # ira mostrar apenas os valores de cima Exemplo: Titulo , Ano , Diretor
print(filme.keys())  # ira mostrar os valores de baixo Exemplo: Star Wars, 1977, Geroge Lucca
print(filme.items())    # ira mostrar todos os elementos de cima e de baixo

for k, v in filme.items():  # ira fazer um for pegando todos os elementos de filme.items  o K é keys que é o valor
    # de baixo é V é o values que e o de cima
    print(f"O {k} é {v}")