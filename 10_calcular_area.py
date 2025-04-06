# Herramienta para calcular multiples areas de figuras geometricas

while True:
    try:
        n_figura = int(input('indica si quieres calcular el area de un cuadrado (1), un rectangulo (2), un circulo (3) o un triangulo (4): '))
        if n_figura in [1,2,3,4]:
            break # Se sale del bucle porque es una opción valida
        else:
            print("Por favor ingresa un numero valido: 1, 2, 3 o 4")
    except ValueError:
        print('Por favor ingresa un numero valido: 1, 2, 3 o 4')
        




if n_figura == 1:
    # Cuadrado
    s_figura = 'cuadrado'
    n_lado = float(input('indica el lado del cuadrado: '))
    n_area = n_lado ** 2
    n_perimetro = n_lado * 4
    print(f'El área del {s_figura} es {n_area} y el perimetro es {n_perimetro}')
elif n_figura == 2:
    # Rectangulo
    s_figura = 'rectangulo'
    n_base = float(input('indica la base del rectangulo: '))
    n_altura = float(input('indica la altura del rectangulo: '))
    n_area = n_base * n_altura
    n_perimetro = (n_base + n_altura) * 2
    print(f'El área del {s_figura} es {n_area} y el perimetro es {n_perimetro}')
elif n_figura == 3:
    # Circulo
    s_figura = 'circulo'
    n_radio = float(input('indica el radio del circulo: '))
    n_area = 3.1416 * (n_radio ** 2)
    n_perimetro = 2 * 3.1416 * n_radio
    print(f'El área del {s_figura} es {n_area} y el perimetro es {n_perimetro}')
elif n_figura == 4:
    # Triangulo
    s_figura = 'triangulo'
    n_base = float(input('indica la base del triangulo: '))
    n_altura = float(input('indica la altura del triangulo: '))
    n_area = (n_base * n_altura) / 2
    n_perimetro = n_base + (n_altura * 2)
    print(f'El área del {s_figura} es {n_area} y el perimetro es {n_perimetro}')
else:
    print('No se ha encontrado la figura solicitada')
    