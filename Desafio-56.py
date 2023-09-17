somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totalmulher20 = 0
for c in range(1, 5):
    print('-' * 5, end= ' ')
    print('{}ª PESSOA'.format(c), end= ' ')
    print('-' * 5)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]: '))
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
#calcula a idade e o nome do homem mais velho da lista.
    if sexo in 'Ff' and idade < 20:
        totalmulher20 += 1
#calcula quantas mulheres com menos de 20 anos tem na lista.
mediaidade = somaidade / 4
#calcula a soma das idades de todos na lista.
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totalmulher20))