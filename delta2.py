a=int(input('Digite o valor de a:'))
b=int(input('Digite o valor de b:'))
c=int(input('Digite o valor de c:'))
import math
delta=(b**2)-(4*a*c)
print(delta)
if delta > 0:
	w= math.sqrt(delta)
	x1 =(-b+w)/(2*a)
	x2 =(-b-w)/(2*a)
	print('as raizes da equação são', x1, 'e',x2)	
elif  delta==0:
	x1=-b/(2*a)
	print('a raiz desta equação é', x1)
else:
	print('esta equação não possui raízes reais')
