print("-="*15)
print("Analisador de triangulos")
print("-="*15)
r1 = float(input("Primeiro segmento"))
r2 = float(input("segundo segmento"))
r3 = float(input("Terceiro segmento"))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
	print("Os segmentos acima podem formar triângulos!")
else:
	print("Os segmentos acima NÂO pode formar triangulo")
