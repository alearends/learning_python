# Ejercicio para crear una calculadora

print ('*** Calculadora ***')

is_salida = False

while not is_salida:
    print('''
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Salir
''')
    
    n_opcion = int(input('Por favor selecciona una opcion: '))

    if n_opcion == 1:
        print('Has seleccionado la suma, vamos a sumar dos numeros')
        n_numero1 = float(input('Por favor ingresa el primer numero: '))
        n_numero2 = float(input('Por favor ingresa el segundo numero: '))
        n_resultado = n_numero1 + n_numero2
        print(f'El resultado de la suma es {n_resultado} \n')
    elif n_opcion == 2:
        print('Has seleccionado la resta, vamos a restar dos numeros')
        n_numero1 = float(input('Por favor ingresa el primer numero: '))
        n_numero2 = float(input('Por favor ingresa el segundo numero: '))
        n_resultado = n_numero1 - n_numero2
        print(f'El resultado de la resta es {n_resultado} \n')
    elif n_opcion == 3:
        print('Has seleccionado la multiplicacion, vamos a multiplicar dos numeros')
        n_numero1 = float(input('Por favor ingresa el primer numero: '))
        n_numero2 = float(input('Por favor ingresa el segundo numero: '))
        n_resultado = n_numero1 * n_numero2
        print(f'El resultado de la multiplicacion es {n_resultado} \n')
    elif n_opcion == 4:
        print('Has seleccionado la division, vamos a dividir dos numeros')
        n_numero1 = float(input('Por favor ingresa el primer numero: '))
        n_numero2 = float(input('Por favor ingresa el segundo numero: '))
        if n_numero2 == 0:
            print('No se puede dividir entre cero')
        else:
            n_resultado = n_numero1 / n_numero2
            print(f'El resultado de la division es {n_resultado} \n')
    elif n_opcion == 5:
        print('Gracias por usar la calculadora \n')
        is_salida = True
    else:
        print('Por favor selecciona una opcion valida')      

