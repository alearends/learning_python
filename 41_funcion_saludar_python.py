# Funcion Saludar en Python

# Opción A - sin argumento, sin return, usando input y print
# 1. Crea la función
def saludar():
    nombre = input('Dime tu nombre para la funcion A: ')
    print(f'Hola {nombre} desde mi función A')

# 2. invoca la función
saludar()


# Opcion B - pasando un argumento, sin input del usuario
# 1. Crea la función
def saludar2(mensaje):
    print(f'{mensaje}')

# 2. invoca la función
saludar2('Hola desde la función B')

# Opcion C - retornando un valor de una función
# 1. Crea la función
def saludar2():
    # vamos a colocar un return y un mensaje que se retornara
    return 'Hola desde la función C'

# 2. invoca la función y guarda la función en una variable
valor_devuelto = saludar2()

# 3. usa la variable donde guardaste el valor retornado de la funcion
print(f'Valor devuelto de la funcion C: {valor_devuelto}')