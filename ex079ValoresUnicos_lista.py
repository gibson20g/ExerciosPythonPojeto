numeros = list()
while True:
	num = int(input('Digite um Número: '))
	if num not in numeros:
		numeros.append(num)
		print('Valor Adicionado com Sucesso')
	else:
		print('Valor já na lista')
	res = str(input('Quer Continuar?[S/N]: ')).upper()
	if res in 'N':
		break
print('='*30)
numeros.sort()
print(f'Você Digitou os Números: {numeros}')
