from time import sleep
n1 = int(input('\033[34mDigite primeiro valor: '))
n2 = int(input('Digite segundo valor: '))
opção = 0
while opção != 5:
    print('''\033[37m    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opção = int(input('\033[33m>>>>>> Qual é a sua opção? ')) 
    sleep(1)
    print('\033[34m=-=' * 10)
    if opção == 1:
        soma = n1 + n2
        print('\033[34mA soma entre {} + {} é {}'.format(n1, n2, soma))
        sleep(1)
    elif opção == 2:
        mul = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, mul))
        sleep(1)
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
        sleep(1)
    elif opção == 4:
        print('\033[33mInforme os número novamente: ')
        n1 = int(input('\033[34mDigite primeiro valor: '))
        n2 = int(input('Digite segundo valor: '))
        sleep(1)
    elif opção == 5:    
        print('\033[31mFinalizando...')
        sleep(1)
    else:
       print('\033[31mOpção invalida. Tente novamente')
    print('\033[34m=-=' * 10)
    sleep(1)            
print('\033[31mFim do programa!')