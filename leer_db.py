import sqlite3

def read_by_file():
    
    filename = input("Ingrese el nombre del archivo: ")

    conexion = sqlite3.connect('test.db')

    cursor = conexion.cursor()

    cursor.execute(f'SELECT * FROM archives WHERE filename LIKE ?', ('%'+filename+'%', ))

# registro = cursor.fetchone()
    resultados = cursor.fetchall()

    print(f"\n= Mostrando resultados para la búsqueda \"{filename}\" \n")
    if resultados is not None:
        for registro in resultados:
            print(f"Filename: {registro[0]}")
            print(f"Download link: https://transfer.sh/{registro[1]}/{registro[0]}")
            print(f"Delete token: {registro[2]}")
            print(f"Upload date: {registro[3]}/{registro[4]}/{registro[5]} - {registro[6]}:{registro[7]}:{registro[8]}")
            print(f"Max days: {registro[9]}")
            print("-------------------------")
    else:
        print("No se encontró registro")

    conexion.close()

def show_files():
    conexion = sqlite3.connect('test.db')

    cursor = conexion.cursor()

    cursor.execute('SELECT * FROM archives')

    resultados = cursor.fetchall()

    # TODO: show as tables
    if resultados is not None:
        for registro in resultados:
            print(f"Filename: {registro[0]}")
            print(f"Download link: https://transfer.sh/{registro[1]}/{registro[0]}")
            print(f"Delete token: {registro[2]}")
            print(f"Upload date: {registro[3]}/{registro[4]}/{registro[5]} - {registro[6]}:{registro[7]}:{registro[8]}")
            print(f"Max days: {registro[9]}")
            print("-------------------------")

    conexion.close()

if __name__ == "__main__":
    read_by_file()
    # show_files()
