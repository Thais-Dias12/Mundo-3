# Função para mostrar as estatísticas
def mostrar_estatisticas(lista):
    # A) Quantidade de números digitados
    print(f"Quantidade de números digitados: {len(lista)}")

    # B) Lista de valores em ordem decrescente
    lista_ordenada = sorted(lista, reverse=True)
    print(f"Valores em ordem decrescente: {lista_ordenada}")

     # C) Verificando se o valor 5 está na lista
    if 5 in lista:
       print("O valor 5 está na lista.")
    else:
        print("O valor 5 não está na lista.")

# Função principal
def main():
    numeros = [] # Lista para armazenar os números
    continuar = True

    # Laço para inserir os números na lista
    while continuar:
        try:
          numero = int(input("Digite um número (ou qualquer letra para parar): "))
          numeros.append(numero)
        except ValueError:
            continuar = False
    
    # Mostrar estatísticas
    mostrar_estatisticas(numeros)

if __name__ == "__main__":
    main()