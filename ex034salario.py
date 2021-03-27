nome = str(input("Digite o Nome do Funcionario: "))
salario = float(input("Qual é o salário do funcionario?R$: "))

if salario <= 1045:
	novo = salario + (salario * 5.26 / 100)
	porcent = 5.26
	aumento = novo - salario
	print("O salario antigo é R${:.2f}, Porcentagem de aumento {}% ".format(salario, porcent))
	print("aumento de R${:.2f}, E o novo salário será {:.2f}".format(aumento, novo))
elif 2195 >= salario > 1045:
	novo = salario + (salario * 4.32 / 100)
	porcent = 4.32
	aumento = novo - salario
	print("O salario antigo é R${:.2f}, Porcentagem de aumento {}% ".format(salario, porcent))
	print("aumento de R${:.2f}, E o novo salário será {:.2f}".format(aumento, novo))
elif 3500 > salario > 2195:
	novo = salario + (salario * 2.75 / 100)
	porcent = 2.75
	aumento = novo - salario
	print("O salario antigo é R${:.2f}, Porcentagem de aumento {}% ".format(salario, porcent))
	print("aumento de R${:.2f}, E o novo salário será {:.2f}".format(aumento, novo))
elif salario >= 3500:
	novo = salario + (salario * 1.79 / 100)
	porcent = 1.79
	aumento = novo - salario
	print("O salario antigo é R${:.2f}, Porcentagem de aumento {}% ".format(salario, porcent))
	print("aumento de R${:.2f}, E o novo salário será {:.2f}".format(aumento, novo))
