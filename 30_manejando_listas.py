# Manejando listas

n_mi_lista = [10, 20, 30, 40, 50]
print(f'Lista original: {n_mi_lista}') # [10, 20, 30, 40, 50]

# Longitud de la lista
print(f'  Longitud de la lista: {len(n_mi_lista)}') # 5

#Acceder a un elemento de la lista
print(f'Accedemos al valor del indice 3: {n_mi_lista[3]}') # 40

# Modificar un elemento de la lista
n_mi_lista[3] = 100
print(f'Modificamos el valor del indice 3: {n_mi_lista[3]}') # 100
print(f'  Longitud de la lista: {len(n_mi_lista)}') # 5

# Agregamos un elemento al final de la lista
n_mi_lista.append(60)
print(f'Agregamos un elemento al final de la lista: {n_mi_lista}') # [10, 20, 30, 100, 50, 60]
print(f'  Longitud de la lista: {len(n_mi_lista)}') # 6

# Eliminar un elemento de la lista
del n_mi_lista[2]   # Elimina el elemento en el indice 2
print(f'Eliminamos el elemento en el indice 2: {n_mi_lista}') # [10, 20, 100, 50, 60]
print(f'  Longitud de la lista: {len(n_mi_lista)}') # 5

# Lista de palabras
nombres = ['Juan', 'Pedro', 'Maria', 'Jose']
print(f'Lista de nombres original: {nombres}') # ['Juan', 'Pedro', 'Maria', 'Jose']

# Iterar una lista con un for
for nombre in nombres:
    print(f'Hola {nombre}')

# Lista_heterogenea
lista_heterogenea = [10, 'Juan', 20.5, True, [1, 2, 3]]

# Iterar Lista_heterogenea con for
for elemento in range(len(lista_heterogenea)):
    print(f'El elemento {elemento} de la lista Heterogea es: {lista_heterogenea[elemento]}')
print()  # Espacio entre los elementos

for elemento in lista_heterogenea:
    print(f'El elemento de la lista Heterogea es: {elemento}')