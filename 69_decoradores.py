print('*** Decoradores en Python ***')

def decorador(funcion):
    def wrapper(*args, **kwargs):
        print('Antes de llamar la función saludar')
        resultado = funcion(*args, **kwargs)  # llamamos a nuestra funcion
        print('Despues de llamar la funcion saludar')
        return resultado
    return wrapper


@decorador
def saludar(nombre):
    print(f'    Hola {nombre}')

saludar('Carlos')

'''
A. Pregunta: 
Teniendo en cuenta que en la siguiente funcion "resultado" es un nombre generico 
(que pudiera sustituirse por "patata") y que la funcion saludar(nombre) no tiene ningun 
return asociado sino en un print ¿por que se guarda el "Hola Carlos" ??

Respuesta:
Estás en lo correcto al identificar que hay algo interesante ocurriendo con la variable resultado.

En la función saludar(nombre), efectivamente no hay un return explícito. Cuando una función en Python 
no tiene un return definido, implícitamente retorna None. Por lo tanto:

1. Cuando se ejecuta resultado = funcion(*args, **kwargs) dentro del wrapper
2. Se llama a saludar('Carlos') que imprime "Hola Carlos"
3. Como saludar no retorna nada explícitamente, resultado recibe el valor None

La variable resultado podría llamarse de cualquier manera (como mencionas, "patata" funcionaría igual). 
Es simplemente una variable que captura el valor retornado por la función decorada.

El return resultado al final del wrapper está devolviendo ese valor None, lo que permite mantener el 
comportamiento original de la función decorada.

En resumen, no se está "guardando" el string "Hola Carlos" en resultado - ese texto se imprime directamente. 
Lo que se guarda en resultado es None, que es el valor implícito que retorna la función saludar.

-----------------------------
B. Pregunta:
entonces en "resultado = funcion(*args, **kwargs) " lo que ocurre es que se ejecuta la funcion? solo eso?

Resultado:
Exactamente. En la línea resultado = funcion(*args, **kwargs) lo que ocurre es:
1. Se ejecuta la función decorada (en este caso saludar)
2. La función se ejecuta con los argumentos que se le pasaron (*args y **kwargs)
3. Cualquier cosa que la función haga (en este caso, imprimir "Hola Carlos") ocurre en ese momento
4. El valor de retorno de la función (en este caso None, ya que saludar no tiene un return explícito) se asigna a la variable resultado

Es importante entender que no se está "guardando" la salida impresa en resultado. Lo que se imprime va directamente a la consola durante 
la ejecución. La variable resultado solo almacena lo que la función retorna, que en este caso es None.

La asignación a resultado es simplemente una forma de capturar el valor de retorno para poder devolverlo más tarde con return resultado, 
manteniendo así la transparencia del decorador (es decir, que la función decorada se comporte igual que la original en términos de lo 
que retorna).

Lo que hace poderosos a los decoradores es esta capacidad de ejecutar código antes y después de la función decorada, mientras preservan 
su comportamiento original.

'''