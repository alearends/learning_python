# Sistema que valida si un numero esta dentro de un rango

n_minimo = float(input('indica el numero minimo:'))
n_maximo = float(input('indica el numero máximo:'))
n_evaluar = float(input('indica el numero a evaluar:'))

if n_evaluar >= n_minimo and n_evaluar <= n_maximo:
    print(f'El número {n_evaluar} esta entre {n_minimo} y {n_maximo}')
    
