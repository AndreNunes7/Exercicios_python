from time import sleep

print("---- Menu De Opções ----")
print("=-=" * 13)
primeiro = int(input("Digite o primeiro valor: "))
segundo = int(input("Digite o segundo: "))
escolha = 0
maior = 0
while escolha != 6:  # enquanto escolha for diferente de 5
    print("""[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NUMEROS
[5] DIVISAO
[6] SAIR DO PROGRAMA""")
    print("=-=" * 13)
    escolha = int(input(">>>>>> Qual sua ESCOLHA? "))
    print("\033[1;32mProcessando...\033[m")
    print("=-=" * 10)
    sleep(1)
    if escolha == 1:
        soma = primeiro + segundo
        print("A \033[1;31mSOMA\033[m entre {} + {} é igual a \033[1;36m{}\033[m".format(primeiro, segundo, soma))
        print("=-=" * 13)
        print("O que deseja fazer novamente?")
    elif escolha == 2:
        mult = primeiro * segundo
        print("A \033[1;31mMULTIPLICAÇÃO\033[m entre {} x {} é igual a \033[1;36m{}\033[m".format(primeiro, segundo,
                                                                                                  mult))
        print("=-=" * 13)
        print("O que deseja fazer novamente?")
    elif escolha == 3:
        if primeiro > maior:
            maior = primeiro
        if segundo > maior:
            maior = segundo
        print("O maior numero é {}".format(maior))
        print("=-=" * 13)
        print("O que deseja fazer novamente?")
    elif escolha == 4:
        print("Informe os numeros novamente!")
        primeiro = int(input("Digite o primeiro valor: "))
        segundo = int(input("Digite o segundo: "))
    elif escolha == 5:
        divisao = primeiro / segundo
        print(f"O resultado foi {divisao}")
        print("-=" * 13)
    elif escolha == 6:
        print("Fim do programa!")
        break
    sleep(1)
print("Volte sempre!!!")
