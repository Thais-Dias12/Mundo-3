#Crie um programa que leia números inteiros pelo teclado. 
#O programa só vai parar quando o usuário digitar o valor 999, 
#que é a condição de parada. No final, mostre quantos números foram 
#digitados e qual foi a soma entre elas (desconsiderando o flag).

núm = s = t = 0
while True:
    núm = int(input('Digite um valor [999 para parar]: '))
    if núm == 999:
        break
    s += núm
    t += 1
print(f'A soma dos {t} foi {s}')