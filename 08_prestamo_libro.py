# Sistema Prestamos de Libros

s_con_credencial = input('¿Tienes credencial? (S/N): ').upper()
n_distancia_biblioteca = int(input('¿A cuántos km está la biblioteca de tu casa? '))
DISTANCIA_MINIMA_KM = 3

es_eligible_para_prestamo = s_con_credencial == 'S' or n_distancia_biblioteca <= DISTANCIA_MINIMA_KM

if es_eligible_para_prestamo:
    print(f'Si eres elegible para el prestamo de libros.')
else: 
    print(f'No eres elegible para el prestamo de libros.')
    