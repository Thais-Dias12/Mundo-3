r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2: 
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 == r2 > r3:
        print('ISÓSCELES!')
    else:
        print('ESCALENO!')
else:
    print('Os segmentos acima NÃO podem FORMAR um triângulo ')
#Diferente (!=) 
#Igual (==)
#r1 != r2 != r3 != r1:
#r1 é diferente de r2:
#r2 é diferente de r3:
#r3 é diferente de r1: