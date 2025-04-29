from mundo_pc.dispositivo_entrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    contador_teclados = 0

    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclados += 1
        self.id_teclado = Teclado.contador_teclados
        # self.marca = marca
        # self.tipo_entrada = tipo_entrada
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        # return super().__str__()
        return (f'Id: {self.id_teclado}, Marca: {self.marca}, Tipo Entrada: {self.tipo_entrada}')

# Codigo Principal
if __name__ == '__main__':
    teclado1 = Teclado('HP', 'USB')
    print(teclado1)
    teclado2 = Teclado('Acer', 'Bluetooth')
    print(teclado2)
    teclado3 = Teclado('Acer', 'USB')
    print(teclado3)