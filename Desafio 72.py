# Crie uma lista com números de zero a vinte por extenso
#primeiro criei uma tupla com os números por extenso.

numero_por_extenso = ['Zero','Um','Dois','Três','Quatro','Cinco','Seis',
           'Sete', 'Oito', 'Nove','Dez','Onze', 'Doze', 'Treze','Quatorze', 
           'Quinze', 'Dezesseis','Dezesete','Dezoito','Dezenove','Vinte']

# Peça ao usuário para inserir um número entre 0 e 20
#Segundo criar um input para usuario escolher um número de 0 a 20.

numero = int(input('Digite um número entre 0 e 20: '))

#Criando uma condição para ver se o número digitado esta dentro das condições
# Verifique se o número está dentro do intervalo permitido.

if 0 <= numero <= 20:
    #Use o número como indice na lista para obter a representação por extenso
    extenso = numero_por_extenso[numero]
    print(f'O número {numero} por extenso é: {extenso}')
else:
    print('Número fora do intervalo permitido. tente novamente.')