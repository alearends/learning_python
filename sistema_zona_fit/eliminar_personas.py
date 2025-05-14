import mysql.connector
from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()

# Obtener variables de entorno
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_DATABASE")

personas_db = mysql.connector.connect(
    host=db_host,
    port=3306,
    user=db_user,
    password=db_password,
    database=db_name
)

# ejecutar la sentencia delete
cursor = personas_db.cursor()

ids_a_eliminar = (13,14,15,16) # Si es una sola fila debes colocar una coma detras del numero, si son varias filas debes separar cada numero con comas
formato_sql = ', '.join(['%s'] * len(ids_a_eliminar))
sentencia_sql = f'DELETE FROM personas WHERE id IN ({formato_sql})'
cursor.execute(sentencia_sql, ids_a_eliminar)

# sentencia_sql = 'DELETE FROM personas WHERE id=%s' # Para eliminar una fila
# valores = (5,) # Aqui se elimina la fila 5
# cursor.execute(sentencia_sql, valores) # Para eliminar una fila

personas_db.commit()
print(f'Se han eliminado {cursor.rowcount} registros\n')

cursor.close()
personas_db.close()

