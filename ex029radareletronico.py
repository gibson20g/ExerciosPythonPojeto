vel = int(input('Qual a velocidade do carro ?'))
if vel > 120:
    print('Multado! você exerceu o limite permitido na via que é de 120km/h')
    multa = (vel - 120) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
if vel < 45:
    print('Velocidade baixa, tenha cuidado')
print('Tenha um bom dia !')
