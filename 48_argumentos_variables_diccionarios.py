# arga - argumentos - tupla
# kwargs - keyword argumentos (key, value), dict

print('*** Argumentos variables por Keywords ***')

def superheroe_superpoderes(nombre, *args, **kwargs):
    print(f'Superheroe: {nombre} - {args}. Mas info: {kwargs}')

superheroe_superpoderes('Spiderman', 'instinto aracnido', 'telaraña', 'se pega a superficies', edad=17, empresa='Marvel' )
superheroe_superpoderes('Superman','super fuerza', 'volar', edad=21, empresa='DC')
superheroe_superpoderes('Papa', edad=71) # Es opcional enviar argumentos variables
superheroe_superpoderes('Yo') # Es opcional enviar args y Kwargs