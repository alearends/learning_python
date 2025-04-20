# Suma con Argumentos Variables

print('*** Suma con Argumentos Variables ***')

def sumar_args(*args):
    total = 0
    for numero in args:
        total += numero
    return total

resultado = sumar_args()

print(resultado)