from equipos import registrar_equipo, ver_equipos

def menu():

    while True:
        print("\n===== SISTEMA DE GESTIÓN DE EQUIPOS =====")
        print("1. Registrar equipo")
        print("2. Ver equipos")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_equipo()

        elif opcion == "2":
            ver_equipos()

        elif opcion == "3":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida")


menu()