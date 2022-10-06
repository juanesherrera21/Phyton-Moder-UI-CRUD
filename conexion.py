# Importa el módulo sqlite3
import sqlite3

# Crea un objeto de conexión a la base de datos SQLite
con = sqlite3.connect("Base_datos.db")

# Con la conexión, crea un objeto cursor
cur = con.cursor()

# El resultado de "cursor.execute" puede ser iterado por fila
for row in cur.execute('SELECT * FROM Tabla_Usuarios;'):
    print(row)

# No olvidar de cerrar la conexión
con.close()