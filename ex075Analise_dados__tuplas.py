num = (int(input('Digite um Número: ')),
       int(input('Digite um Número: ')),
       int(input('Digite um Número: ')),
       int(input('Digite um Número: ')))
print(f'Valores digitados: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
	print(f'O valor 3 apareceu {num.index(3)+1}ª posição')
else:
	print('O valor 3 não foi digitado')
print(f'Os valores PARES Digitados foram')
for n in num:
	if n % 2 == 0:
		print(n, end=' ')
