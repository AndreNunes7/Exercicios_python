from utilidadescev import Moeda

# programa principal

n = float(input("Digite um preço: R$"))
print(f"A metade de {Moeda.cifrao(n)} é {(Moeda.metade(n))}")      # show False = nao mostra o dinheiro formatado
print(f"O dobro de {Moeda.cifrao(n)} é {(Moeda.dobro(n, show=True))}")    # show True mostra o dinheiro formatado
print(f"Aumentando 10%, temos: {(Moeda.aumento(n, show=True))} ")
print(f"Diminuindo 13%, temos: {(Moeda.diminui(n, show=True))}")

    # ira mostrar o dinheiro formatado ou nao dependendo da opçao do usuario True ou False