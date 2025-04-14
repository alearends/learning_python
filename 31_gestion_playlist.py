# Crear un programa que gestione listas
# - Solicitar al usuario cuantas canciones quiere
# - Solicitar al usuario cada cancion
# - desplegar la lista de canciones en orden alfabetico

ls_playlist = []

while True:
    try:
        n_cantidad_canciones = int(input('Cuantas canciones deseas agregar a la lista? '))
        if n_cantidad_canciones > 0:
            break
        else:
            print('Por favor ingresa un número mayor a cero')
    except ValueError:
        print('Por favor ingresa un número entero')

for i in range(n_cantidad_canciones):
    s_cancion = input(f'Por favor indicar el nombre de la cancion {i + 1}:  ')
    ls_playlist.append(s_cancion)
    print(f'Cancion {i + 1} agregada a la lista')   

ls_playlist_alphabetico = sorted(ls_playlist) # Ordenar la lista de canciones en orden alfabetico

print(f'La Lista de canciones ordenadas alfabeticamente es: ')
for cancion in ls_playlist_alphabetico:
    print(f' - {cancion}')

print()



