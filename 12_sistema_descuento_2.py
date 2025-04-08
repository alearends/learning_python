# Sistema que ofrece descuentos dependiendo del monto de la compra o si es miembro VIP


# (if (s_vip.upper() == 'S') or ('N'))  # 'N' siempre es True porque no está comparando nada
# Posibles soluciones: 
# 1. if s_vip.upper() in ('S', 'N'):
    # break
# 2. if s_vip.upper() == 'S' or s_vip.upper() == 'N':
    #  break



while True:
    try:
        s_vip = input('Eres VIP ? (S / N): ')
        if s_vip.upper() in ('S', 'N'): 
            break
        else:
            print('Por favor ingresa una de las dos opciones --> S o N: ')
    except ValueError:
        print('Por favor ingresa una de las dos opciones --> S o N: ')
    


while True:
    try:
        n_monto_compra = float(input('Indica el monto total de tu compra: '))
        if n_monto_compra >= 1000 and s_vip.upper() == 'S':
            n_total_pagar = n_monto_compra - (n_monto_compra * 0.1)
            print(f'el total a pagar es de {n_total_pagar} despues de aplicar un descuento del 10% sobre {n_monto_compra}')
        elif n_monto_compra < 1000 and s_vip.upper() == 'S':
            n_total_pagar = n_monto_compra - (n_monto_compra * 0.05)
            print(f'el total a pagar es de {n_total_pagar} despues de aplicar un descuento del 5% sobre {n_monto_compra}')
        else:
            n_total_pagar = n_monto_compra
            print(f'Hazte miembro si deseas obtener un descuento. El total a pagar es de {n_total_pagar} sin descuento')
        break
    except ValueError:
        n_monto_compra = float(input('Por favor ingresa un monto valido: '))


