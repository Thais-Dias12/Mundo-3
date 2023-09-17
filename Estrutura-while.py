'''for c in range(1, 10):
    print(c)
print('Fim')'''
#quando a estrutura tem um limite, pré determinado.

'''c = 1
while c < 10:
    print(c)
#é necessario fazer a estrutura a baixo, pós o programa vai se repetir. e para evitar que fique repetindo (1)
#é necessario adicionar (c = c + 1) ou (c += 1) para continuar a contagem, pos o programa vai entender (1 + 1 = 2) e assim, por diante.
    c += 1
print('Acabou!')
#Estrutura quando não tem limite, mas também funciona para limite pré determinado.'''

'''n = 1 
while n != 0: #Quando o zero for digitado, o programa ira para.
    n int(input('Digite um valor: '))
print('Fim')'''

'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:    
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} número pares e {} números ímpares!'.format(par, impar))

