def éprimo(x):
	fator=1
	maiorprimo=1
	while x>fator:
		fator=fator+1
	if x%fator==0:
		maiorprimo=fator
		return maiorprimo
	