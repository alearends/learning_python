# Ejercios para gestionar conjuntos con python
# Los conjuntos o set son una colección no ordenada y mutable de elementos unicos
# no se admiten elementos unicos
# conjuntos = {1, 2, 3, 4}
# no tiene indices asociados

print('+++ Gestionando Conjuntos o Sets +++')
mi_set = {1, 2, 3, 4, 5, 4, 6}
print(f'mi set es: {mi_set}')

# agregando 3 elementos
mi_set.add(7)
mi_set.add(8)

print(mi_set)

# tratando de agregar un elemento repetido
mi_set.add(1)
print(mi_set)

# remove un elemento
mi_set.remove(4)
print(mi_set)

# iterar los elementos
for elemento in mi_set:
    print(elemento)

# iterar los elementos en una misma linea
for elemento in mi_set:
    print(elemento, end=' ')
print()

# Comprobar si existe un elemento en el set
print(2 in mi_set)

print(4 in mi_set)

# obtener la longitud de un set o conjunto
print(len(mi_set))

