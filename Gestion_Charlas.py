# Módulo: gestion_charlas.py
# Propósito: Lógica de negocio, validación de cupos y validación recursiva.

import Manejo_Archivos

# Diccionario de datos: Charlas y sus cupos iniciales
charlas = {
    "Marketing": 5,
    "Finanzas": 2,
    "Liderazgo": 10,
    "Superación": 8,
    "Redes Sociales": 1
}

def validar_entrada_recursiva(mensaje):
    """
    Criterio: Uso de recursividad en la validación de entrada.
    Asegura que el usuario no ingrese valores vacíos.
    """
    valor = input(mensaje).strip()
    if valor == "":
        print("⚠ Error: Este campo no puede quedar vacío. Inténtelo de nuevo.")
        return validar_entrada_recursiva(mensaje)  # Llamada recursiva
    return valor

def mostrar_disponibilidad():
    """Muestra las charlas y sus cupos actuales."""
    print("\n--- Listado de Charlas y Disponibilidad ---")
    lista_claves = list(charlas.keys())
    for i, nombre in enumerate(lista_claves, 1):
        cupo = charlas[nombre]
        estado = f"{cupo} cupos" if cupo > 0 else "SIN CUPOS"
        print(f"{i}. {nombre} ({estado})")
    return lista_claves

def inscribir_participante():
    """
    Criterio: Gestión de inscripciones y validación de cupos.
    """
    nombre = validar_entrada_recursiva("Ingrese su nombre: ")
    correo = validar_entrada_recursiva("Ingrese su correo: ")
    
    charlas_nombres = mostrar_disponibilidad()
    
    try:
        seleccion = int(input("\nSeleccione el número de la charla: "))
        
        # Validar si la opción existe en la lista
        if 1 <= seleccion <= len(charlas_nombres):
            nombre_charla = charlas_nombres[seleccion - 1]
            
            # Validación de cupos (Criterio 2)
            if charlas[nombre_charla] > 0:
                # Actualizar cupo
                charlas[nombre_charla] -= 1
                # Guardar en archivo
                manejo_archivos.guardar_registro(nombre, correo, nombre_charla)
                print(f"✅ ¡Confirmado! Inscrito en: {nombre_charla}")
            else:
                print(f"❌ Error: Ya no quedan cupos disponibles para {nombre_charla}.")
        else:
            print("⚠ Opción inválida. Seleccione un número de la lista.")
            
    except ValueError:
        print("⚠ Error de entrada: Debe ingresar un número entero.")

def ver_consultas():
    print("\n--- Historial de Inscritos ---")

    print(Manejo_Archivos.leer_registros())
