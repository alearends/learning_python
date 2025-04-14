# validacion de un campo de un formulario

nombre_usuario = None

while not nombre_usuario:
    nombre_usuario = input('Por favor indica tu nombre de usuario: ')
    
mensaje = f'El nombre de usuario es {nombre_usuario}'

# Repeticion de un mensaje
numero_de_repeticiones = None
while not numero_de_repeticiones:
    try:
        numero_de_repeticiones = int(input('Cuantas veces quieres repetir el mensaje: '))
        if numero_de_repeticiones <= 0:
            print('Por favor ingresa un numero mayor a cero')
    except ValueError:
        print('Por favor ingresa un numero:') 

for _ in range(numero_de_repeticiones):
    print(mensaje)
