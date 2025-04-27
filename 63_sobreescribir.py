class Animal:
    def comer(self):
        print('Como muchas veces al dia')

    def dormir(self):
        print('Duermo muchas horas')


class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')

    # Sobreescribiendo el metodo heredado de la clase padre
    def dormir(self):
        print('Duermo 15 horas al día')

# Programa principal
print('*** Ejemplo de Herencia en Python ***')
print('Clase Padre, soy un Animal')
animal1 = Animal()
animal1.comer()
animal1.dormir()

print('\nClase Hija, soy un Perro')
perro1 = Perro()
perro1.comer()
perro1.dormir()  # Se llama el metodo sobreescrito en la clase hija
perro1.hacer_sonido()

print(f'\nCódigo con Sobreescritura (sin polimorfismo explícito)')
print(f'Aquí solo estamos llamando métodos directamente, sin aprovechar el polimorfismo.')
animal = Animal()
animal.dormir()  # Output: "Duermo muchas horas" (llama al método de Animal)
perro = Perro()
perro.dormir()   # Output: "Duermo 15 horas al día" (llama al método sobreescrito de Perro)

print(f'\nCódigo con polimorfismo')
def describir_animal(animal):  # Esta función acepta CUALQUIER Animal (o subclase)
    animal.dormir()  # Llama al método correcto según el tipo de objeto

# El polimorfismo está en que describir_animal() no sabe si recibe un Animal o un Perro, 
# pero llama al método correcto.
# La misma función (describir_animal()) se comporta de manera diferente según el tipo de objeto que reciba.
mi_animal = Animal()
mi_perro = Perro()

describir_animal(mi_animal)  # Output: "Duermo muchas horas" (Animal)
describir_animal(mi_perro)   # Output: "Duermo 15 horas al día" (Perro)