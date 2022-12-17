r = str(input("Digite algo"))
t = str(input("Digite outro"))
f = (r.isalpha()), (t.isalpha())
print("A primeira letra é {} e a segunda letra é {} o formato é {}".format(r, t, f))


n1 = float(input("Digite seu saldo r$:"))
p = n1 / 3.27
print("Seu saldo atual é de {}! a conversâo minima atual é de R$3,27".format(n1,))
print("Você pode comprar {:.2f}! dolares".format(p))




v = int(input("Digite um valor ?"))
a = v + 1
b = v - 1
print("o antecessor é {} o principal é {} e o sucessor é {}".format(b,v,a))



n = int(input("O numero é :"))
d = n*2
r = n ** (1/2)
t = n*3
print("o Dobro do numero é: \033[4;35m{}\033[m \n a raiz quadrada é: \033[4;31m{:.2f}\033[m \n e o triplo seria: \033[4;36m{}\033[m".format(d, r, t))



n1 = float(input("Qual a primeira nota?"))
n2 = float(input("Qual a segunda nota?"))
s = n1 + n2
r = s / 2
print("A media final do aluno foi {}!".format(r))



salario = int(input("Qual seu salario atual? "))
a = input("o aumento dado pela empresa é de 15% deseja aceitar?")
aumento = 15
print(salario + (salario * aumento / 100))


print('\033[1;35m''-=' * 20)
num = int(input("Digite um numero para ver sua tabuada: "))
print("\033[1;33m{} x {:2} = \033[1;31m{} ".format(num, 1, num * 1))
print("\033[1;33m{} x {:2} = \033[1;31m{} ".format(num, 2, num * 2))
print("\033[1;33m{} x {:2} = \033[1;31m{} ".format(num, 3, num * 3))
print("\033[1;33m{} x {:2} = \033[1;31m{} ".format(num, 4, num * 4))
print("\033[1;33m{} x {:2} = \033[1;31m{} ".format(num, 5, num * 5))
print("\033[1;33m{} x {:2} = \033[1;31m{} ".format(num, 6, num * 6))
print("\033[1;33m{} x {:2} = \033[1;31m{} ".format(num, 7, num * 7))
print("\033[1;33m{} x {:2} = \033[1;31m{}".format(num, 8,  num * 8))
print("\033[1;33m{} x {:2} = \033[1;31m{}".format(num, 9,  num * 9))
print("\033[1;33m{} x {:2} = \033[1;31m{}\033[m".format(num, 10, num * 10))
print('\033[1;35m''-='*20)



novo = float(input("Digite um valor para saber o desconto, R$"))
p = novo - (novo * 5 / 100)
print("o preço normal é {:.2f} e com desconto fica {:.2f}".format(novo, p))


import math
n = float(input("Digite um numero: "))
print("O numero digitado tem sua parte inteira representada em {:.0f} ".format(math.floor(n)))




import random
a1 = str(input("Digite o nome do primeiro aluno:"))
a2 = str(input("Digite o nome do segundo aluno:"))
a3 = str(input("Digite o nome do terceiro aluno:"))
a4 = str(input("Digite o nome do quarto aluno:"))
lista = random.choice([a1, a2, a3, a4])
print("O sorteado foi {}!".format(lista))





from math import hypot
co = float(input("Comprimento do cateto oposto:"))
ca = float(input("Comprimento do cateto adjacente:"))
hi = hypot(co, ca)
print("a hipotenusa vai medir {}".format(hi))




from math import sin, tan, radians, cos
angulo = float(input("Digite o valor do angulo :"))
seno = sin(radians(angulo))
coseno = cos(angulo)
tan = tan(radians(angulo))
print("o SENO é {:.2f} e o COSENO é {:.2f} e a tangente é {:.2f}".format(seno, coseno, tan))





nome = str(input("Digite seu nome completo: ")).strip()
q = len(nome) - nome.count(' ')
u = nome.upper()
l = nome.lower()
p = len(nome.split()[0])
print("Seu nome é: {:^} \ncom letra maiusculas fica: {:^} \ne com minusculas fica: {:^}".format(nome, u, l))
print("Seu nome completo tem {} letras ".format(q))
print("Seu primeiro nome tem: {}".format(p))




cidade = str(input("Digite o nome da sua cidade: ")).strip()
print(cidade[:5].upper() == 'SANTO' )


nome = str(input("Digite seu nome: "))
n ='silva' in nome.lower()
print("Seu nome é: {} portanto ele é: {}".format(nome,n))


nome = str(input("Digite seu nome: ")).strip()
n = nome.split()
print("Primeiro nome: {}".format(n[0]))
print("ultimo nome: {}".format(n[3]))



num = int(input("Digite um numero: "))
u = num // 1 % 10
p = num // 10 % 10
q = num // 100 % 10
t = num // 1000 % 10
print("Analisando o numero...")
print("Unidade: {}".format(u))
print("dezena:  {}".format(p))
print("Centena: {}".format(q))
print("Milhar:  {}".format(t))



q = str(input("Digite uma frase: ")).upper()
print("Analisando...")
print("A  letra A aparece {} vezes na frase.".format(q.count('A')))
print("A primeira letra A aparece na posição: {}".format(q.find('A')+1))
print("A ultima letra A aparece na posição: {} ".format(q.rfind('A')+1))




import random
e = int(input("Digite um numero de 1 ate 5: "))
print("Analisando...")
s = random.choice([1, 5])
random.shuffle([s])
if e == s:
    print("O numero era {} VOCÊ ACERTOU PARABENS!".format(s))
else:
    print("Você errou, o numero escolhido era: {}".format(s))







n = int(input("Digite um numero "))
if (n % 2 ) == 0:
    print("Par")
else:
    print("impar")






distancia = float(input("Qual a distancia da sua viagem? "))
print("Voce esta prestes a começar uma viagem de {}km ".format(distancia))
if distancia <= 200:
        p = distancia * 0.50
else:
        p = distancia * 0.45

print("E o preço da sua passagem sera de R${:.2f}".format(p))




import time
v = float(input("Digite a velocidade do carro: "))
print("Processando...")
time.sleep(3)
if v >= 80:
    d = (v-80) *7
    print("Você está acima do limite permitido! você foi multado em R${:.1f}".format(d))
else:
      print("Você esta no limite permitido parabéns!")





from datetime import  date
ano = int(input("Qual o ano? Coloque 0 para analisar o ano atual: "))
if ano ==0:
    ano= date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print("{} é um ano bissexto".format(ano))
else:
    print("{} não é um ano bissexto!".format(ano))












n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
n3 = int(input("Digite o terceiro valor: "))
#maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
print("O maior valor é {}".format(maior))
#menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3
print("O menor valor é {}".format(menor))












import time
v = float(input("Qual o seu salario atual?: "))
print("Analisando...")
time.sleep(1.5)
if v > 1250:
    novo = v + (v * 10 / 100)
else:
    novo = v + (v * 15 / 100)
print("Quem ganhavá R${:.2f} passa a ganhar R${:.2f} agora!".format(v, novo))










print('-='*16)
print("Analisador de triangulos!")
print("-="*16)
l1 = float(input("Primeiro segmento: "))
l2 = float(input("Segundo segmento: "))
l3 = float(input("Terceiro segmento: "))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print("Os segmentos PODEM FORMAR um triangulo!")
else:
    print("Os segmentos NÃO PODEM FORMAR um triangulo!")

    import time

    nome = str(input("Qual o seu nome? "))
    print("Processando....")
    time.sleep(2)
    if nome == "Andre":
        print("Que nome bonito  \033[1;36m{}\033[m seja bem vindo!".format(nome))
    elif nome == "Celia" or nome == "Allan" or nome == "Aline":
        print("Seu nome é muito bonito, seja bem vindo(a)!! \033[1;36m{}".format(nome))
    else:
        print("Tenha um bom dia \033[1;36m{}".format(nome))

