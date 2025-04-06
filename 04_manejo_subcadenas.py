# Manejo de subcadenas
# Slice de cadenas
s_cadena = 'Hola, Mundo!'

s_subcadena1 = s_cadena[0:4]  # 'Hola'
s_subcadena2 = s_cadena[6:11] # 'Mundo'

print(s_subcadena1)  # Output: 'Hola'
print(s_subcadena2)  # Output: 'Mundo'
print(s_cadena[0:4])  # Output: 'Hola'  
print(s_cadena[6:11]) # Output: 'Mundo'
print(s_cadena[0:])    # Output: 'Hola, Mundo!' 
print(s_cadena[:])     # Output: 'Hola, Mundo!'
