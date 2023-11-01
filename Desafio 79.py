valores = [] # Lista para armazenar os valores digitados
valores_unicos = set() # Conjunto para armazenar os valores únicos

# Loop para ler os valores
while True:
    valor = input("Digite um valor numerico (ou 'sair' para encerrar): ")

    if valor.lower() == 'sair':
        break

    # Verifica se o valor é numérico
    if valor.isdigit():
        valor = int(valor)

        # Adiciona o valor ao conjunto de valores únicos se não estiver presente na lista de valores
        if valor not in valores:
            valores_unicos.add(valor)
            valores.append(valor)
        else:
            print("Valor já existe na lista. Não será adicionado.")

    else:
        print("Valor inválido. Digite um valor numérico.")

# Exibe os valores únicos em ordem crescente
valores_unicos_ordenados = sorted(valores_unicos)
print("Valores únicos digitados, em ordem crescente:")
print(valores_unicos_ordenados)