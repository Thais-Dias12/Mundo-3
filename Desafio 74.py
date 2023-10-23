import random

# Gerar cinco números aleatórios e colocá-los em uma tupla
numero_aleatorios = tuple(random.randint(1, 10) for _ in range(5))

# Mostrar a listagem dos números gerados
print(f"Número gerados: {numero_aleatorios}")

# Encontrar o menor e o maior valor na tupla
menor_valor = min(numero_aleatorios)
maior_valor = max(numero_aleatorios)

#Mostrar o menor e o maior valor
print("Menor valor:", menor_valor)
print("Maior valor:", maior_valor)