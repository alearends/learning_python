# Juego de adivinar numero secreto
# Se usara while siepre que se pueda
# Se usara la funcion rand int de la libreria random para generar un valor aleatorio entre 1 y 50
# Se le pedira al usuario que adivine el numero secreto
# Se le indicara si el numero es mayor o menor al numero secreto
# Se llevara un contador de los intentos
# Cuando el usuario adivine el numero secreto se felicitara y se le indicara el numero de intentos
# Se le preguntara si desea jugar nuevamente
# Existira una opcion avanzada limitando el numero de intentos maximos

import random

def introduce_numero():
    while True:
        try:
            n_numero = int(input('Dame un numero entre 1 y 50: '))
            if 1 <= n_numero <= 50:
                return n_numero
            else:
                print('Por favor ingresa un numero entre 1 y 50')
        except ValueError:
            print('Por favor ingresa un numero entre 1 y 50')

def indica_limite():
    while True:
        try:
            n_limite = int(input('Por favor indica el limite de intentos: '))
            if n_limite > 0:
                return n_limite
            else:
                print('Por favor ingresa un numero mayor a cero')
        except ValueError:
            print('Por favor ingresa un numero mayor a cero')

print('**** Bienvenido al juego de adivinar el número secreto ***')

is_salida = False

while not is_salida:
    print('''
    1. Nivel Basico
    2. Nivel Avanzado
    3. Salir
''')

    n_opcion = int(input('Por favor selecciona una opcion: '))
    
    if n_opcion == 1:
        n_intentos = 0
        print('++ Nivel Básico ++ \n')
        n_numero_secreto = random.randint(1, 50)
        n_numero = introduce_numero()
        while n_numero != n_numero_secreto:
            if n_numero < n_numero_secreto:
                print('El numero secreto es mayor')
                n_intentos += 1
                n_numero = introduce_numero()
            elif n_numero > n_numero_secreto:
                print('El numero secreto es menor')
                n_intentos += 1
                n_numero = introduce_numero()
            
        print('Felicidades, adivinaste el numero secreto')
        print(f'El numero secreto es {n_numero_secreto}')
        print(f'Lo adivinaste en {n_intentos} intentos')
        
    elif n_opcion == 2:
        n_intentos = 0
        print('++ Nivel Avanzado ++ \n')
        n_numero_secreto = random.randint(1, 50)
        n_intentos = indica_limite()
        n_numero = introduce_numero()
        while n_numero != n_numero_secreto and n_intentos > 0:
            if n_numero < n_numero_secreto:
                print('El numero secreto es mayor')
                n_intentos -= 1
                if n_intentos == 0:
                    print('Lo siento, has perdido')
                    break
                else:
                    print(f'Te quedan {n_intentos} intentos')
                    n_numero = introduce_numero()
            elif n_numero > n_numero_secreto:
                print('El numero secreto es menor')
                n_intentos -= 1
                if n_intentos == 0:
                    print('Lo siento, has perdido')
                    break
                else:
                    print(f'Te quedan {n_intentos} intentos')
                    n_numero = introduce_numero()

        print('Felicidades, adivinaste el numero secreto')
        print(f'El numero secreto es {n_numero_secreto}')
        print(f'Lo adivinaste en {n_intentos} intentos')

    elif n_opcion == 3:
        print('Gracias por jugar \n')
        is_salida = True
    else:
        print('Por favor selecciona una opcion valida')


