# La función zip() en Python:
# ----------------------------
# 1. PROPÓSITO:
#    - Combina múltiples iterables (listas, tuplas, etc.) "emparejando" sus elementos.
#    - Como un cierre relámpago (zip), une elementos en el mismo índice.

# 2. SINTAXIS:
#    zip(iterable1, iterable2, ...) → Devuelve un objeto zip (iterador de tuplas).

# 3. FUNCIONAMIENTO:
#    - Toma el primer elemento de cada iterable y los agrupa en una tupla.
#    - Luego el segundo elemento de cada uno, y así sucesivamente.
#    - Si los iterables son de diferente longitud, se detiene en el más corto.

# 4. USO COMÚN:
#    - Para iterar sobre múltiples listas en paralelo.
#    - Convertir columnas de datos en filas (transposición).

# -------------------------------------------------------------------------------------------------------------

# Supongamos que tenemos 3 listas de personajes de Marvel:
superheroes = ["Iron Man", "Spider-Man", "Thor", "Hulk"]
villanos = ["Thanos", "Green Goblin", "Loki"]
poderes = ["Tecnología", "Telarañas", "Rayos", "Fuerza"]

# 1. Crear un equipo de batalla combinado con zip():
equipos_marvel = zip(superheroes, villanos, poderes)
print(f'etapa 1: {equipos_marvel}')

# 2. Convertir el objeto zip en una lista para visualización:
lista_equipos = list(equipos_marvel)
print(f'etapa 2: {lista_equipos}')
print ('Hulk no aparece porque villanos solo tiene 3 elementos')

# 3. Mostrar los emparejamientos:
print("\n⚡ etapa 3: \n¡Combates épicos! ⚡")
for heroe, villano, poder in lista_equipos:
    print(f"{heroe} ({poder}) vs {villano}")

