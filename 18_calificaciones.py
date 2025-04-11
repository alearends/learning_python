# Ejercicio para transformar calificaciones de numeros a letras
# A si es mayor o igual a 9
# B si es mayor o igual a 8
# C si es mayor o igual a 7
# D si es mayor o igual a 6
# F si es menor a 6
# en cualquier otro caso imprimir "valor desconocido"

while True:
    try:
        n_calificacion = float(input('Por favor dime tu calificación: '))
        if 0 <= n_calificacion <= 10:
            break
        else:
            print('Ingresa una calificación entre 0 y 10')
    except ValueError:
        print('Por favor ingresa una calificación valida entre 0 y 10: ')

if n_calificacion >= 9:
    print(f'Tu calificación es A\n')
elif n_calificacion >= 8:
    print(f'Tu calificación es B\n')
elif n_calificacion >= 7: 
    print(f'Tu calificación es C\n')
elif n_calificacion >= 6:
    print(f'Tu calificación es D\n')
elif n_calificacion < 6:
    print(f'Tu calificación es F\n')
else:
    print(f'Valor desconocido\n')

