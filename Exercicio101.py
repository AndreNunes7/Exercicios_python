def voto(ano):
    from datetime import datetime
    aniversario = datetime.now().year - ano

    if aniversario < 16:
        return f"Com a idade de {aniversario} anos  NAO VOTA"

    elif 16 <= aniversario < 18 or aniversario > 65:
        return f"Com a idade de {aniversario} anos o voto é OPCIONAL"

    else:
        return f"Com {aniversario} anos o voto é : OBRIGATORIO"


data = int(input("Digite sua data de aniversario: "))
print(voto(data))
