# Obtener Coordenadas

def obtener_coordenadas():
    x, y, z = 10, 20, 30
    return x, y, z    # = return (x, y, z)

resultado = obtener_coordenadas()
print(resultado)

# unpacking
x1, y2, z3 = resultado

# Imprimir los valores de manera individual
print(f'Coordenadas x = {x1}, y = {y2}, z = {z3}')

