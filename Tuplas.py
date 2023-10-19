#Tuplas são imutáveis 
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

#for comida in lanche:
#    print(f'Eu vou comer muito {comida}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer muito {lanche[cont]} na posição {cont}')

#for pos, comida in enumerate(lanche):
#    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi para caramba!')

#.index ele mostra a possição da alguma variavel, mostrando em qual possição ela oculpa
#.conut conta quantos elementos tem dentro de uma variavel, exemplo lanche. mostrando seu total. exemplo, pudim. ele aparece uma vez. e é assim que o conut vai mostrar.
#sorted ele coloca em ordem uma lista, ou tuplas.
#del explui uma variavel.