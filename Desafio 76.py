# Defina a tupla com os produtos e preços
produtos_precos = (
    "Macarrão", 10.99,
    "Arroz",    24.95,
    "Presunto", 7.50,
    "Fejão",    15.75,
    "Mussarela", 9.99
  )

# Imprima a listagem de preços em forma tabular
print("-" * 37)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print("-" * 37) # Linha de separação

# Itere sobre os elementos da tupla e imprima os produtos e preços formatados
for produto in range(0, len(produtos_precos)):
    if produto % 2 == 0:
        print(f'{produtos_precos[produto]:.<30}', end='')
    else:
        print(f"R${produtos_precos[produto]:>2.2f}")
print("-" * 37)