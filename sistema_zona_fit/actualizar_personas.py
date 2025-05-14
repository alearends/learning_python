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

# ejecutar la sentencia update
cursor = personas_db.cursor()
sentencia_sql = 'UPDATE personas SET nombre=%s, apellido=%s, edad=%s WHERE id=%s'
valores = ('Victoria', 'Flores', 45, 5)
cursor.execute(sentencia_sql, valores)
personas_db.commit()
print('Se ha modificado la informacion...')
cursor.close()
personas_db.close()


