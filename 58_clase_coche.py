

class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca # atributo publico
        self._modelo = modelo # atributo protegido
        self.__color = color # atributo privado

    def conducir(self):
        print(f'''Conduciendo el coche:
            Marca: {self.marca}
            Modelo: {self._modelo}
            Color: {self.__color}''')

# Programa Principal
if __name__ == '__main__':
    # Creacion de un primer coche
    coche1 = Coche('Toyota', 'Yaris', 'Azul')
    coche1.conducir()
    # En este momento no deberias acceder directamente a los atributos protegidos o privados
    coche1.marca = 'Toyota 2'
    coche1._modelo = 'Yaris 2' # Esto es una mala practica, me refiero a modificar al atributo protegido
    coche1.__color = 'Azul 2'  # Python ignora el cambio, porque el atributo es privado
    coche1._Coche__color = 'Azul 3' # Esto es una mala practica, me refiero a modificar al atributo privado
    coche1.conducir()
