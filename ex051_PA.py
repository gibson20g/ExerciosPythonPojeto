print('='*20)
print('10 Termos de Uma PA')
print('='*20)
termo = int(input('Primeira Termo: '))
razao = int(input('Razão: '))
decimo = termo + (10 - 1) * razao
for c in range(termo, decimo, razao):
	print('{}'.format(c), end='-')
print('ACABOU')
