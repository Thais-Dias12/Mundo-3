#Média do aluno. para saber se foi APROVADO, REPROVADO, ou RECUPERAÇÃO
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
nota = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, nota))
if nota < 5.0:
    print('Você foi reprovado!')
elif 7 > nota >= 5:
    print('Você esta de recuperação!')
else:
    print('Você foi APROVADO! Parabéns!')