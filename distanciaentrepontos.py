x1=float(input('digite o numero da coordenada x1:'))
y1=float(input('digite o numero da coordenada y1:'))
x2=float(input('digite o numero da coordenada x2:'))
y2=float(input('difite o numero da coordenada y2:'))
import math
dist=math.sqrt((x1-x2)**2+(y1-y2)**2)
if dist >=10:
	print('longe')
else:
	print('perto')