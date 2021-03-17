from random import randint
from time import sleep
itens = ('[Pedra]', '[Papel]', '[Tesoura]')
maquina = randint(0, 2)
print('''Suas Opções
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual sua ESCOLHA ????'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO !!!')
sleep(1)
print('-='*20)
print('Seu adversario escolheu {}'.format(itens[maquina]))
print('Jogador Escolheu {}'.format(itens[jogador]))
print('-='*20)
if maquina == 0: # pedra
	if jogador == 0:
		print('EMPATE1')
	elif jogador == 1:
		print('Jogador Vence1')
	elif jogador == 2:
		print('Maquina Venceu1')
	else:
		print('invalido1')
if maquina == 1:  # papel
	if jogador == 0:
		print('Maquina Vence2')
	elif jogador == 1:
		print('Empate 2')
	elif jogador == 2:
		print('jogador Vence2')
	else:
		print('invalido2')
if maquina == 2:  # tesoura
	if jogador == 0:
		print('jogador vence 3')
	elif jogador == 1:
		print('Maquina Vence3')
	elif jogador == 2:
		print('Emapate 2')
	else:
		print('invalido3')
