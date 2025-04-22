# Maquina de Snacks

snacks =  [
    {"id": 1, "nombre": "Papas", "precio": 5.99},
    {"id": 2, "nombre": "Helado", "precio": 5.50}, 
    {"id": 3, "nombre": "pizza", "precio": 12.00}
]

# snacks a comprar. 
snacks_comprados = []

def mostrar_snacks():
    print('--- Snacks Disponibles --- ')
    for producto in snacks:
        print(f"ID: {producto.get('id')} -> {producto.get('nombre')} - €{producto.get('precio')}")

def buscar_snack_id(id_a_buscar):
    for snack in snacks:
        if snack.get('id') == id_a_buscar:
            return snack
    return None # no se encontro ningun snack con ese id

def comprar_snack():
    id_snack = int(input('Que Snack quieres comprar (id)? '))
    snack_encontrado = buscar_snack_id(id_snack)
    if snack_encontrado:
        snacks_comprados.append(snack_encontrado)
        print(f'Snack agregado: {snack_encontrado}')
    else:
        print(f'Snack NO encontrado con id: {id_snack}')

def mostrar_ticket():
    ticket = f'\t--- Ticket de Venta ---'
    total = 0
    for snack in snacks_comprados:
        ticket += f"\n\t - {snack.get('nombre')} - € {snack.get('precio'):.2f}"
        total += snack.get('precio')
    ticket += f'\nTOTAL -> € {total:.2f}'
    print(ticket)


# Programa principal
if __name__=='__main__':
    print('*** Maquina de Snacks ***')
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
            elif opcion == 2: # comprar producto
                comprar_snack()
            elif opcion == 3: # mostrar ticket
                mostrar_ticket()
            elif opcion == 4: # Salir
                print('Regresa pronto!')
                break
            else: 
                print('Opción invalida, proporciona una opción valida')
        except ValueError:
            print('Opción invalida, proporciona una opción valida')