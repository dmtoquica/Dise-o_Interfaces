from equipos import equipos

def prestar_equipo():

    nombre = input("Nombre del equipo a prestar: ")

    for e in equipos:
        if e["nombre"] == nombre:

            if e["cantidad"] > 0:
                e["cantidad"] -= 1
                print("Préstamo realizado")
                return
            else:
                print("No hay equipos disponibles")
                return

    print("Equipo no encontrado")