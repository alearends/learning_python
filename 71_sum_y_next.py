print('*** Función sum y next ***')

lista = [1, 2, 3, 4, 5]

# Suma de todos los elementos
resultado = sum(lista) # 1+2+3+4+5 = 15
print(f'Resultado de la suma: {resultado}') # 15


# Podemos proporcionar un valor inicial
resultado = sum(lista, 20) # 15 + 20 = 35
print(f'Resultado de la suma con valor inicial de 20: {resultado}') # 35

# La funcion next
iterador = iter(lista)

# Obtenemos el proximo elemento del iterador usando la funcion next
print(f'Siguiente elemento del iterable: {next(iterador)}') # 1
print(f'Siguiente elemento del iterable: {next(iterador)}') # 2
print(f'Siguiente elemento del iterable: {next(iterador)}') # 3
print(f'Siguiente elemento del iterable: {next(iterador)}') # 4
print(f'Siguiente elemento del iterable: {next(iterador)}') # 5
 