#Tuplas são imutáveis 
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

#for comida in lanche:
#    print(f'Eu vou comer muito {comida}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer muito {lanche[cont]} na posição {cont}')

#for pos, comida in enumerate(lanche):
#    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi para caramba!')