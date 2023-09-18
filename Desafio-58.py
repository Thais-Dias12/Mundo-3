#Jogo da Adivinhação v2.0
from random import randint
computador = randint(0, 10)
print('\033[34mSou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('\033[31mMais... Tente mais uma vez.')
        elif jogador > computador:
            print('\033[36mMenos... Tente mais uma vez.')
print('\033[32mAcertou com {} tentativas. Parabéns!'.format(palpites))