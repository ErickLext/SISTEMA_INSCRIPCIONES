# Módulo: manejo_archivos.py
# Propósito: Gestionar la lectura y escritura de datos en el sistema de archivos.

NOMBRE_ARCHIVO = "inscripciones_charlas.txt"

def guardar_registro(nombre, correo, charla):
    """Escribe una nueva inscripción en el archivo de texto."""
    try:
        # 'a' (append) para agregar datos sin borrar los anteriores
        with open(NOMBRE_ARCHIVO, "a", encoding="utf-8") as archivo:
            archivo.write(f"Nombre: {nombre} | Correo: {correo} | Charla: {charla}\n")
    except IOError:
        print("Error: No se pudo escribir en el archivo de registros.")

def leer_registros():
    """Lee y retorna el contenido del archivo de inscripciones."""
    try:
        with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            return contenido if contenido else "No hay inscripciones registradas."
    except FileNotFoundError:
        return "El archivo de registros aún no existe (no hay inscripciones)."
    except Exception as e:
        return f"Error inesperado al leer el archivo: {e}"
