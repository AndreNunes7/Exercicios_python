tabela = ("Corinthians", "Bragantino", "Atletico-MG", "Coritiba", "Sao Paulo", "Santos", "Cuiaba", "Internacional",
          "Avai", "America-MG", "Palmeiras", "Flamengo", "Botafogo", "Fluminense", "Ceara", "Athletico-PR",
          "Atletico-GO", "Goias ", "Juventude", "Chapecoense")
print("-="*15)
print("---- TABELA DO BRASILEIRAO ----")
print("-="*15)
print(f"Lista dos times do BRASILEIRÃO:\n{tabela}")
print("-="*15)
print("TOP 5 TIMES:")
for c in range(0, 5):
    print(tabela[c])
print("-="*15)
print("ULTIMOS 4 COLOCADOS DA TABELA: ")
print(tabela[-4:])
print("-="*15)
print("TIMES EM ORDEM ALFABETICA:")
print(sorted(tabela))
print("-="*15)
print(f"A CHAPECOENSE está na POSIÇÃO {tabela.index('Chapecoense')+1}°")
