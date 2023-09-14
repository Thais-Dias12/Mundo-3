# Calculo para saber o valor de sua compra, e para saber qual o modo de pagamento!
print('{:=^40}'.format(' MERCADINHO '))
preço = float(input('Preço das compras? R$'))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.0f} SEM JUROS'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.0f} COM JUROS'.format(totparc, parcela))
else:
    total = 0
    print('Opção de pagamento INVÁLIDA. Tente novamente!')
print('Sua compra de R${:.0f} vai custar R${:.0f} no final.'.format(preço, total))

