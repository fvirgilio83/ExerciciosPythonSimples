numerosegundos=int(input('Por favor, entre com o número de segundos que deseja converter: '))
numerodia=(numerosegundos//(24*3600))
segundosrestantes=(numerosegundos%(24*3600))
numerohora=segundosrestantes//3600
numerohorasrestante=segundosrestantes%3600
numerominutos=numerohorasrestante//60
numerosegundorestante=numerohorasrestante%60
print(numerodia,'dias',numerohora,'horas',numerominutos,'minutos','e',numerosegundorestante,'segundos.')
