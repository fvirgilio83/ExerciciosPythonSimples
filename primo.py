n=int(input('Digite um numero inteiro: '))
tot=0
for c in range(1, n+1):
	if n%c==0:
		print('\033', end='')
		tot=tot+1
	else:
		print('\033', end='')
	print('{} ' .format(c), end='')
print('\n\033[o numero {} foi divisivel {} vezes' .format(n, tot))
if tot>2:
	print('não é primo')
else:
	print('é primo')