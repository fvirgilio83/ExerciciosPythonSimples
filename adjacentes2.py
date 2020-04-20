n = int(input("Digite um número inteiro: "))

anterior=1
while (n > 0):
	resto = n % 10
	n = (n - resto)/10
	if resto==anterior:
		anterior=resto
		print("existe dois numeros iguais adjacentes neste numero")
	else:
		print("não existe dois numeros iguais adjacentes neste numero")
