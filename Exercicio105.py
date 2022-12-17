def notas(*n, sit=False):
    """

    -> Função para analisar notas e situaçoes de varios alunos.
    :param n: uma ou mais notas dos alunos (aceita varias)
    :param sit: valor opcional, indicando se deve ou nao adicionar a situação
    :return: dicionario com varias informaçoes sobre a situação da turma.

    """

    dic = {}
    dic['Total:'] = len(n)
    dic['Maior:'] = max(n)
    dic['Menor:'] = min(n)
    dic['Media:'] = sum(n) / len(n)

    if sit:
        if dic['Media:'] >= 7:
            dic['Situação'] = "BOA"
        elif dic['Media:'] >= 5:
            dic['Situação'] = "RAZOAVEL"
        else:
            dic['Situação'] = "RUIM"
    return dic


rsp = notas(5.7, 4.7, 8, 6, 7, 10, sit=True)
print(rsp)
help(notas)
