# Generador de emails

print('*** Sistema de Generador de Emails ***')

s_nombre = input('Ingrese su nombre: ')
s_apellido = input('Ingrese su apellido: ')
s_empresa = input('Ingrese el nombre de la empresa: ')

# s_nombre_email = s_nombre.lower()
# s_apellido_email = s_apellido.lower()

s_email_generado = f'{s_nombre.lower()}.{s_apellido.lower()}@{s_empresa.lower()}.com'

print(f'''
Hola {s_nombre},
    tu nuevo email es: 
    {s_email_generado} \n''')