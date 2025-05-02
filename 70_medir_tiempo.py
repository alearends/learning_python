import functools
import time


print('*** Decoradores en Python ***')

def medir_tiempo(funcion):
    # Decorador que mide y muestra el tiempo de ejecución de una función.
    
    @functools.wraps(funcion)  # Preserva el nombre y la documentación de la función original
    def wrapper(*args, **kwargs):
        # Medir tiempo inicial
        tiempo_inicio = time.time()
        
        # Ejecutar la función original
        resultado = funcion(*args, **kwargs)
        
        # Medir tiempo final y calcular duración
        tiempo_fin = time.time()
        duracion = tiempo_fin - tiempo_inicio
        
        # Mostrar información sobre el tiempo de ejecución
        print(f"Función '{funcion.__name__}' ejecutada en {duracion:.4f} segundos")
        
        return resultado
    
    return wrapper

# -----------------------------------------------------

# Ejemplo práctico 1: Análisis de datos
@medir_tiempo
def procesar_datos(tamano):
    """Simula el procesamiento de una gran cantidad de datos."""
    print(f"Procesando {tamano} elementos...")
    # Simulamos trabajo con una pausa
    time.sleep(1)  # En un caso real, aquí estaría el procesamiento
    return f"{tamano} elementos procesados correctamente"

# -----------------------------------------------------

@medir_tiempo
def calcular_fibonacci(n):
    """Calcula el n-ésimo número de Fibonacci (implementación ineficiente a propósito)."""
    if n <= 1:
        return n
    else:
        return calcular_fibonacci(n-1) + calcular_fibonacci(n-2)

# -----------------------------------------------------

# Probar nuestras funciones decoradas
if __name__ == "__main__":
    # Probamos la función de procesamiento
    resultado = procesar_datos(1000)
    print(resultado)
    print("-" * 40)

 # Probamos el cálculo de Fibonacci
    n = 10
    resultado = calcular_fibonacci(n)
    print(f"Fibonacci({n}) = {resultado}")
