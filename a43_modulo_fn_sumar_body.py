# La función esta ubicada en el archivo a43_modulo_fn_sumar_head.py
# pero solo se debe ejecutar el archivo a43_modulo_fn_sumar_body.py (este archivo)

from a43_modulo_fn_sumar_head import sumar

# arg1, arg2 = 1, 2
arg1 = float(input('dame un numero: '))
arg2 = float(input('dame otro numero: '))

resultado = sumar(arg1, arg2)

print(resultado)  