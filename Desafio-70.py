print('-'*20)
print('{:-^5}'.format(' LOJA SUPER BARATÃO '))
print('-'*20)
rest = 'S'
soma = mais = cont = menor = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$ '))
    #soma das compras
    cont += 1
    soma += preço
    #Produto custando mais de 1.000
    if preço >= 1000:
        mais += 1
    #Produto mais barato da lista.
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    rest = ' '
    while rest not in 'SN':
        rest = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if rest == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total gasto na compra foi R${soma:.2f}')
print(f'Temos {mais} produtos custando mais de R$1.000')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')