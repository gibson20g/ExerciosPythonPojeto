print('Bem Vindo (a) ao Menu')
num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))
print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos Números\n[5] Sair do Programa')
op = int(input('Qual sua opção?: '))

if op == 1:
	print(f'A soma dos números é: {num1 + num2} ')
elif op == 2:
	print(f'A multiplicação é: {num1 * num2}')
elif op == 3:
	if num1 > num2:
		print(f'O número {num1} é maior que o número {num2}')
	elif num2 > num1:
		print(f'O número {num2} é maior que o número {num1}')
	elif num1 == num2:
		print('Nuermos iguais/ de mesmo valor')
elif op == 4:
	num_1 = int(input('Digite o 1º número Novo: '))
	num_2 = int(input('Digite o 2º número Novo: '))
	print(f'Númmeros novos {num_1} e {num_2}')
elif op == 5:
	print('Saindo do Programa...Até logo')
