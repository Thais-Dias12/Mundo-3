#Os termos da PA são identificados pela posição que ocupam na sequência, númerica. 
#Exemplo: 1, 2, 3, 4, etc
print('='*21)
print('10 TERMOS DE UMA PA')
print('='*21)
n1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = n1 + (10 - 1) * razao
for c in range(n1, decimo + razao, razao):
    print('{}'.format(c), end= ' ⇾  ')
print('ACABOU')