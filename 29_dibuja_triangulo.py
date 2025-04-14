# usar For para dibujar un triangulo

ASTERICO = '*'

while True:
    try:
        numero_filas = int(input('Indica el numero de filas del triangulo: '))
        if (numero_filas > 0):
            break
        else:
            print('Por favor ingresa un numero mayor a cero')
    except ValueError:
        print('Por favor ingresa un numero entero')


# dibujar el triangulo pegado al margen izquierdo
for i in range(1, numero_filas + 1):
    print(ASTERICO * i)
print('\n') # dejar un espacio entre los triangulos

# dibujar el triangulo centrado
for i in range(1, numero_filas + 1):
    espacios_en_blanco = ' ' * (numero_filas - i) # Espacios en blanco para centrar el triangulo
    caracteres = ASTERICO * (2 * i - 1) # Caracteres para dibujar el triangulo centrado
    print(f'{espacios_en_blanco}{caracteres}')
print('\n') # dejar un espacio al final