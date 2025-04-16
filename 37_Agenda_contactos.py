# Ejercicio Crear una Agenda de Contactos
# - Utilizar Diccionarios de Python
# - Diccionario llamado Agenda
# - dentro de la Agenda, Nombre: telefono, email, dirección

print('*** Agenda de Contactos ***')

agenda = {
    "Carlos": {
        "telefono": "55566111",
        "email": "carlos@email.com",
        "direccion": "calle principal, 132"
    },
    "Maria":{
        "telefono": "98122345",
        "email": "marias@email.com",
        "direccion": "calle principal, 154"
    },
    "Pedro": {
        "telefono": "56566117",
        "email": "pedro@email.com",
        "direccion": "calle principal, 33"
    }
}

print(agenda)

# Acceder a los datos de de un contacto
print(f''' Informacion del contacto de Maria
    telefono: {agenda['Maria']['telefono']}
    ''')

# Agregar un nuevo contacto
agenda['Ana'] = {
        "telefono": "86566117",
        "email": "ana@email.com",
        "direccion": "calle secundaria, 33"
}

print(f''' Informacion del contacto de Ana
    telefono: {agenda['Ana']['telefono']}
    email: {agenda["Ana"]['email']}
    dirección: {agenda["Ana"]['direccion']}
    ''')

# Eliminar un contacto existente

del agenda["Pedro"]

print(agenda)

# Mostrar todos los detalles de la Agenda
print('\nLista de contactos de la Agenda: ')
for nombre, detalles in agenda.items():
    print(f''' Nombre: {nombre}
        telefono: {detalles['telefono']}
        email: {detalles['email']}
        direccion: {detalles['direccion']}
        ''')