import sqlite3
import sys
from subir import upload_archives

def write_db(*args):
    conexion = sqlite3.connect('test.db')

    # Crear un cursor
    cursor = conexion.cursor()

    for querie in args:
        cursor.execute("INSERT INTO archives (downloadToken, filename, deleteToken, day, month, year, hour, minute, second) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", querie)

    # Guardar los cambios
    conexion.commit()

    # Cerrar la conexión
    conexion.close()

if __name__ == "__main__":
    queries = upload_archives(*sys.argv[1:])
    write_db(*queries)
