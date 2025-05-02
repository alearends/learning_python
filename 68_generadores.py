'''
def funcion_normal():
    return [1, 2, 3]  # Devuelve toda la lista de una vez

def generador():
    yield 1  # Pausa aquí
    yield 2  # Luego aquí
    yield 3  # Finalmente aquí

# Uso:
print(funcion_normal())  # Output: [1, 2, 3] (toda la lista en memoria)

gen = generador()
print(next(gen))  # Output: 1 (solo genera el primero)
print(next(gen))  # Output: 2 (luego el segundo, manteniendo el estado)
'''

print('*** Generadores en Python ***')

def generador(maximo):
    contador = 0
    while contador < maximo:
        yield contador
        contador += 1

# Creamos un generador
var_generador = generador(5)

# iteramos sobre el generador
for valor in var_generador:
    print(valor)

print('*** Expresiones Generadoras en Python ***')

generador = (x**2 for x in range(10) if x % 2 == 0)

for cuadrados_pares in generador:
    print(cuadrados_pares)