# Numero factorial

print('*** Calcular numero factorial con recursiva ***')

def factorial_recursivo(numero):
    if numero == 1 or numero == 0:
        return 1
    else:
        return numero * factorial_recursivo(numero - 1)
    

if __name__ == '__main__':
    
    while True:
        try:
            numero = int(input('Proporciona el numero para calcular su factorial: '))
            if numero >= 0:
                break
            else:
                print('Proporciona un numero mayor o igual a cero para calcular su factorial: ')
        except ValueError:
            print('El numero debe ser mayor o igual a cero para calcular su factorial')
    
    resultado = factorial_recursivo(numero)
    print(f'El factorial del numero {numero} es {resultado:,}')