#Mostrando a tabuada de um número que o usuário escolher, só que agora utilizando a estrutura de repetição.
num = int(input('\033[32mDigite um número para ver sua tabuada: '))
print('-'*12)
for c in range(1, 11):
    print('\033[33m{} x {:2} = \033[31m{}'.format(num, c, num*c))
print('\033[32m-'*12)