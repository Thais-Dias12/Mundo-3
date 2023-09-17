# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for c in range (1, 6):
    peso = float(input('\033[37m Peso da {}ª pessoa:\033[32m '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
        #se for a primeira pessoa, ela é a maior e o menor peso.
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
        #agora se não for, ele vai verificar quem é o maior e quem é o menor.
print('\033[37mO maior peso lido foi de \033[32m{}Kg'.format(maior))
print('\033[37mO menor peso lido foi de \033[32m{}Kg'.format(menor))