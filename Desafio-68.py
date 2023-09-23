#Faça um programa que jogue par ou ímpar com o computador. 
#O jogo só será interrompido quando o jogador perder, 
#mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
print('\033[37m=-=' * 20)
print('\033[33mVAMOS JOGAR PAR OU ÍMPAR')
print('\033[37m=-=' * 20)
v = 0
while True:
    jogador = int(input('\033[34mDiga um valor: '))
    computador = randint(1, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('\033[33mPar ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou: {jogador} e o computador {computador}. total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')  
    if tipo == 'P':
        if total % 2 == 0:
            print('\033[32mVocê VENCEU!')
            v += 1
        else:
            print('\033[31mVocê PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 ==  1:
            print('\033[32mVocê VENCEU!')
            v += 1
        else:
            print('\033[31mVocê PERDEU!')
            break
        print('-' * 40)
    print('\033[32mVamos jogar novamente...')
print(f'\033[31mGAME OVER! \033[32mVocê venceu {v} vezes.')