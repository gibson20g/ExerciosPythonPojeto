print('*'*15)
print('Cálculadora')
print('*'*15)
print('='*20)
print('''Escolha Uma opção\n1 - Soma\n2 - Multiplicação\n3 - Divisão\n4 - Subtração''')
print('='*20)
op = float(input('Digite Sua Opção: '))

if op == 1:
	num = int(input('Digite o numero para ver a tabuada: '))
	for c in range(1, 11):
		print('{} + {:2} = {} '.format(num, c, num + c))
elif op == 2:
	num = int(input('Digite um numero para ver a tabuada: '))
	for c in range(1, 11):
		print('{} x {:2} = {}'.format(num, c, num * c))
elif op == 3:
	num = int(input('Digite um numero para ver a tabuada: '))
	for c in range(1, 11):
		print(f'{num} / {c} = {num / c :.2f}')
elif op == 4:
	num = int(input('Digite um numero para ver a tabuada: '))
	for c in range(1, 11):
		print(f'{num} - {c} = {num - c :.2f}')
else:
	print('Opção Inválida!!!!Tente Novamente')
	print('Programa Encerrado ')
