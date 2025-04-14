# Promedio de Calificaciones

# - Se debe solicitar el numero de calificaciones a ingresar
# - Se deben solicitar las calificaciones y calcular el promedio
# - imprimir el promedio

calificaciones = []
while True:
    try:
        n_calificaciones = int(input('Cuantas calificaciones deseas ingresar: '))
        if n_calificaciones > 0:
            break
        else:
            print('Por favor ingresa un numero mayor a cero')
    except ValueError:
        print('Por favor ingresa un numero entero mayor a cero')

for nota in range(n_calificaciones):
    while True:
        try:
            calificacion = float(input(f'Por favor ingresa la calificacion {nota + 1}: '))
            if calificacion >= 0 and calificacion <= 10:
                calificaciones.append(calificacion)
                break
            else:
                print('Por favor ingresa una calificacion entre 0 y 10')
        except ValueError:
            print('Por favor ingresa una calificacion entre 0 y 10')
        

n_promedio = sum(calificaciones) / len(calificaciones)
print('\n Las calificaciones son:', calificaciones)
print(f' El promedio de las calificaciones es: {n_promedio:.2f} \n')

