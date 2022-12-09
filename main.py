import sqlite3
conn = sqlite3.connect('colegio.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE alumnos(id INT AUTO_INCREMENT, nombre TEXT, apellidos TEXT)")

def insertar_alumno(nombre, apellidos):
    cursor.execute(f"INSERT INTO Alumnos(nombre, apellidos) VALUES('{nombre}', '{apellidos}')")
    conn.commit()


print('1-.VER ALUMNOS')
print('2-.INSERTAR ALUMNO')
opcion = input('Seleccione una opción: ')

match opcion:
    case 1:
        query = cursor.execute('SELECT * FROM alumnos')
        filas = cursor.fetchall(query)
        print(filas)
    case 2:
        nombre = input('Introduzca nombre')
        apellido = input('introduzca apellido')
        insertar_alumno(nombre, apellido)
    case other:
        print('Seleccione una opción correcta')

conn.close()