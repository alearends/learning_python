# Función con argumentos por nombre

print('*** función con argumentos por nombre ***')

def crear_persona(nombre, apellido='', edad=0):
    print(f'Persona: nombre = {nombre}, apellido = {apellido}, edad = {edad}')

# crear_persona('Ricardo')

crear_persona(nombre='Ricardo') # asi es mejor

crear_persona(edad=28, nombre='Ricardo', apellido='Quintana' ) # Si se pasan los argumentos asi, no importa el orden

