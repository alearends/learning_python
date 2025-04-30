# Creación de una lista simple vs una comprensiva
# ----------------------------------------------------------------------------------

# Procedimiento para crear una lista simple en Python:

# 1. Definir una variable que almacenará la lista.
# 2. Usar corchetes [] para delimitar los elementos.
# 3. Separar los elementos con comas.
# 4. Los elementos pueden ser de cualquier tipo (números, strings, etc.).

# Ejemplo: Filtrar números pares de una lista existente (enfoque tradicional) -----> 6 lineas de codigo
# 1. Lista original con números diversos
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 2. Crear una lista vacía para almacenar los pares
pares = []
# 3. Recorrer cada elemento de la lista original
for numero in numeros:
    # 4. Verificar si el número es par (divisible por 2 sin residuo)
    if numero % 2 == 0:
        # 5. Si es par, agregarlo a la nueva lista
        pares.append(numero)
# Resultado final
print("Lista simple (pares):", pares)  # Salida: [2, 4, 6, 8, 10]


# ----------------------------------------------------------------------------------

# Procedimiento para crear una lista por comprensión:

# 1. Definir una expresión para los elementos (ej: operación matemática).
# 2. Usar un bucle for dentro de corchetes [] para generar elementos dinámicamente.
# 3. Opcional: Añadir condiciones con 'if' para filtrar elementos.

# Sintaxis básica:
# [expresión for elemento in iterable if condición]

# Ejemplo: Filtrar números pares de una lista existente (enfoque tradicional) -----> 1 linea de codigo
# 1. Lista original con números diversos
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 2. Generar la nueva lista en una sola línea:
#    - Sintaxis: [expresión for elemento in iterable if condición]
pares = [numero for numero in numeros if numero % 2 == 0]

# Resultado final
print("Lista comprensiva (pares):", pares)  # Salida: [2, 4, 6, 8, 10]

