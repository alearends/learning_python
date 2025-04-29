from mundo_pc.monitor import Monitor
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado


class Computadora:
    contador_computadora = 0

    def __init__(self, nombre, monitor, raton, *teclado):
        Computadora.contador_computadora += 1
        self.id_computadora = Computadora.contador_computadora
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton

    def __str__(self):
        ", ".join(str(teclado) for teclado in self.teclado)
        
        return (f'''{self.nombre}: {self.id_computadora}
        Monitor: {self.monitor}
        Teclado: {self.teclado}
        Raton: {self.raton}''')
    
# Codigo principal
if __name__ == '__main__':
    teclado1 = Teclado('HP', 'USB')
    raton1 = Raton('HP', 'USB')
    monitor1 = Monitor('HP', 27)
    computadora1 = Computadora('HP', monitor1, raton1, teclado1)
    print(computadora1)

    teclado2 = Teclado('Gamer', 'Bluetooth')
    teclado3 = Teclado('Gamer', 'USB')
    raton2 = Raton('Gamer', 'Bluetooth')
    monitor2 = Monitor('Gamer', 34)
    computadora2 = Computadora('Gamer', monitor2, raton2, teclado2, teclado3)
    print(computadora2)