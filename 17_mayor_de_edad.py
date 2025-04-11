# programa para saber si esmayor de edad

while True:
    try:
        n_edad = int(input('¿Cuántos años tienes? '))
        if n_edad >= 0:
            break
        else:
            print('Por favor ingresa una edad valida')
    except ValueError:
        print('Por favor ingresa una edad valida')


n_mayor_edad = 18

print(f'Tu eres mayor de edad') if n_edad >= n_mayor_edad else print(f'Tu eres menor de edad')

