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

# Ejecutar la sentencia select
cursor = personas_db.cursor()
cursor.execute('SELECT * FROM personas')
resultado = cursor.fetchall()

for persona in resultado:
    print(persona)

cursor.close()
personas_db.close()

