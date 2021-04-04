soma = 0
cont = 0
for c in range(1, 11):
	num = int(input('Digite 10 numeros inteiros: '))
	if num % 2 == 0:
		soma += num
		cont += 1

print(f'numeros PARES informados {cont} e a soma foi = {soma}')
