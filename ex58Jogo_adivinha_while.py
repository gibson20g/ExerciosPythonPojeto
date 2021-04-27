from random import randint
maquina = randint(0, 10)
print('Sou seu computador... Pensei em um numero entre 0 e 10')
print('Você consegue adivinhar ?')
acertou = False
palpite = 0
while not acertou:
	jogador = int(input('Qual seu palpite?: '))
	palpite += 1
	if jogador == maquina:
		acertou = True
	else:
		if jogador < maquina:
			print('Mais... continue tentando')
		elif jogador > maquina:
			print('Menos... vai lá tu consegue')
print(f'Acertou com {palpite} tentativas. Legal!')
