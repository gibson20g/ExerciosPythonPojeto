valor1 = int(input("Primeiro valor:"))
valor2 = int(input("Segundo Valor:"))
valor3 = int(input("Terceiro Valor:"))
# testando para saber quem é o menor
menor = valor1
if valor2 < valor1 and valor3 < valor1:
    menor = valor2
if valor3 < valor1 and valor3 < valor2:
    menor = valor3
# testando para saber quem é o menor
maior = valor1
if valor2 > valor1 and valor2 > valor3:
    maior = valor2
if valor3 > valor1 and valor3 > valor2:
    maior = valor3
print("O menor valor digitado foi {}".format(menor))
print("O maior valor dentre os três é {}".format(maior))
