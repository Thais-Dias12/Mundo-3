#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('\033[33mInforme seu sexo: [M/F] ')).strip().upper()[0]#.strip() remove os espaços
# .upper() deixa as letras em maiusculos. [0] vai utilizar a penas a primeira letra digitada.
while sexo not in 'MmFf':
    sexo = str(input('\033[31mDados  inválidos. por favor, informe seu sexo: ')).strip().upper()[0]
print('\033[32mSexo {} registrado com sucesso'.format(sexo))