#Calculando Fatorial dos Números!

#Solução simples.
#from math import factorial
#n = int(input('Digite um número para calcular seu fatorial: '))
#f = factorial(n)
#print('O fatorial de {} é {}.'.format(n, f))

#solução mais compleção
#n = int(input('Digite um número para calcular seu Fatorial: '))
#c = n
#f = 1
#print('calculando {}! = '.format(n), end='')
#while c > 0:
    #print('{}'.format(c), end='')
    #print(' x ' if c > 1 else ' = ', end='')
    #f *= c
    #c -= 1 
#print('{}'.format(f)) 

#Solução 3
n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print('Calcualando {}! = '.format(n), end='')
for m in range(5, 0, -1):
    print('{}'.format(m), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))