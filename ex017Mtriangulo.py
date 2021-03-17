import math
#hi= (co ** 2 + ca ** 2) ** (1/2)
co = float(input('Digite o valor do catetto oposto'))
ca = float(input('Digite o valor do cateto adjecente'))
hi = math.hypot(co, ca)
print('A hhipotenusa vai medir {}'.format(hi))
