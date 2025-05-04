print('*** Leer Archivo con Python ***')

print('*** Leyendo con el metodo readlines ***')

nombre_archivo = 'archivo_con_python.txt'

# Leer un archivo usando el metodo readlines
with open(nombre_archivo, 'r') as archivo:
    # Leer todas las lineas del archivo
    # print(archivo.readlines())
    lineas = archivo.readlines()
    for linea in lineas:
        print(linea.strip())

# Leer el contenido del archivo usando read
print('*** Leyendo con el metodo read ***')
with open(nombre_archivo, 'r') as archivo:
    print(archivo.read())