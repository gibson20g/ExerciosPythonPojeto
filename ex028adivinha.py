from random import randint
from time import sleep
computador = randint(0, 5) #faz o computador pensar
print('^**' *30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('^**' *30)
jogador = int(input('\nEm que número eu pensei ?')) # jogador tentando adivinhar
print('será o mesmo número ou ganhei ?')
print('PEra que vou roubar')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador))
