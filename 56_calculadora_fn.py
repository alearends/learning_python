# Ejemplo de calculadora con funciones

def mostrar_menu():
    print(f'''\n--- Menu ---
                1. Suma
                2. Resta
                3. Multiplicación
                4. División
                5. Salir''')
    opcion = int(input('Escoje una opción: '))
    return opcion

def suma(*args):
    if not args:
        return 0
    total = 0
    for numero in args:
        total += numero
    return total

def resta(*args):
    if not args:
        return 0
    total = 0
    for numero in args:
        total -= numero
    return total

def multiplica(*args):
    if not args:
        return 0
    total = args[0]
    for numero in args[1:]:
        total *= numero
    return total

def divide(*args):
    if not args:
        return 0
    total = args[0]
    for numero in args[1:]:
        if numero == 0:
            print("⚠️ No se puede dividir entre 0")
            return None
        total /= numero
    return total



# Programa principal
if __name__=='__main__':
    print('*** Maquina de Snacks ***')
    while True:
        try:
            opcion = mostrar_menu()
            
            if opcion == 1: # suma
                entrada = input("Ingresa los números separados por coma: ")  # ejemplo: 4,5,6
                numeros = [float(n) for n in entrada.split(',')]
                resultado = suma(*numeros)
                print(f"Resultado: {resultado}")
            elif opcion == 2: # resta
                entrada = input("Ingresa los números separados por coma: ")  # ejemplo: 4,5,6
                numeros = [float(n) for n in entrada.split(',')]
                resultado = resta(*numeros)
                print(f"Resultado: {resultado}")
            elif opcion == 3: # multiplica
                entrada = input("Ingresa los números separados por coma: ")  # ejemplo: 4,5,6
                numeros = [float(n) for n in entrada.split(',')]
                resultado = multiplica(*numeros)
                print(f"Resultado: {resultado}")
            elif opcion == 4: # divide
                entrada = input("Ingresa los números separados por coma: ")  # ejemplo: 4,5,6
                numeros = [float(n) for n in entrada.split(',')]
                resultado = divide(*numeros)
                print(f"Resultado: {resultado}")
            elif opcion == 5: # Salir
                print('Regresa pronto!')
                break
            else: 
                print('Opción invalida, proporciona una opción valida')
        except ValueError:
            print('Opción invalida, proporciona una opción valida')


