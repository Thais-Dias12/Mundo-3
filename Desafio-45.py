#Programa para jogar Pedra, papel e tesoura. Com o computador!
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''\033[37mSua opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('\033[34mQual é a sua jogada? '))
print('\033[35mJO')
sleep(1)
print('\033[35mKEN')
sleep(1)
print('\033[35mPÔ!!!')
print('\033[34m-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: #Computador jogou PEDRA
    if jogador == 0: #PEDRA
        print('\033[33mEMPATE!')
    elif jogador == 1: #PAPEL
        print('\033[32mJOGADOR VENCEU!')
    elif jogador == 2: #TESOURA
        print('\033[31mJOGADOR PERDEU!')
    else:
        print('\033[31mJOGADA INVÁLIDA!')            
elif computador == 1: #Computador jogou PAPEL
    if jogador == 0: #PEDRA
        print('\033[31mJOGADOR PERDEU!')
    elif jogador == 1: #PAPEL
        print('\033[33mEMPATE!')
    elif jogador == 2: #TESOURA
        print('\033[32mJOGADOR VENCEU!')
    else:
        print('\033[31mJOGADA INVÁLIDA!')
elif computador == 2: #Computador jogou TESOURA
    if jogador == 0: #PEDRA
        print('\033[32mJOGADOR VENCEU!')
    elif jogador == 1: #PAPEL
        print('\033[31mjOGADOR PERDEU!')
    elif jogador == 2: #TESOURA
        print('\033[33mEMPATE!')
    else:
        print('\033[31mJOGADA INVÁLIDA!')
