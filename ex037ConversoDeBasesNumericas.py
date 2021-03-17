n1 = int(input("Digite um Número Inteiro"))
print('''Escolha uma das bases para conversão:
[1] Converte para BINÁRIO
[2] Converte para OCTAL
[3] Converte para HEXADECIAML''')
opcao = int(input("Sua Opção: "))
if opcao == 1:
	print("{} convertido para Binário é igual a {}".format(n1, bin(n1)))
elif opcao == 2:
	print("{} converttido para OCTAL é igual a {}".format(n1, oct(n1)))
elif opcao == 3:
	print("{} convertido para HEXADECIAML é igual a {}".format(n1, hex(n1)))
else:
	print("Você não digitou uma alternativa reconhecida, tente novamente!")
