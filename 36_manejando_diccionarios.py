# Gestionando diccionarios
# nombre_diccionario = {'a': 1, 'b': 2, 'c': 3}
# clave: valor
# las claves solo puede ser string

print('*** Diccionarios en Python ***')

persona = {
    'nombre': 'sergio', 
    'edad': 30, 
    'ciudad': 'Mexico'
    }

print(f'Diccionario de persona: {persona}')

print(f"Su nombre es {persona['nombre']}")
print(f"La edad es {persona['edad']}")
print(f"{persona['nombre']} tiene {persona['edad']} años y viven en {persona['ciudad']}")

# modificar el valor de un diccionario
persona['edad'] = 25

print(f"La edad es {persona['edad']}")

# agregar un nuevo elemento

persona['profesion'] = 'ingeniero'

print(f'Diccionario de persona: {persona}')

# Borrar elementos de un diccionario

del persona['ciudad']

print(f'Diccionario de persona: {persona}')

# iterar los elementos de un dict Solo las claves
for clave in persona:
    print(clave, end=' ')

for clave in persona.keys():
    print(clave, end=' ')

# iterar los elementos de un dict Solo los valores
for valor in persona.values():
    print(valor, end=' ')

# iterar los elementos de un dict Claves y valores
for clave, valor in persona.items():
    print(f'{clave}: {valor}')

