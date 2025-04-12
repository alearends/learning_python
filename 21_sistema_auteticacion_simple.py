# Sistema de Auteticación mas simple

print('*** Bienvenido a este Sistema ***')

while True:
    try:
        s_usuario = input('Indica tu nombre de usuario (mayor a 4 caracteres): ')
        if len(s_usuario) >= 4:
            break
        else:
            print('Por favor ingresa un nombre de usuario mayor a 8 caracteres')
    except ValueError:
        print('Por favor ingresa un nombre de usuario valido')

while True:
    try:
        s_password = input('Indica tu contraseña (debe ser mayor a 8 caracteres): ')
        if len(s_password) >= 8:
            break
        else:
            print('Por favor ingresa una contraseña mayor a 8 caracteres')
    except ValueError:
        print('Por favor ingresa una contraseña valida')

while True:
    try:
        s_password_confirm = input('Por favor confirma tu contraseña: ')
        if s_password == s_password_confirm:
            break
        else:
            print('Las contraseñas no coinciden. Por favor intenta de nuevo')
    except ValueError:
        print('Debes escribir los mismos caracteres y en el mismo orden de tu contraseña para validarla')

print(f' Bienvenido {s_usuario} al Sistema de verificar usuarios y contraseñas')

s_usuario_verificado = input('Por favor indica tu nombre de usuario: ')
s_password_verificado = input('Por favor indica tu contraseña: ')

if s_usuario == s_usuario_verificado and s_password == s_password_verificado:
    print(f' Bienvenido {s_usuario} tu usuario y contraseña han sido verificados')
elif s_usuario == s_usuario_verificado:
    print('contraseña erronea \n')
elif s_password != s_password_verificado:
    print('usuario erroneo \n')
else:
    print('usuario y contraseña erroneos \n')

