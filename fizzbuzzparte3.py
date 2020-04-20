n=input('Digite um numero:')
a=n[-1]
b=int(n)
if b%3==0 and (a=='0' or a=='5'):
		print('FizzBuzz')
else:
	print(n)
