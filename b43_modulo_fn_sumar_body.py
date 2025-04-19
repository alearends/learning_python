# La función esta ubicada en el archivo a43_modulo_fn_sumar_head.py
# pero solo se debe ejecutar el archivo b43_modulo_fn_sumar_body.py (este archivo)

import a43_modulo_fn_sumar_head

# arg1, arg2 = 1, 2
arg1 = float(input('dame un numero: '))
arg2 = float(input('dame otro numero: '))

resultado = a43_modulo_fn_sumar_head.sumar(arg1, arg2)

print(resultado)  