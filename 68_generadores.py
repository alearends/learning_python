def funcion_normal():
    return [1, 2, 3]  # Devuelve toda la lista de una vez

def generador():
    yield 1  # Pausa aquí
    yield 2  # Luego aquí
    yield 3  # Finalmente aquí

# Uso:
print(funcion_normal())  # Output: [1, 2, 3] (toda la lista en memoria)

gen = generador()
print(next(gen))  # Output: 1 (solo genera el primero)
print(next(gen))  # Output: 2 (luego el segundo, manteniendo el estado)