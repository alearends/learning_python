# Juego de adivinar numero secreto

from random import randint

numero_secreto = randint(1, 50)
intentos = 0
INTENTOS_MAXIMOS = 5
adivinanza = None

while adivinanza != numero_secreto and intentos < INTENTOS_MAXIMOS:
    adivinanza = int(input('Adivina el número secreto entre 1 y 50: '))
    intentos += 1

    # Agregamos una guia para que sepa si el numero es mayor o menor que el numero secreto
    if adivinanza < numero_secreto:
        print('El número secreto es mayor.')
    elif adivinanza > numero_secreto:
        print('El número secreto es menor.')

    if adivinanza == numero_secreto:
        print('¡Felicidades, adivinaste el número secreto en {intentos} intentos!')
    else:
        print(f'Lo siento, has agotado tus intentos que eran {INTENTOS_MAXIMOS}. El número secreto era {numero_secreto}.')


print(f'Felicidades, adivinaste el número secreto {numero_secreto} en {intentos} intentos.\n')