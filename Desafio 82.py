# Função para separar pares e ímpares
def separar_pares_impares(numeros):
    pares = [num for num in numeros if num % 2 == 0]
    impares = [num for num in numeros if num % 2 != 0]
    return pares, impares

# Função principal
def main():
    numeros = [] # Lista para armazenar os números

    # Laço para inserir os números na lista
    while True:
        try:
            numero = int(input("Digite um número (ou qualquer letra para parar): "))
            numeros.append(numero)
        except ValueError:
            break
    
    # Separar os valores pares e ímpares
    pares, impares = separar_pares_impares(numeros)

    # Mostrar o conteúdo das três listas
    print(f"Todos os números digitados: {numeros}")
    print(f"Números pares: {pares}")
    print(f"Números ímapares: {impares}")

if __name__ == "__main__":
    main()