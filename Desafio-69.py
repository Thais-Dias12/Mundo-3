#Crie um programa que leia a idade e o sexo de várias pessoas. 
#A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
#No final, mostre:
print('--'*20)
print('CADASTRE UMA PESSOA')
print('--'*20)
total = homem = pessoas = mulher = 0
resposta = 'S'
while True:
    print('-=-'*10)
    idade = int(input('Idade: '))
#Estrutura para quando: digitar uma letra errado. fazendo repetir a pergunta
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-=-'*10)
     #quantas pessoas maior de 18 anos
    total += 1
    if idade > 18:
        pessoas += 1
    #Quantos homens tem no cadastro!
    if sexo in 'Mm':
        homem += 1
    #Quantas mulheres menores de 20 anos cadastradas.
    if sexo in 'Ff' and idade < 20:
        mulher += 1 
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {pessoas}')
print(f'Ao todo temos {homem} homens cadatrados')
print(f'E temos {mulher} mulheres com menos de 20 anos')