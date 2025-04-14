# programa para administrar lista de suscriptores utilizando un email
# - un usuario se suscribe utilizando su email
# - a medida que crece la lista hay que asegurase de no tener duplicados
# - tambien se debe poder agregarse o eliminar suscriptores

print('*** Lista de Suscriptores ***')

cs_suscriptores = set()

is_salida = False

while not is_salida:
    print('''
    1. Agregar un Suscriptor
    2. Eliminar un suscriptor
    3. Ver la lista de suscriptores
    4. Salir
''')
    try:
        n_opcion = int(input('Por favor selecciona una opcion: '))
    except ValueError:
        print('Por favor ingresa un número válido.')
        continue
    
    if n_opcion == 1:
        s_new_suscriptor = input('ingresa el correo electronico para suscribirte: ' ).strip().lower()
        if '@' in s_new_suscriptor and '.' in s_new_suscriptor:
            if s_new_suscriptor in cs_suscriptores:
                print('Este correo ya está suscrito.\n')
            else:
                cs_suscriptores.add(s_new_suscriptor)
                print('¡Correo suscrito con éxito!\n')
        else:
            print('Correo no válido. Debe contener "@" y "."\n')

    elif n_opcion == 2:
        s_remove_suscriptor = input('Ingresa el correo a eliminar de la lista: ').strip().lower()
        if s_remove_suscriptor in cs_suscriptores:
            cs_suscriptores.remove(s_remove_suscriptor)
            print(f'La cuenta {s_remove_suscriptor} ha sido eliminada.\n')
        else:
            print('Este correo no se encuentra en la lista.\n')

    elif n_opcion == 3:
        if cs_suscriptores:
            print('\nLista de suscriptores:')
            for elemento in cs_suscriptores:
                print(f'- {elemento}')
            print()
        else:
            print('La lista de suscriptores está vacía.\n')

    elif n_opcion == 4:
        print('Gracias por usar el sistema \n')
        is_salida = True

    else:
        print('Por favor selecciona una opcion valida')
