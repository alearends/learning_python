class Libro:
    def __init__(self, titulo, autor, genero):
        self._titulo = titulo
        self._autor = autor
        self._genero = genero

    @property                   # Esto sustituye a los getter
    def titulo(self):           # def get_titulo(self):
        return self._titulo
    
    @property 
    def autor(self):
        return self._autor
    
    @property 
    def genero(self):
        return self._genero
    
    # Setters (para permitir modificación)
    @titulo.setter
    def titulo(self, value):
        self._titulo = value

    @autor.setter
    def autor(self, value):
        self._autor = value    

    @genero.setter
    def genero(self, value):
        self._genero = value    

if __name__ == '__main__':
    libro = Libro('titulo', 'autor', 'genero')
    # libro.titulo =  'titulo2' # Esto marca error porque no hay un setter 
    print(f'Accediendo a la propiedad de titulo: {libro.titulo}')