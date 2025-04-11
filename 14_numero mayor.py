# Programa que determine el mayor de todos los numeros

while True:
    try:
        n_cantidad_numeros = int(input('Cuántos numeros deseas comparar? '))
        if n_cantidad_numeros > 0:
            break
        else:
            print('Por favor ingresa un número mayor a cero')
    except ValueError:
        print('Por favor ingresa un número entero')

# solicitarle al usuario tantos numeros como n_cantidad_numeros

n_numeros = []

for i in range(n_cantidad_numeros):
    while True:
        try:
            n_numero = float(input(f'Por favor indicar el numero {i + 1}:  '))
            n_numeros.append(n_numero)
            break
        except ValueError:
            print('Por favor ingresa un número valido')

# determinar el mayor de todos los numeros
# comparando cada numero con el resto de los numeros
n_mayor = n_numeros[0]
for i in range(0, len(n_numeros)):
    if n_numeros[i] > n_mayor:
        n_mayor = n_numeros[i]

print(f'\nEl mayor de todos los numeros es {n_mayor}\n')    
