# Generador de un ID unico

import random
from random import randint
from random import choice

import string
from string import punctuation

print('*** Sistema de Generador de ID unico ***')

s_nombre = input('Ingrese su nombre: ')
s_nombre_codificado =  s_nombre[0:2].upper()

s_apellido = input('Ingrese su apellido: ')
s_apellido_codificado = s_apellido[0:2].lower()

n_anio = input('Ingrese los cuatro digitos de su año de nacimiento (YYYY): ')
n_anio_codificado = int(n_anio[3:]) + 1

# n_random = random.randint(1000, 9999)
n_random = randint(1000, 9999) # Solo randit porque se importo de random
s_random = str(n_random)[2:]

s_especiales = ''.join(random.choices(string.punctuation, k=2))

s_id_unico = s_nombre_codificado + str(n_anio_codificado) + s_apellido_codificado + s_especiales + s_random

print(f'''\nHola {s_nombre},
    tu nuevo ID unico es: 
    {s_id_unico} \n''')
