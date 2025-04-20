# imprimir informacion de kwargs

print('*** imprimir informacion de kwargs ***')

def imprimir_info_kwargs(**kwargs):
    print('\nvalores recibidos: ')
    for key, value in kwargs.items():
        print(f'{key}:{value}')


imprimir_info_kwargs(nombre=' ', edad=0)
imprimir_info_kwargs(nombre=' Karla', edad=30, ciudad=' Mexico')