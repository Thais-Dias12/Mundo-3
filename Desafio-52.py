#programa para saber se o número é primo, ou não!
num = int(input('\033[34mDigite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end= '')
        tot += 1
    else:
        print('\033[31m', end= '')
    print('{} '.format(c))
print('\033[34mO número {}, foi divisível {} vezes.'.format(num, tot))
if tot == 2:
    print('\033[32mÉ por isso que ele É PRIMO!')
else:
    print('\033[31mÉ por isso que ele NÃO É PRIMO!')