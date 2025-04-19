# El resultado de esta función se vera al ejecutar el archivo a43_modulo_fn_sumar_body.py

def sumar(a, b):
    resultado = a + b
    return resultado


# Esta prueba solo aparecera en este acrivo porque se esta haciendo dentro del __name__ == '__main__'
if __name__ == '__main__':
    print(f'Prueba de la funcion sumar: {sumar(1, 2)}')
    print(f'Esta prueba solo aparecera en este archivo porque se esta haciendo dentro del __name__ == "__main__" \n')
