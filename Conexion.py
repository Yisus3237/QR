import mysql.connector  # Suponiendo que estás usando MySQL como ejemplo

def conectar_bd():
    try:
        # Configura los parámetros de conexión a tu base de datos
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="operacion7",
            database="qr_estudiantes"
        )
        return conexion
    except mysql.connector.Error as error:
        print("Error al conectar a la base de datos:", error)
        return None

def cerrar_bd(conexion):
    if conexion:
        conexion.close()
