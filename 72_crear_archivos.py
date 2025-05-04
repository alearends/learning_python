# 1. crear un archivo con python
nombre_archivo = 'archivo_con_python.txt'

# 2. Abrir el archivo en modo escritura (w)
archivo = open(nombre_archivo, 'w')

# 3. Escribir en el archivo
archivo.write('Esto es una prueba')
archivo.write('\nestoy agregando informacion al archivo\n')

# 4. Cerrar el archivo, para liberar los recursos y no se pueda seguir escribiendo en ese archivo
archivo.close()


print(f'se creo el archivo: {nombre_archivo}')