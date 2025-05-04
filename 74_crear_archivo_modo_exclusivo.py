# 1. crear un archivo con python
nombre_archivo = 'archivo_con_python.txt'

try:
    # Usar el comando with y asociarlo a la variable "archivo"
    # 2. Abrir el archivo en modo excepcion (x)
    with open(nombre_archivo, 'x') as archivo:

        # 3. Escribir en el archivo
        archivo.write('Escritura en modo exclusivo')
        archivo.write('\nEspero que sea util\n')
    
    print(f'Se ha creado el archivo: {nombre_archivo}')

except FileExistsError as e:
    print('el archivo ya existe\n') 
    print(f'Detalle del error: {e}')
