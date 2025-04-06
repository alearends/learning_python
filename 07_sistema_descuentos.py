# Sistema Descuentos VIP

MIN_PRODUCTOS_DESCUENTO = 10

n_cantidad_productos = int(input('Cuántos productos compraste hoy?'))
s_miembro = input('Eres miembro VIP? (Si/No): ').lower()

is_elegible_discount = n_cantidad_productos >= MIN_PRODUCTOS_DESCUENTO and s_miembro == 'si'

print(f'is_elegible_discount: {is_elegible_discount}')
