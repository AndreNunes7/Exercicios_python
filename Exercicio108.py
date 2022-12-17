from utilidadescev import Moeda

# programa principal

n = float(input("Digite um preço: R$"))
print(f"A metade de {Moeda.cifrao(n)} é {Moeda.cifrao(Moeda.metade(n))}")
# ira mostrar o dinheiro formatado para reais
print(f"O dobro de {Moeda.cifrao(n)} é {Moeda.cifrao(Moeda.dobro(n))}")
print(f"Aumentando 10%, temos: {Moeda.cifrao(Moeda.aumento(n))}")
print(f"Diminuindo 13%, temos: {Moeda.cifrao(Moeda.diminui(n))}")
