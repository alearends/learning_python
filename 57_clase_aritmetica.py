# Ejercicio de gestion de objetos
# Crear una Clase Aritmetica
# Debe tener:
# - Atributo Operando1
# - Atributo Operando2
# - Metodos Sumar, Restar, multiplicar, dividir
# Luego hay que crear 2 oobjetos
# Hay que incluir el constructor

class Aritmetica:
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2

    def sumar(self):
        resultado = self.operando1 + self.operando2
        print(f'Resultado suma: {resultado}')
    
    def restar(self):
        resultado = self.operando1 - self.operando2
        print(f'Resultado resta: {resultado}')
    
    def multiplicar(self):
        resultado = self.operando1 * self.operando2
        print(f'Resultado multiplicar: {resultado}')
    
    def dividir(self):
        resultado = self.operando1 / self.operando2
        print(f'Resultado dividir: {resultado}')

# Programa Principal
if __name__ == '__main__':
    print('--- Clase Aritmetica ---')
    aritmetica1 = Aritmetica(5, 7)
    aritmetica1.sumar()
    aritmetica1.restar()
    aritmetica1.multiplicar()
    aritmetica1.dividir()

    aritmetica2 = Aritmetica(12, 16)
    aritmetica2.sumar()
    aritmetica2.restar()
    aritmetica2.multiplicar()
    aritmetica2.dividir()