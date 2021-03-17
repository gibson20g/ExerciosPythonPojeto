import math
angulo = float(input('Digite o ângulo que você deseja'))
seno = math.sin(math.radians(angulo))
print('o angulo de {} tem o seno d {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O cosseno do ângulo de {} mede {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('A tangente do angulo {} mede {:.2f}'.format(angulo, tangente))
