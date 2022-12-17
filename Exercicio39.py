import time
from datetime import date

ano = date.today().year
atual = int(input("Digite o seu ano de nascimento: "))
idade = ano - atual
print("\033[1;36mProcessando...\033[m")
time.sleep(1.3)
print("Quem nasceu em {} tem {} anos em {}".format(atual, idade, ano))
if idade == 18:
    print("Você deve se apresentar para o alistamento IMEDIATAMENTE!")
elif idade < 18:
    tempo = 18 - idade
    falta = ano + tempo
    print("Você ainda não deve se apresentar para o alistamento! ainda faltam {} ano.".format(tempo))
    print("Seu alistamento será em {} ".format(falta))
elif idade > 18:
    tempo = idade - 18
    falta = ano - tempo
    print("Você ja passou do prazo para se alistar! Você deveria ter se apresentado há {} anos.".format(tempo))
    print("Seu alistamento foi em {} ".format(falta))
