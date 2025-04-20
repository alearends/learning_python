# Maquina de Snacks

print('*** Maquina de Snacks ***')

snacks =  [
    {"id": 1, "nombre": "papas", "precio": 5.99, "cantidad": 10},
    {"id": 2, "nombre": "Helado", "precio": 5.50, "cantidad": 15}, 
    {"id": 3, "nombre": "pizza", "precio": 12.00, "cantidad": 7}
]

def mostrar_snacks()
    print('Inventario de Snacks: ')
    for producto in snacks:
        print(f"ID: {snacks.get('id')}, Nombre: {snacks.get('nombre')}, Precio: €{snacks.get('precio')}, Cantidad: {snacks.get('cantidad')}")

def comprar_snack():
    pass

def mostrar_ticket():
    pass


# Programa principal
if __name__=='__main__':
    while True:
        try:
            print(f'''\n--- Menu ---
                1. Mostrar Snacks
                2. Comprar Snack
                3. Mostrar Ticket
                4. Salir''')
            opcion = int(input('Proporciona una opcion (1-4): '))
            if opcion == 1: # Mostrar inventario
                mostrar_snacks()
            elif opcion == 2: # Agregar producto
                comprar_snack()
            elif opcion == 3: # Buscar producto por Id
                mostrar_ticket()
            elif opcion == 4: # Salir
                print('Hasta luego')
                break
            else: 
                print('Opción invalida, proporciona una opción valida')
        except ValueError:
            print('Opción invalida, proporciona una opción valida')