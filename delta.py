a=float(input('Digite o valor de a:'))
b=float(input('Digite o valor de b:'))
c=float(input('Digite o valor de c:'))
import math
delta=(b**2)-(4*a*c)
if delta < 0: 
	print('esta equação não possui raízes reais')
elif delta==0:
	x1=-b/(2*a)
	print('a raiz desta equação é', x1)
	
else:
	w= math.sqrt(delta)
	y1 =(-b+w)/(2*a)
	y2 =(-b-w)/(2*a)
	if y1>y2:	
		print('as raízes da equação são', y2, 'e',y1)
	else:
		print('as raízes da equação são',y1,'e',y2)


	


