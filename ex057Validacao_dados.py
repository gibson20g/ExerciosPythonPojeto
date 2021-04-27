genero = str(input('Informe seu Gênero,[M/F]: ')).strip().upper()[0]
# idade = int(input('Informe Sua Idade: '))
while genero not in 'MF':
	genero = str(input('Dados Invalidos.Informe seu Gênero,[M/F]: ')).strip().upper()[0]
print(f'Genero {genero} cadastrado com sucesso')
