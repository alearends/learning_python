# Herramienta para determinar si un numero es positivo o negativo

while True:
    try:
        n_numero = float(input('Indica un numero: '))
        if n_numero <= 0:
            print(f'El numero {n_numero} no es positivo')
        else:
            print(f'El numero {n_numero} es positivo')
        break # Se sale del bucle porque es una opción valida
    except ValueError: 
        print('Por favor ingresa un numero:')




