# Definición de una función con 'def':

# 1. Se usa la palabra clave 'def' seguida del nombre de la función.
# 2. Puede tener múltiples líneas de código y lógica compleja.
# 3. Permite documentación (docstrings) y es más legible.
# 4. Se llama usando su nombre más paréntesis (ej: saludar()).

numero = int(input('indica un numero: '))   # Si numero = 2

def cuadrado(numero):
    return numero ** 2
print(f'El cuadrado de {numero}: {cuadrado(numero)}')  # El cuadrado de 2: 4

# -----------------------------------------------------------------

# Definición de una función lambda:

# 1. Es una función anónima (sin nombre) de una sola línea.
# 2. Sintaxis: lambda argumentos: expresión.
# 3. Útil para operaciones rápidas y simples.
# 4. Se usa comúnmente dentro de otras funciones (map, filter, etc.).

cuadrado_lambda = lambda numero: numero ** 2
print(f'El cuadrado_lambda de {numero}: {cuadrado_lambda(numero)}')  # El cuadrado_lambda de 2: 4


# -------------------------------------------------------------------

# Con map y lambda
# Se usa para iterar listas
# map(funcion, iterable) 
#  --> función = La función que se aplicará a cada elemento.
#  --> iterable = Lista, tupla, etc., cuyos elementos serán transformados.
# map() devuelve un objeto map (iterador). Para ver los resultados, conviértelo a lista con list(map(...))

numeros = [numero, numero+1, numero+2, numero+3, numero+4]  # numeros es [2, 3, 4, 5, 6]

cuadrados = list(map(lambda x: x ** 2, numeros))   # cuadrados es [4, 9, 16, 25, 36]
print(f'El resultado de usar map y lambda sobre la lista {numeros} es: {cuadrados}')  
# El resultado de usar map y lambda sobre la lista [2, 3, 4, 5, 6] es: [4, 9, 16, 25, 36

# -------------------------------------------------------------------

# Con filter y lambda
# Se usa para filtrar listas
# filter(funcion_condicional, iterable) 
#  --> función_condicional = Una función que devuelve True o False para cada elemento.
#  --> iterable = Lista, tupla, etc., cuyos elementos serán transformados.
# filter() devuelve un objeto filter (iterador). Para ver los resultados, conviértelo a lista con list(filter(...))

pares_cuadrados = list(filter(lambda x: x % 2 == 0, cuadrados))  
print(f'De los cuadrados {cuadrados} los números pares son {pares_cuadrados} ')
# De los cuadrados [4, 9, 16, 25, 36], los números pares son [4, 16, 36]

# -------------------------------------------------------------------

# Con Reduce, map y lambda
# Reduce sirve para aplicar una función acumulativa a los elementos de un iterable,
# reduciéndolos a un único valor. Es como un "acumulador" que procesa la lista paso a paso.
# Para usar reduce() se debe importar de functools:
from functools import reduce
# reduce(función_acumulativa, iterable[, valor_inicial])
# ---> función_acumulativa = una funcion que toma dos argumentos (acumulador y elemento actual) y devuelve un nuevo valor acumulado
# ---> iterable = Lista, tupla, etc., cuyos elementos serán transformados.
# ---> valor_inicial = (opcional) valor inicial del acumulador. Si no se especifica, se usa el primer elemento del iterable como valor inicial

suma_cuadrados_pares = reduce(lambda acumulador, x: acumulador + x, pares_cuadrados, 0)
print(f'La suma de los cuadrados de los numeros pares de {pares_cuadrados} es {suma_cuadrados_pares} ')

# -------------------------------------------------------------------

# Con sorted y lambda
# Sorted se ordena una lista de valores
# sorted(iterable, key=None, reverse=False)
# ---> key = Una función que toma un elemento del iterable y devuelve un valor que se usará para ordenar.
# ---> reverse: Si es True, la lista se ordena en orden descendente.

# Ordenar la lista 'numeros' basándose en el último dígito de cada número
orden_por_ultimo_digito = sorted(numeros, key=lambda x: x % 10)
print(f'La lista {numeros} ordenada por su último dígito: {orden_por_ultimo_digito}')

# Ordenar los cuadrados en orden descendente
cuadrados_ordenados = sorted(cuadrados, key=lambda x: x, reverse=True)
print(f'Cuadrados ordenados de mayor a menor: {cuadrados_ordenados}')

# -------------------------------------------------------------------

