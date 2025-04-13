# menu iterativo

print ('*** Menu iterativo ***')

is_salida = False

while not is_salida:
    print('''
    1. Crear Cuenta
    2. Eliminar Cuenta
    3. Salir
''')
    n_opcion = int(input('Por favor selecciona una opcion: '))
    
    if n_opcion == 1:
        print('La cuenta fue creada \n')
    elif n_opcion == 2:
        print('La cuenta fue eliminada \n')
    elif n_opcion == 3:
        print('Gracias por usar el sistema \n')
        is_salida = True
    else:
        print('Por favor selecciona una opcion valida')
