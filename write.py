import sqlite3

def write_db(data: dict):
    conexion = sqlite3.connect('test.db')

    # Crear un cursor
    cursor = conexion.cursor()

    cursor.execute('create table if not exists archives(filename text, downloadToken text, deleteToken text, day integer, month integer, year integer, hour integer, minute integer, second integer, maxDays integer);')
    
    querie = "INSERT INTO archives (filename, downloadToken, deleteToken, day, month, year, hour, minute, second, maxDays) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    
    args = (data['filename'],
            data['download_token'],
            data['delete_token'],
            data['day'],
            data['month'],
            data['year'],
            data['hour'],
            data['minute'],
            data['second'],
            data['max-days'])

    cursor.execute(querie, args)

    # Guardar los cambios
    conexion.commit()

    # Cerrar la conexión
    conexion.close()

def main():
    # write_db({'filename': 'README.md', 'upload_token': 'C8dfGGdFn1', 'delete_token':'MREvjjEn5EkMfAHHQz2u', 'day': '04', 'month': '12', 'year': '2023', 'hour': '17', 'minute': '56', 'second': '27'})
    pass

if __name__ == "__main__":
    main()
