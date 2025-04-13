#Ejercicio Suma acumulada con while

print('*** Suma acumulada de numeros con while ***')
MAXIMO_NUMERO=5
n_suma_acumulada=0
numero = 1

while numero <= MAXIMO_NUMERO:
    n_suma_acumulada += numero
    print(f'El acumulado hasta ahora es {n_suma_acumulada}')
    numero += 1
print(f'La suma acumulada es {n_suma_acumulada}')

#Ejercicio Suma acumulada con for

print('*** Suma acumulada de numeros con for ***')
MAXIMO_NUMERO=5
n_suma_acumulada=0

for numero in range(MAXIMO_NUMERO + 1):
    n_suma_acumulada += numero
    print(f'El acumulado hasta ahora es {n_suma_acumulada}')

print(f'La suma acumulada es {n_suma_acumulada}')

