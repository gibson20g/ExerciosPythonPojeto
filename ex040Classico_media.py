nota1 = float(input('Priemira Nota'))
nota2 = float(input('Segunda Nota'))
media = (nota1 + nota2) / 2
print('tirando {:.2f} e {:.2f}, a média do aluno é {:.2f}'.format(nota1, nota2, media))
if 7 > media >= 5:
	print('O aluno está em Recuperação')
elif media < 5:
	print('o aluno está REPROVADO')
elif media >= 7:
	print('Aprovado!!!!!!')
