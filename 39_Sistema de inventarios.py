# Gestion de inventarios

# Usar lista para mantener un registro de los productos disponibles
# Usar diccionario para almacenar detalle del producto

inventario = []

is_salida = False

while not is_salida:

    print('''
    1. Agregar un Producto 
    2. Eliminar un Producto 
    3. Ver la lista de Productos
    4. Ver detalles del Producto 
    5. Salir 
''')
    
    try:
        n_opcion = int(input('Por favor selecciona una opcion: '))
    except ValueError:
        print('Por favor ingresa un número válido.')
        continue
    
    if n_opcion == 1:
        s_new_producto = input('Ingresa el nombre de un producto: ').strip().lower()

        # Validar si el producto ya existe
        existe = any(p['nombre'] == s_new_producto for p in inventario)
        if existe:
            print('Este producto ya está en el inventario.\n')
            continue

        try:
            precio = float(input('Ingresa el precio del producto: '))
            cantidad = int(input('Ingresa la cantidad disponible: '))
        except ValueError:
            print('Precio o cantidad inválida.\n')
            continue

        # Crear diccionario del producto
        nuevo_producto = {
            'id': len(inventario) + 1,  # ID automático
            'nombre': s_new_producto,
            'precio': precio,
            'cantidad': cantidad
        }

        # Agregar a la lista de inventario
        inventario.append(nuevo_producto)
        print(f'Producto "{s_new_producto}" agregado correctamente.\n')


    elif n_opcion == 2:
        s_remove_producto = input('Ingresa el producto a eliminar de la lista: ').strip().lower()

        # Buscar el producto por nombre
        producto_encontrado = None
        for producto in inventario:
            if producto['nombre'] == s_remove_producto:
                producto_encontrado = producto
                break

        # Si se encuentra, eliminarlo
            if producto_encontrado:
                inventario.remove(producto_encontrado)
                print(f'El producto "{s_remove_producto}" ha sido eliminado.\n')
            else:
                print('Este producto no se encuentra en el inventario.\n')

    elif n_opcion == 3:
        if inventario:
            print('\nLista de productos disponibles:')
        for producto in inventario:
            print(f"- {producto['nombre'].title()} (ID: {producto['id']})")
            print()  # línea en blanco para formato
        else:
            print('El inventario está vacío.\n')

    elif n_opcion == 4:
        s_detalle_producto = input('Ingresa el nombre del producto para ver los detalles: ').strip().lower()
    
        producto_encontrado = False
        for producto in inventario:
            if producto['nombre'] == s_detalle_producto:
                print(f"""
                    Detalles del Producto:
                    ID: {producto['id']}
                    Nombre: {producto['nombre'].title()}
                    Precio: ${producto['precio']:.2f}
                    Cantidad disponible: {producto['cantidad']}
                """)
                producto_encontrado = True
                break  # Ya lo encontramos, no hay que seguir buscando
    
            if not producto_encontrado:
                print('El producto no fue encontrado en el inventario.\n')


    elif n_opcion == 5: 
        print('Gracias por usar el sistema \n')
        is_salida = True

    else:
        print('Por favor selecciona una opcion valida')





# Inventario = [
#     {
#         'id': 1,
#         'nombre':'Pantalones',
#         'precio': 50.99,
#         'cantidad': 100
#     },
#     {
#         'id': 2,
#         'nombre':'Camisas',
#         'precio': 30.99,
#         'cantidad': 100
#     },
#     {
#         'id': 3,
#         'nombre':'Zapatos',
#         'precio': 20.99,
#         'cantidad': 100
#     }
# ]