# falta corrigir erro
print(f"{'Guarána de Sabores':=^40}")
preco = float(input('Preço das Compras: R$ '))
print(''''Formas de Pagamento
[1] À vista Dinnehiro/Cheque
[2] À vista CARTÃO
[3] 2x no CARTÃO
[4] 3x ou mais no CARTÃO''')
alternativa = int(input('Qual Sua Opção ?: '))
if alternativa == 1:
	final = preco - (preco * 10 / 100)
elif alternativa == 2:
	final = preco - (preco * 5 / 100)
elif alternativa == 3:
	final = preco
	parcelas = final / 2
	print('Sua compra Parcelada de 2 Vezes é R$:{:.2f} SEM JUROS '.format(parcelas))
elif alternativa == 4:
	final = preco + (preco * 20 / 100)
	tot_parcelas = int(input('Quantas Parcelas ?: '))
	parcela = final / tot_parcelas
	print(f'Sua Compra será parcelada em {tot_parcelas:.2f}x vezes de R${parcela:,2f} COM JUROS')
print('Sua compra de {:.2f} vai custar R${:.2f}'.format(preco, final))


