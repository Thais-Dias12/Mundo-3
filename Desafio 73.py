# Crie uma tupla com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
tabela_brasileirao = ('Botafogo','Bragantino','Flamengo','Athletico',
                      'Grêmio', 'Palmeiras','Atlético-MG','Fortaleza',
                      'Fluminense', 'São Paulo','Chapecoense','Bahia','Internacional',
                      'Corinthians','Cruzeiro','Goiás','Vasco da Gama','Santos','Coritiba','América-MG')

# a) Os 5 primeiros times
print("a) Os 5 primeiros times:")
for i in range(5):
    print(f"{i + 1}: {tabela_brasileirao[i]}")

# b) Os últimos 4 colocados
print("\nb) Os últimos 4 colocados:")
for i in range(16, 20):
    print(f"{i + 1}: {tabela_brasileirao[i]}")

#c) Times em ordem alfabética
print('\nc) Times em ordem alfabética:')
for time in sorted(tabela_brasileirao):
    print(time)

#d) Posição da chapecoense
chapecoense_index = tabela_brasileirao.index("Chapecoense") + 1
print(f"\nd) A chapecoense está na {chapecoense_index}ª posição.")