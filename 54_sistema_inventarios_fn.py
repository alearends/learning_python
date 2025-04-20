# Sistema de inventarios con funciones

print('*** Sistema de inventarios con funciones ***')

# Inventario del almacen (harcodeado)
inventario = [
    {"id": 1, "nombre": "Teclado Mecánico", "precio": 45.99, "cantidad": 10},
    {"id": 2, "nombre": "Mouse Inalámbrico", "precio": 25.50, "cantidad": 15},
    {"id": 3, "nombre": "Monitor 24 pulgadas", "precio": 120.00, "cantidad": 7}
]

# Funcion para mostrar inventario
def mostrar_inventario():
    print('Inventario del almacen: ')
    for producto in inventario:
        print(f"ID: {producto.get('id')}, Nombre: {producto.get('nombre')}, Precio: €{producto.get('precio')}, Cantidad: {producto.get('cantidad')}")

# Función para agregar producto
def agregar_producto():
    # pass  # No hara nada, solo pasara por esta funcion sin ejecutar nada
    print('--- Agregar un nuevo producto ---')

    # Obtener el siguiente id automáticamente
    if inventario:
        nuevo_id = max(producto["id"] for producto in inventario) + 1
    else:
        nuevo_id = 1  # Si el inventario está vacío

    nombre = input('Nombre: ')
    precio = float(input('Precio: '))
    cantidad = int(input('Cantidad: '))
    nuevo_producto = {'id': nuevo_id, 'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
    inventario.append(nuevo_producto)
    print('---> Producto agregado exitosamente')

# Funcion para buscar producto por ID
def buscar_producto_por_id():
    print('--- Buscar producto por ID ---')
    id_buscado = int(input('Ingrese el ID a buscar: '))
    for producto in inventario:
        if producto.get('id') == id_buscado:
            print('\nInformación del producto encontrado: ')
            print(f"  ID: {producto.get('id')}, Nombre: {producto.get('nombre')}, Precio: €{producto.get('precio')}, Cantidad: {producto.get('cantidad')}")
            return
    print('\n Producto no encontrado')

# Función para borrar producto por ID
def borrar_producto_por_id():
    print('--- Borrar producto por ID ---')
    id_borrar = int(input('Ingrese el ID del producto a borrar: '))
    for producto in inventario:
        if producto.get('id') == id_borrar:
            inventario.remove(producto)
            print(f'---> Producto con ID {id_borrar} eliminado exitosamente')
            return
    print(f'---> Producto con ID {id_borrar} no encontrado')

# Programa principal
if __name__=='__main__':
    while True:
        try:
            print(f'''\n--- Menu ---
                1. Mostrar inventario
                2. Agregar nuevo producto
                3. Buscar producto por Id
                4. Borrar producto por Id
                5. Salir''')
            opcion = int(input('Proporciona una opcion (1-5): '))
            if opcion == 1: # Mostrar inventario
                mostrar_inventario()
            elif opcion == 2: # Agregar producto
                agregar_producto()
            elif opcion == 3: # Buscar producto por Id
                buscar_producto_por_id()
            elif opcion == 4: # borrar producto por Id
                borrar_producto_por_id()
            elif opcion == 5: # Salir
                print('Hasta luego')
                break
            else: 
                print('Opción invalida, proporciona una opción valida')
        except ValueError:
            print('Opción invalida, proporciona una opción valida')