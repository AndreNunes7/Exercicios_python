palavras = "Revisao", \
           "Chocolate", \
           "Peixe", \
           "Fazenda", \
           "Olimpiadas", \
           "Deus", \
           "pecado",
print("----- Leitor de vogais -----")
print("-="*20)
for p in palavras:
    print(f"\nNa palavra {p.upper()} as vogais são:", end=' ')
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end=' ')

