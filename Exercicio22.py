nome = str(input("Digite seu nome completo: ")).strip()
q = len(nome) - nome.count(' ')
u = nome.upper()
l = nome.lower()
p = len(nome.split()[0])
print("Seu nome é: {:^} \ncom letra maiusculas fica: {:^} \ne com minusculas fica: {:^}".format(nome, u, l))
print("Seu nome completo tem {} letras ".format(q))
print("Seu primeiro nome tem: {}".format(p))

