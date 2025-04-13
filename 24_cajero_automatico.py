# Ejercicio de Cajero automatico

print ('*** Cajero automatico ***')

is_salida = False
n_saldo = 10000000


while not is_salida:

    print('''
Operaciones que puedes realizar:
    1. Consultar Saldo
    2. Retirar Dinero
    3. Depositar Dinero
    4. Salir
''')

    n_opcion = int(input('Por favor selecciona una opcion: '))

    if n_opcion == 1:
        print(f'El saldo actual es de {n_saldo} \n')
    
    elif n_opcion == 2:
        n_retiro = float(input('¿Cuánto vas a retirar? '))
        if n_retiro > n_saldo:
            print('No tienes suficiente saldo para retirar esa cantidad')
        elif n_retiro <= 0:
            print('Por favor ingresa un monto valido')
        else:
            n_saldo -= n_retiro
            print(f'Has retirado {n_retiro}')
            print(f'El saldo actual es de {n_saldo} \n')
            
    elif n_opcion == 3:
        n_deposito = float(input('¿Cuánto vas a depositar? '))
        if n_deposito <= 0:
            print('Por favor ingresa un monto valido')
        else:
            n_saldo += n_deposito
            print(f'Has depositado {n_deposito}')
            print(f'El saldo actual es de {n_saldo} \n')
    
    elif n_opcion == 4:
        print('Gracias por usar nuestros cajeros \n')
        is_salida = True
    
    else:
        print('Por favor selecciona una opcion valida')



