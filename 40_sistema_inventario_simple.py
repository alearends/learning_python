print('\n*** Sistema de inventarios Simple ***')

# Definimos la variable de inventarios
inventario = []

numero_productos = int(input('Cuantos productos deseas agregar al inventario? '))

for indice in range(numero_productos):
    print(f'Proporciona los valores del producto # {indice + 1}')
    nombre = input('Nombre: ')
    precio = float(input('Precio: '))
    cantidad = int(input('Cantidad: '))
    # Crear el diiccionario con el detalle del nuevo producto
    producto = {'id': indice, 'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
    # Agregamos el nuevo producto al inventario
    inventario.append(producto)

# Mostrar el inventario de manera simplificada
print(f'\n{inventario}')

# Buscar un producto por ID
id_buscar = int(input('\nindica el ID del producto que deseas buscar: '))

producto_encontrado = None

for producto in inventario:
    if producto.get('id') == id_buscar:
        producto_encontrado = producto
        break

if producto_encontrado:
    print(f'El producto con ID {id_buscar} fue encontrado')
    print(f'''
        ID: {producto_encontrado.get('id')},
        Nombre: {producto_encontrado.get('nombre')},
        Precio: {producto_encontrado.get('precio')},
        Cantidad: {producto_encontrado.get('cantidad')}''')
else:
    print('Producto con ID {id_buscar} no fue encontrado ')