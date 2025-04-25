
class Persona:
    # Atributo de clase
    contador_personas = 0

    def __init__(self, nombre, apellido):
        # Incrementamos el valor del atributo de clase
        Persona.contador_personas +=1
        self.id = Persona.contador_personas
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'Persona: 00{self.id}, {self.nombre}, {self.apellido}')

    @staticmethod
    def get_contador_personas_estatico():
        print('Metodo Estatico')
        return Persona.contador_personas
    
    @classmethod
    def get_contador_personas_clase(cls): # cls = class
        print('Metodo de Clase:')
        return cls.contador_personas

if __name__ == '__main__':
    print('\n*** Ejemplo Contador de Objetos ***')
    persona1 = Persona('Gerardo', 'Perez')
    persona2 = Persona('Daniel', 'Sanchez')

    persona1.mostrar_persona()
    persona2.mostrar_persona()

    # Imprimir el valor del contador de objetos de personas
    print(f'\nContador de objetos Persona: {Persona.contador_personas}')
    print(f'Contador objetos personas (static): {Persona.get_contador_personas_estatico()}')
    print(f'Contador de objetos Persona (clase): {Persona.get_contador_personas_clase()}')