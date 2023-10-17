import sqlite3

filename = input("Ingrese el nombre del archivo: ")

conexion = sqlite3.connect('test.db')

cursor = conexion.cursor()

cursor.execute(f'SELECT * FROM archives WHERE filename LIKE ?', ('%'+filename+'%', ))

# registro = cursor.fetchone()
resultados = cursor.fetchall()

print("-------------------------")
if resultados is not None:
    for registro in resultados:
        print(f"Filename: {registro[1]}")
        print(f"Download link: https://transfer.sh/{registro[0]}/{registro[1]}")
        print(f"Delete token: {registro[2]}")
        print(f"Upload date: {registro[3]}/{registro[4]}/{registro[5]} - {registro[6]}:{registro[7]}:{registro[8]}")
        print("-------------------------")
else:
    print("No se encontró registro")

conexion.close()
