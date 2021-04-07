cont = ('zero', 'Um', 'Dois', 'Três', 'Quatro',
        'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
        'Dez', 'Onze', 'Doze', 'Treze', 'Quartoze',
        'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
        'Dezenove', 'Vinte')
while True:
	num = int(input('Digite um numero entre 0 e 20: '))
	if 0 <= num <= 20:
		break
	print('Valor fora do Intervalo', end='')
print(f'Foi digitado o número {cont[num]}')
