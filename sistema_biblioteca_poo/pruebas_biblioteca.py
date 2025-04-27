from sistema_biblioteca_poo.biblioteca import Biblioteca
from sistema_biblioteca_poo.libro import Libro

bibliotecaLatina = Biblioteca('Biblioteca Latinoamericana')

# Agregar carios libros
libro1 = Libro("Fundación", "Isaac Asimov", "Ciencia ficción")
libro2 = Libro("Dune", "Frank Herbert", "Ciencia ficción")
libro3 = Libro("El fin de la eternidad", "Isaac Asimov", "Ciencia ficción")
libro4 = Libro("La rebelión de Lucifer", "J.J. Benítez", "Misterio")
libro5 = Libro("Estoy bien", "J.J. Benítez", "Drama")

# Agregar los Libros a la biblioteca
bibliotecaLatina.agregar_libro(libro1)
bibliotecaLatina.agregar_libro(libro2)
bibliotecaLatina.agregar_libro(libro3)
bibliotecaLatina.agregar_libro(libro4)
bibliotecaLatina.agregar_libro(libro5)

# Nombre de la Biblioteca
print(f'*** Bienvenidos a la {bibliotecaLatina.nombre} ***')

# Buscar Libros por autor
print(f'\nLibros de Isaac Asimov')
bibliotecaLatina.buscar_libro_por_autor('Isaac Asimov')

# Buscar Libros por genero
print(f'\nLibros de Ciencia ficción: ')
bibliotecaLatina.buscar_libros_por_genero('Ciencia ficción')

# Mostrar todos los libros de la biblioteca
bibliotecaLatina.mostrar_todos_los_libros()

# Para Ejecutar este Sistema:
# Abre la terminal en \Experimentos\
# Ejecuta: python -m sistema_biblioteca_poo.pruebas_biblioteca