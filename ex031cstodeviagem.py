dis = float(input('Qual a distância da viagem ?'))
if dis <= 200:
    preco = dis * 0.50
else:
    preco = dis * 0.45
print('*=' * 25)
print('E o preço da sua viagem será R${:.2f}'.format(preco))
print('*=' * 25)
