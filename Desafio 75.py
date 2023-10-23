# Ler quatro valores pelo teclado e armazená-los em uma tupla
valores = (int(input('Digite o Primeiro valor: ')), 
           int(input('Digite o Segundo valor: ')),
           int(input('Digite o Terceiro valor: ')),
           int(input('Digite o Quarto valor: ')))

print('Você digitou os valores', valores)
# Contar quantas vezes o valor 9 apareceu
quantidade_de_noves = valores.count(9)

# Encontrar a posição do primeiro valor 3 (se existir)
posicao_primeiro_tres = valores.index(3) if 3 in valores else None

# Encontrar os números pares na tupla
numeros_pares = [valor for valor in valores if valor % 2 == 0]

# Exibir os resultados
print(f"Quantidade de vezes que o valor 9 apareceu: {quantidade_de_noves}")
if posicao_primeiro_tres is not None:
    print(f"Posição do primeiro valor 3: {posicao_primeiro_tres + 1}ª") # Adicione 1 porque as posições começam em 1
else:
    print("O valor 3 não foi digitado.")

print(f"Número pares na tupla: {numeros_pares}")