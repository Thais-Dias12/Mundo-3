#Para saber sua massa corporal, e se você esta acima do peso ou não!
peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você esta ABAIXO do peso! CUIDADO!')
elif 18.5 <= imc < 25:
    print('PARABÉNS, Você está na faixa de PESO NORMAL!')
elif 25 <= imc < 30:
    print('Você esta com SOBREPESO!')
elif 30 <= imc < 40:
    print('Você esta com OBESIDADE!')
else:
    print('Você esta com OBESIDADE MÓRBIDA!, CUIDADO!')