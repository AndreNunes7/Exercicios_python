from utilidadescev import Moeda

# programa principal

n = float(input("Digite um preço: R$"))
print(f"A metade de {n} é {(Moeda.metade(n))}")        # programa ira mostrar os calculos pedidos
print(f"O dobro de {n} é {(Moeda.dobro(n))}")
print(f"Aumentando 10%, temos: {(Moeda.aumento(n))} ")
print(f"Diminuindo 13%, temos: {(Moeda.diminui(n))}")
