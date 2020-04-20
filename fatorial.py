n=int(input('Digite um número inteiro: '))
fat=1
count=1
while count<=n:
	fat*=count
	count+=1

print(fat)
