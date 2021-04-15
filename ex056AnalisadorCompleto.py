soma_idade = 0
media_idade = 0
maior_ida_h = 0
nome_velho = ''
total_mulher_20 = 0
for p in range(1, 11):
	print(f'======= {p}ª Pessoa ========')
	nome = str(input('Nome: ')).strip()
	idade = int(input('Idade: '))
	genero = str(input('Seu Genero [M/F]: ')).strip().upper()
	soma_idade += idade
	if p == 1 and genero in 'Mm':
		maior_ida_h = idade
		nome_velho = nome
	if genero in 'Mm' and idade > maior_ida_h:
		maior_ida_h = idade
		nome_velho = nome
	if genero in 'Ff' and idade < 20:
		total_mulher_20 += 1
media_idade = soma_idade / 10
print(f'A média das idades é {media_idade}')
print(f'O Homem mais velho tem {maior_ida_h} e se chama {nome_velho}')
print(f'Total de mullheres menores que 20 anos é {total_mulher_20}')
