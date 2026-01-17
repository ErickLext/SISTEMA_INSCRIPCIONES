# Módulo: main.py
# Estudiante: [Tu Nombre]
# Propósito: Interfaz de usuario y control principal del sistema.

import Gestion_Charlas

def ejecutar_sistema():
    """Criterio: Implementación del menú interactivo."""
    while True:
        print("\n" + "="*40)
        print("   SISTEMA DE GESTIÓN DE CHARLAS   ")
        print("="*40)
        print("1. Inscribirse en una charla")
        print("2. Consultar inscripciones")
        print("3. Salir")
        
        try:
            opcion = input("\nSeleccione una opción (1-3): ")
            
            if opcion == "1":
                Gestion_Charlas.inscribir_participante()
            elif opcion == "2":
                Gestion_Charlas.ver_consultas()
            elif opcion == "3":
                print("Gracias por usar el sistema. Cerrando sesión...")
                break
            else:
                print("⚠ Opción no válida. Intente con 1, 2 o 3.")
        
        except Exception as e:
            # Criterio: Manejo de excepciones (try-except)
            print(f"Ha ocurrido un error inesperado en el sistema: {e}")

if __name__ == "__main__":

    ejecutar_sistema()
