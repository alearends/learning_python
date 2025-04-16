# Combinando listas y diccionarios

print('*** Listas y Diccionarios ***')

personas = [
    {
        'nombre':'Regina',
        'apellido':'Flores',
        'edad': 21
    },
    {
        'nombre':'Alex',
        'apellido':'Rada',
        'edad': 25
    }
]

print(personas)

print(personas[0]['nombre'])

print(personas[0]['nombre'])  # Resultado: Regina

regina = personas[0]
print(f"{regina['nombre']} {regina['apellido']} tiene {regina['edad']} años")

# Recorrer los elementos de la lista
for contador, persona in enumerate(personas):
    print(f"persona: {contador + 1}: {persona.get('nombre')}, {persona.get('apellido')}, {persona.get('edad')}")