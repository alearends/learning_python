from mundo_pc.computadora import Computadora
from mundo_pc.monitor import Monitor
from mundo_pc.orden import Orden
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado


print('*** Mundo PC ***')

# Creamos una primer orden
teclado1 = Teclado('HP', 'USB')
raton1 = Raton('HP', 'USB')
monitor1 = Monitor('HP', 27)
computadora1 = Computadora('HP', monitor1, raton1, teclado1)

teclado2 = Teclado('Gamer', 'Bluetooth')
teclado3 = Teclado('Gamer', 'USB')
raton2 = Raton('Gamer', 'Bluetooth')
monitor2 = Monitor('Gamer', 34)
computadora2 = Computadora('Gamer', monitor2, raton2, teclado2, teclado3)


computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)
print(orden1)

teclado4 = Teclado('Dell', 'Bluetooth')
raton4 = Raton('Dell', 'Bluetooth')
monitor4 = Monitor('Dell', 27)
computadora4 = Computadora('Dell', monitor4, teclado4, raton4)
orden1.agregar_computadora(computadora4)
print(orden1)
