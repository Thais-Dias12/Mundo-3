#Conta de 1 até 6, porem o ultimo número ele não considera. ficando então de 1 a 5.
#Se for colocado de 0 a 6, ai sim. ele vai fazer 6 (Oi).
for c in range(0, 7, 2):
     print(c) #Se tiver dentro desta estrutura também será repetido, porem se colocar (C) ao inves de letras será números.
print('FIM')  
#Se for colocado mais um número, dentro do range. o que você coloque será o final da interação. então se colocar -1. no fim, ele vai contar de trás para frente.   
#Se for colocado (0, 7, 2) será contado. De zero a seis, pulando duas casas.
n = int(input('Digite um número: '))
for c in range(0, n+1, 2):
    print(c)
print('FIM')
#se você por print dentro da estrutura de repetição, sera repetida o tento de vezes que foi determinado.
s = 0
for c in range(0, 3):
    n = int(input('Digite um número: '))
    s += n
print('A somatoria destes números são: {}'.format(s))