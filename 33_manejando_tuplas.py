# Gestionando tuplas

# Las tuplas son inmutables, no se pueden modificar una vez creadas.
# Las tuplas son similares a las listas, pero no se pueden modificar.
# Se definen con paréntesis () y se separan por comas.
# Se pueden crear tuplas vacías o con elementos.

# no se puede append ni modificar

ts_coordenadas = (90, 135, 45)
print(f'la coordenada X es la coordenada {ts_coordenadas[0]}')
print(f'la coordenada Y es la coordenada {ts_coordenadas[1]}')
print(f'la coordenada Z es la coordenada {ts_coordenadas[2]}')

x, y, z = ts_coordenadas
print(f'ts_coordenadas completas: {ts_coordenadas}')

print(f'las coordenadas son: X = {x}, y = {y}, z = {z}')

n_old_coordenadas = ts_coordenadas[0], ts_coordenadas[1], ts_coordenadas[2]
print(f'las coordenadas viejas son: {n_old_coordenadas}')
print()

# Combinacion de tuplas y listas
print('--------------------------------')
print('Combinacion de tuplas y listas')
print('--------------------------------')

productos = [
    ('P001', 'Laptop', 1000, 2), # tupla 1 id, tipo, precio, cantidad
    ('P089', 'Celular', 500, 5), # tupla 2 id, tipo, precio, cantidad
    ('P015', 'Tablet', 300, 10), # tupla 3 id, tipo, precio, cantidad
]

precio_total = 0
print(f'Información de los productos: ')
for producto in productos:
    # print(producto)
    id, tipo, precio, cantidad = producto
    print(f'   id = {id}, tipo = {tipo}, precio = {precio} y cantidad = {cantidad}')
    precio_total += precio

print(f'Precio total: {precio_total}')
print()
