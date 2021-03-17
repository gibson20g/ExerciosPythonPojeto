from time import sleep
print("="*25)
print("olá, Seja bem vindo(a) "),
print("="*25),
sleep(2),
valor_salario = float(input("Agora preciso que você informe o valor da casa: R$")),
casa = float(input("Infome também o seu salário: R$")),
anos = int(input("Agora, digite em quantos anos quer pagar")),

prestacao = casa / (anos * 12),

print("Para pagar uma casa de R${:.2f} em {} anos" .format(casa, anos)),
print("Calculando o Valor da Prestação, aguarde."),
print("A prestação será de R${:.2f}".format(prestacao)),
