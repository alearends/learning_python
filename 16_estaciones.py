# Identificar la estación del año en base a un numero

n_invierno = [1, 2, 12]
n_primavera = [3, 4, 5]
n_verano = [6, 7, 8]
n_otonio = [9, 10, 11]

n_estacion = 0
while True:
    try:
        n_estacion = int(input('Por favor indicar el numero del mes: '))
        if 1 <= n_estacion <= 12:  # si el numero es mayor o igual a 1 y menor o igual a 12
            break 
        else:
            print('por favor ingresa un numero entero entre 1 y 12: ')
    except ValueError:
        print('por favor ingresa un numero entero entre 1 y 12: ')

# comparo n_estacion con las estaciones
if n_estacion in n_invierno:
    print('Invierno')
elif n_estacion in n_primavera:
    print('Primavera')
elif n_estacion in n_verano:
    print('Verano')
else: 
    print('Otonio')


