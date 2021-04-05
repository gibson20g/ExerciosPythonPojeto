nump = int(input('Digite um numero: '))
tot = 0
for c in range(1, nump + 1):
	if nump % c == 0:
		print('\033[34m', end='')
		tot += 1
	else:
		print('\33[m', end=',')
	print(f'{c}', end='')
print(f'\n\033[m0 Número {nump} foi divisivel {tot} vezes')
if tot == 2:
	print('É Primo')
else:
	print('Não Primo')
