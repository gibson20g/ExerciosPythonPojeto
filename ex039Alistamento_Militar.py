from datetime import date
atual = date.today().year
ano_nascimento = int(input('Qual seu ano de Nascimento ?'))
idade = atual - ano_nascimento
print('Quem nasceu em {}  tem {} anos em {}'.format(ano_nascimento, idade, atual))
if idade == 18:
	print('Você Precisa se Alistar !!!!!!!')
elif idade < 18:
	salto = 18 - idade
	print('Ainda Não tem 18 anos, fique calmo ainda faltam {} anos!!!'.format(salto))
	ano = atual + salto
	print('Seu Alistamento será em {}'.format(ano))

elif idade > 18:
	salto = idade - 18
	print('Você Já derveria ter se alistados há {} anos atrás !!'.format(salto))
	ano = atual - salto
	print('Seu Alistamento foi em {}'.format(ano))

