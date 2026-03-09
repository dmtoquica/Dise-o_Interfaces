equipos = []

def registrar_equipo():

    nombre = input("Nombre del equipo: ")
    categoria = input("Categoría: ")

    try:
        cantidad = int(input("Cantidad disponible: "))
    except ValueError:
        print("Error: debe ingresar un número")
        return

    equipo = {
        "nombre": nombre,
        "categoria": categoria,
        "cantidad": cantidad
    }

    equipos.append(equipo)

    print("Equipo registrado correctamente")


def ver_equipos():

    if len(equipos) == 0:
        print("No hay equipos registrados")
        return

    print("\nLista de equipos:")

    for e in equipos:
        print(
            "Nombre:", e["nombre"],
            "| Categoría:", e["categoria"],
            "| Cantidad:", e["cantidad"]
        )