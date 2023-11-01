# Este programa solicita ao usuário a inserção de 5 valores inteiros, armazena-os em uma lista,
# e em seguida, identifica e exibe o maior e o menor valor digitado, juntamente com suas respectivas posições na lista.
#----------------------------------------------------

# Lista para armazenar os valores
valores = []

# Loop para ler os 5 valores
for i in range(5):
    valor = int(input(f'Digite o {i+1}º valor: '))
    valores.append(valor)

# Encontrar o maior e o menor valor na lista
maior_valor = max(valores)
menor_valor = min(valores)

# Encontrar as posições do maior e menor valor na lista
posicao_maior = (i + 1 for i, v in enumerate(valores) if v == maior_valor)
posicao_menor = (i + 1 for i, v in enumerate(valores) if v == menor_valor)

# Mostrar os resultados
print(f"Valores digitados: {valores}")
print(f"O maior valor digitado foi {maior_valor} na posição {', '.join(map(str, posicao_maior))}")
print(f"O menor valor digitado foi {menor_valor} na posição {', '.join(map(str, posicao_menor))}")