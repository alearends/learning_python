# Aplicar Logica inversa con if not. Asumir que estamos dentro de un sistema bancario
# Solicitar al usuario si desea continuar dentro del sistema
# Si NO deseamos salir imprimir: continuar dentro del sistema
# De lo contrario imprimir: Saliendo del sistema 

print('*** Bienvenidos al Sistema Bancario ***')

s_salir_sistema = input('Deseas continuar en el sistema? (S/N): ').upper()

if not s_salir_sistema == 'N':
    print('Continuando dentro del sistema')
else:
    print('Saliendo del sistema')