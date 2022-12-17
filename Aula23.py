# tratamentos de erros em python

#   serve para capturar o erro que esta ocorrendo e mostra - la na tela

try:  # para tentar fazer
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b

# Except:   # ira passar a mensagem abaixo caso aconteça erro
    #   print("Aconteceu um problema sentimos muito :(")

# OBS: em um mesmo programa pode se ter varios excepts!!
except (ValueError, TypeError):     # outro modo de se usar especificando o erro é dando o retorno a penas para
    # esse tipo de erro
    print("Tivemos um problema com o tipo de dado que vc inseriu ")

except ZeroDivisionError:   # pode se usar para colocar uma mensagem correspondente ao erro mostrado!!
    print("Não é possivel dividir um numero por zero")

except KeyboardInterrupt:
    print("O usuario preferiu nao inserir os dados. ")

except Exception as erro:  # se der problema ele fara o print abaixo, o Exception serve para mostrar qual foi o
    # erro importando o modulo erro

    print(f"O problema encontrado foi {erro.__class__} ")   # aqui vc chama pelo modulo e o class é para ver qual
    # o tipo do erro e a classe 

else:  # se nao der problema ele mostrara o resultado abaixo
    print(f"O resultado é {r}")

finally:    # O comando finally ira ser executado mesmo o programa dando certo ou errado ele ira mostrar o que vier
    # a seguir
    print("Volte sempre!")
