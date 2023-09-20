#Melhorando o DESAFIO 61
from time import sleep
print('Gerador de PA')
print('='* 10)
n1 = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = n1
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ⇾ '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
sleep(1)
print('Progressão finalizada com {} termos mostrados.'.format(total))