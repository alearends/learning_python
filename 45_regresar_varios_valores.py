# Cuando se regresan varios valores de una función, se regresan como una Tupla

print('*** regresar varios valores (tupla) de una función ***')

# Definimos una función
def persona_mayusculas(nombre, apellido, edad):
    print('esta función regresa varios valores en forma de tupla')
    return nombre.upper(), apellido.upper(), edad

# Desempaquetando la tupla: 
nombre, apellido, edad = persona_mayusculas('sandra', 'jimeMEz', 45)

# Comprobar
print(f'Resultado: nombre = {nombre}, apellido = {apellido}, edad = {edad}')