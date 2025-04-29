class Orden:
    contador_ordenes = 0

    def __init__(self, computadoras):
        Orden.contador_ordenes += 1
        self.id_orden = Orden.contador_ordenes

        # Recibimos la lista de objetos de tipo Computadora
        self.computadoras = []

    def agregar_supercomputadora(self, computadora):
        self.computadoras.append(computadora)
    
    def __str__(self):
        computadora_str = ' '
        for computadora in self.computadoras:
            computadora_str += '\n' + computadora.__str__()

        return (f'''Orden {self.id_orden}
        Computadoras: {computadora_str}''')
