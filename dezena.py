number=(input('Digite um numero inteiro:'))
valor=int(number)
if valor>=10:
	print('O dígito das dezenas é',number[-2])
else:
	print('O dígito das dezenas é 0')