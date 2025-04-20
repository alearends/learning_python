# funciones recursivas
# Reglas:
# 1. Debe llamarse a si misma sin que sean ciclos infinitos
# 2. Debenos avanzar hacia un caso base 
def funcion_recursiva(n):
    # Caso base
    if n == 1:
        print(n, end=' ')
    else: # Caso recursiva
        # print(n, end=' ') # 5 4 3 2 1
        funcion_recursiva(n-1)
        print(n, end=' ') # 1 2 3 4 5


if __name__ == '__main__':
    funcion_recursiva(5)

