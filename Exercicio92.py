from datetime import datetime
dados = {}


dados['nome'] = str(input("Digite seu nome completo: "))
ano = int(input("Ano de nascimento: "))
dados['idade'] = datetime.now().year - ano
dados['ctps'] = int(input("Carteira de trabalho [tecle 0 se não tiver]:  "))
if dados['ctps'] == 0:
    print('-=' * 15)
    print(" == SEUS DADOS: ==")

    for k, v in dados.items():
        print(f"  - {k}:  {v}")
else:
    if dados['ctps'] != 0:
        dados['contrataçao'] = int(input("Ano de contratação: "))
        dados['Aposentadoria'] = dados['idade'] + ((dados['contrataçao'] + 35) - datetime.now().year)   # isto serve
        # para calcular quantos anos faltam para a aposentadoria

        dados['Salario'] = float(input("Qual seu salario?: R$"))
    print('-=' * 15)
    print("  == SEUS DADOS  ==")

    for k, v in dados.items():
        print(f"  - {k}:  {v}")

    if dados['idade'] > 35:
        print('-=' * 15)
        print("Você ja pode se aposentar ")
    else:
        print('-=' * 15)
        print("Você ainda nao pode se aposentar! ")
print('-=' * 15)
