# 1. SPLICE (rebanado de cadenas) → Cadena[inicio:fin:paso]
#    - Extrae subcadenas como si cortaras un pastel.
#    - Ej: "Batman"[1:4] → "atm"

# 2. REPLACE() → Cadena.replace(viejo, nuevo[, conteo])
#    - Reemplaza texto como un disfraz de identidad.
#    - Ej: "Joker".replace("J", "L") → "Loker"

# 3. FIND() → Cadena.find(subcadena[, inicio[, fin]])
#    - Busca la posición de un villano (subcadena).
#    - Devuelve -1 si no lo encuentra.
#    - Ej: "Gotham".find("ham") → 3

# 4. STRIP() → Cadena.strip([caracteres])
#    - Elimina espacios (o caracteres) de los bordes, como recortar capa.
#    - Ej: "  Batman  ".strip() → "Batman"

# 5. MULTIPLICAR CADENA → Cadena * entero
#    - Repite texto como un ejército de clones.
#    - Ej: "Boom!" * 3 → "Boom!Boom!Boom!"

# -------------------------------------------------------------------------------

# Ejemplo Práctico: ¡Código Secreto de la Liga de la Justicia!
mensaje_cifrado = "  xBxaxtxsxixgxnxaxlx:x xLxexx xLxuxtxhxoxrx xaxxtxaxcxax xMxexxtxrxxóxpxoxlxixsx xcxoxnx xkxrxixpxtxoxnxixxtxaxx  "
mensaje_limpio = mensaje_cifrado.strip() 
mensaje_descifrado = mensaje_limpio.replace("x", "")  
posicion_amenaza = mensaje_descifrado.find("kriptonita")  
ubicacion = mensaje_descifrado[23:34]  # "Metrópolis"
alerta = "¡CÓDIGO ROJO! " * 2 + "🚨"  
# --- Mostramos el informe de la misión ---
print("\n=== 🔓 MENSAJE DESCIFRADO (LIGA DE LA JUSTICIA) 🔓 ===")  
print("Alerta:", alerta)  
print("Mensaje descifrado:", mensaje_descifrado)  
print(f"Ubicación del ataque: {ubicacion}")  
print(f"Amenaza detectada en posición: {posicion_amenaza} ('kriptonita')")  
print("¡Superman necesita backup! " * 2)  