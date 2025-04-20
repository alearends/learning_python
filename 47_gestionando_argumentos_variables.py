# Argumentos variables en python

print('*** Argumentos variables en python ***')

def superheroe_superpoderes(nombre_Superheroe, nombre_humano, *args):
    print(f'\nSuperheroe: {nombre_Superheroe}, {nombre_humano} - {args}')
    # Iteramos Superpoderes
    for superpoder in args:
        print(f'\tSuperpoder: {superpoder}')

superheroe_superpoderes('Spiderman', 'Peter Parker', 'instinto aracnido', 'telaraña', 'se pega a superficies')
superheroe_superpoderes('Superman','Clark Kent', 'super fuerza', 'volar') # Los argimentos variables pueden pueden variar en cantidad
superheroe_superpoderes('Papa', 'Ernesto') # Es opcional enviar argumentos variables