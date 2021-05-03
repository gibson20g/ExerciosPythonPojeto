largura = float(input('Informe a largura da parede em Metros: '))
altura = float(input('Informe a altura da parede em Metros: '))
tamanho = (largura * altura) / 2
tinta = tamanho / 2
print('A parede tem {}m² e Precisa de {} litros de tinta'.format(tamanho, tinta))
