produtos = "Jujuba", 8.50, \
           "Arroz", 14.50, \
           "Feijao", 15.90, \
           "Carne", 28.90, \
           "Molho", 8.30, \
           "Ovo", 10.00, \
           "Mandioca", 7.50, \
           "Macarrão", 12.35  # cada numero é impar!!! lembra-se que jujuba no caso é par e o numero impar, assim por
# diante
print("-="*20)
print(f'{"LISTA DE PREÇOS":^40}')
print("=-" * 20)
for p in range(0, len(produtos)):  # o len esta servindo para contar

    if p % 2 == 0:  # aqui ele esta vendo se os produtos dentro da variavel produtos sao par
        print(f"{produtos[p]:.<30}R$:", end=' ')
    else:
        print(f"{produtos[p]:>3.2f}")  # aqui se eles nao forem par sao impares e coloca eles para a direita formatado
print("-=" * 20)
