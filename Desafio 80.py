# Lista para armazenar os valores
valores = []

# Loop para ler os 5 valores
for i in range(5):
    valor = int(input(f"Digite o {i + 1}º valor: "))

    #posicionar o valor na lista na posição correta
    if i == 0:
        valores.append(valor)
    else:
        for j in range(len(valores)):
            if valor <= valores[j]:
                valores.insert(j, valor)
                break
        else:
            valores.append(valor)
            
# Mostra a lista ordenada na tela
print("Lista ordenada:", valores)