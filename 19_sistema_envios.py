# Programa para determinar el costo de envio de un paquete basado en su peso y los kilometras a viajar

TARIFA_NACIONAL = 10
TARIFA_INTERNACIONAL = 20

while True:
    try:
        n_peso = float(input('Por favor indica el peso en kilos del paquete: '))
        if n_peso > 0:
            break
        else:
            print('Por favor ingresa un peso mayor a cero')
    except ValueError:
        print('Por favor ingresa un peso valido')

while True :
    try:
        s_destino = input('Por favor indica el destino del paquete (nacional o internacional): ').strip().lower()
        if s_destino in ['nacional', 'internacional']:
            break
        else:
            print('Por favor ingresa un destino valido (nacional o internacional)')
    except ValueError:
        print('Por favor escoge un destino valido (nacional o internacional)')

if s_destino == 'nacional':
    n_pagar = n_peso * TARIFA_NACIONAL
else:
    n_pagar = n_peso * TARIFA_INTERNACIONAL

print(f' ☑ ☑ El costo de envio es de {n_pagar} para un paquete de {n_peso} kilos y con destino {s_destino}\n')