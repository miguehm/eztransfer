import sqlite3

conexion = sqlite3.connect('test.db')

# Crear un cursor
cursor = conexion.cursor()

downloadToken = input("Inserte el downloadToken: ")
filename = input("Inserte el filename: ")
deleteToken = input("Inserte el deleteToken: ")
day = input("Inserte el day: ")
month = input("Inserte el month: ")
year = input("Inserte el year: ")
hour = input("Inserte el hour: ")
minute = input("Inserte el minute: ")
second = input("Inserte el second: ")

cursor.execute("INSERT INTO archives (downloadToken, filename, deleteToken, day, month, year, hour, minute, second) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (downloadToken, filename, deleteToken, day, month, year, hour, minute, second))

# Guardar los cambios
conexion.commit()

# Cerrar la conexión
conexion.close()
