#comando (.strip) ele vai retirar os espaços da frase. enquanto o comando (.upper) vai deixar todas as letras em maiúsculas.
frase = str(input('Digite uma frase: ')).strip().upper()
#e os comandos a baixo, removeu os espaços internos.
palavras = frase.split() 
junto = ''.join(palavras)
inverso = ''
#Para diminuir seu codigo é ficaria (inverso == junto[::-1]) removendo assim as duas linhas abaixo!
#esse comando faz a frase ser lida de trás para frente.
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos uma palíndromo!')
else:
    print('A frase digitada NÃO é um PALÍNDROMO!')
