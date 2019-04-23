#
lista1 = []

def functionlist(nombrelista):
	return len(nombrelista)


while True:
	elementos = input('ingrese elementos a la lista o "fin" para terminar: ')
	if elementos == 'fin':
		break
	else:
		lista1.append(elementos)



print('Lista completa: ')
n = 0
for x in lista1:
	print(x.center(10,'_') + 'orden : ' + str(n))
	n = n + 1
	print('='*20)

print('\nEl total de elementos es :' + str(functionlist(lista1)))

elige = input('Elija el orden: ')

print('El elemento elegido es: ' + lista1[int(elige)])

