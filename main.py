import sqlite3
conn = sqlite3.connect('colegio.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS alumnos(nombre TEXT, apellidos TEXT)")

def insertar_alumno(nombre, apellidos):
    
        cursor.execute(f"INSERT INTO Alumnos(nombre, apellidos) VALUES('{nombre}', '{apellidos}')")
        conn.commit()
        

def menu():
    print('1-.VER ALUMNOS')
    print('2-.INSERTAR ALUMNO')
    opcion = int(input('Seleccione una opción: '))
    match opcion:
        case 1:
            query = cursor.execute('SELECT rowid, nombre, apellidos FROM alumnos')
            filas = cursor.fetchall()
            print(filas)
            menu()
        case 2:
            seguir= ''
            while seguir != 'no':
                nombre = input('Introduzca nombre: ')
                apellido = input('introduzca apellido: ')
                insertar_alumno(nombre, apellido)
                seguir = input('¿Desea introducir otro (si/no)? ')
            else:
                menu()
        case other:
            print('Seleccione una opción correcta')

menu()


conn.close()