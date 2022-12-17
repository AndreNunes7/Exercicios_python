pessoas = {"nome": "Gustavo ", "Sexo": "M", "Idade": 22}
print(f"O {pessoas['nome']}tem {pessoas['Idade']} anos")
print(pessoas.keys())
pessoas["nome"] = "leandro"  # serve para trocar um elemento no caso gustavo passa a ser leandro agora
pessoas["peso"] = 100.2  # Este mesmo comando serve para adicionar um elemento ao dicionario tambem
# del pessoas["Sexo"]     # para apagar um elemento dentro do dicionario
for k in pessoas.keys():  # para cada uma das chaves
    print(k)
print()

for k in pessoas.values():   # para cada chave em values
    print(k)
print()

for k, v in pessoas.items():    # para cada chave (k) e valor (v) em pessoas.items:
    print(f"{k} = {v}")
