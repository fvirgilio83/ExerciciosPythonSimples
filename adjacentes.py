n = int(input("Digite um número inteiro: "))

anterior=-1
adjacente = False
while (n > 0) and not adjacente:
    resto = n % 10
    n = (n - resto)/10
    if resto==anterior:
    	adjacente= True
    anterior=resto

if adjacente:
	print("sim")
else:
	print("não")
