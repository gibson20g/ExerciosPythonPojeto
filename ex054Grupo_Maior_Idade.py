from datetime import date
atual = date.today().year
total_maior = 0
total_menor = 0
for pessoa in range(1, 8):
	nascimento = int(input('Em que ano a Pessoa Nasceu ? '))
	idade = atual - nascimento
	if idade >= 21:
		total_maior += 1
	else:
		total_menor += 1
print(f'tivemos o total de {total_maior} pessoas Maiores de Idade')
print(f'tivemos o total de {total_menor} pessoas Menores de Idaade')
