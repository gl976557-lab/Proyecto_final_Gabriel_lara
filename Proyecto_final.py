# ==========================================
#        CINEMAX - RESERVAS DE CINE
# ==========================================

# -------------------------------
# DATOS DE LA CARTELERA
# -------------------------------

cartelera = {
    "lunes": [
        {"pelicula": "Avengers", "sala": 1, "horario": "3:00 PM", "formato": "Normal"},
        {"pelicula": "Avatar", "sala": 2, "horario": "4:00 PM", "formato": "3D"},
        {"pelicula": "Batman", "sala": 3, "horario": "5:00 PM", "formato": "Normal"},
        {"pelicula": "Superman", "sala": 4, "horario": "6:00 PM", "formato": "4DX"},
        {"pelicula": "Spider-Man", "sala": 5, "horario": "7:00 PM", "formato": "CXC"}
    ],

    "martes": [
        {"pelicula": "Avengers", "sala": 1, "horario": "3:00 PM", "formato": "Normal"},
        {"pelicula": "Avatar", "sala": 2, "horario": "4:00 PM", "formato": "3D"},
        {"pelicula": "Batman", "sala": 3, "horario": "5:00 PM", "formato": "Normal"},
        {"pelicula": "Superman", "sala": 4, "horario": "6:00 PM", "formato": "4DX"},
        {"pelicula": "Spider-Man", "sala": 5, "horario": "7:00 PM", "formato": "CXC"}
    ],

    "miércoles": [
        {"pelicula": "Avengers", "sala": 1, "horario": "3:00 PM", "formato": "Normal"},
        {"pelicula": "Avatar", "sala": 2, "horario": "4:00 PM", "formato": "3D"},
        {"pelicula": "Batman", "sala": 3, "horario": "5:00 PM", "formato": "Normal"},
        {"pelicula": "Superman", "sala": 4, "horario": "6:00 PM", "formato": "4DX"},
        {"pelicula": "Spider-Man", "sala": 5, "horario": "7:00 PM", "formato": "CXC"}
    ],

    "jueves": [
        {"pelicula": "Avengers", "sala": 1, "horario": "3:00 PM", "formato": "Normal"},
        {"pelicula": "Avatar", "sala": 2, "horario": "4:00 PM", "formato": "3D"},
        {"pelicula": "Batman", "sala": 3, "horario": "5:00 PM", "formato": "Normal"},
        {"pelicula": "Superman", "sala": 4, "horario": "6:00 PM", "formato": "4DX"},
        {"pelicula": "Spider-Man", "sala": 5, "horario": "7:00 PM", "formato": "CXC"}
    ],

    "viernes": [
        {"pelicula": "Avengers", "sala": 1, "horario": "3:00 PM", "formato": "Normal"},
        {"pelicula": "Avatar", "sala": 2, "horario": "4:00 PM", "formato": "3D"},
        {"pelicula": "Batman", "sala": 3, "horario": "5:00 PM", "formato": "Normal"},
        {"pelicula": "Superman", "sala": 4, "horario": "6:00 PM", "formato": "4DX"},
        {"pelicula": "Spider-Man", "sala": 5, "horario": "7:00 PM", "formato": "CXC"}
    ],

    "sábado": [
        {"pelicula": "Avengers", "sala": 1, "horario": "3:00 PM", "formato": "Normal"},
        {"pelicula": "Avatar", "sala": 2, "horario": "4:00 PM", "formato": "3D"},
        {"pelicula": "Batman", "sala": 3, "horario": "5:00 PM", "formato": "Normal"},
        {"pelicula": "Superman", "sala": 4, "horario": "6:00 PM", "formato": "4DX"},
        {"pelicula": "Spider-Man", "sala": 5, "horario": "7:00 PM", "formato": "CXC"}
    ],

    "domingo": [
        {"pelicula": "Avengers", "sala": 1, "horario": "3:00 PM", "formato": "Normal"},
        {"pelicula": "Avatar", "sala": 2, "horario": "4:00 PM", "formato": "3D"},
        {"pelicula": "Batman", "sala": 3, "horario": "5:00 PM", "formato": "Normal"},
        {"pelicula": "Superman", "sala": 4, "horario": "6:00 PM", "formato": "4DX"},
        {"pelicula": "Spider-Man", "sala": 5, "horario": "7:00 PM", "formato": "CXC"}
    ]
}


# -------------------------------
# ASIENTOS
# -------------------------------

asientos = {}

for dia in cartelera:

    asientos[dia] = {}

    for funcion in cartelera[dia]:

        sala = funcion["sala"]
        horario = funcion["horario"]

        asientos[dia][sala] = {}

        matriz = []

        for fila in range(5):
            fila_asientos = []

            for columna in range(6):
                fila_asientos.append(".")

            matriz.append(fila_asientos)

        asientos[dia][sala][horario] = matriz


# -------------------------------
# FUNCIÓN: MOSTRAR CARTELERA
# -------------------------------

def mostrar_cartelera():

    dia = input("Escriba el día: ").lower()

    if dia not in cartelera:
        print("Ese día no existe.")
        return

    print("\n===== CARTELERA =====")

    for funcion in cartelera[dia]:

        print("----------------------")
        print("Película:", funcion["pelicula"])
        print("Sala:", funcion["sala"])
        print("Horario:", funcion["horario"])
        print("Formato:", funcion["formato"])


# -------------------------------
# FUNCIÓN: BUSCAR FUNCIÓN
# -------------------------------

def buscar_funcion():

    dia = input("Día: ").lower()
    sala = int(input("Sala: "))
    horario = input("Horario: ")

    if dia not in cartelera:
        print("El día no existe.")
        return None

    if sala not in asientos[dia]:
        print("La sala no existe para ese día.")
        return None

    if horario not in asientos[dia][sala]:
        print("Ese horario no existe.")
        return None

    return dia, sala, horario


# -------------------------------
# FUNCIÓN: MOSTRAR ASIENTOS
# -------------------------------

def mostrar_asientos():

    datos = buscar_funcion()

    if datos is None:
        return

    dia, sala, horario = datos

    matriz = asientos[dia][sala][horario]

    print("\n      1 2 3 4 5 6")

    letras = ["A", "B", "C", "D", "E"]

    for i in range(5):

        print(letras[i], end="     ")

        for asiento in matriz[i]:
            print(asiento, end=" ")

        print()


# -------------------------------
# FUNCIÓN: RESERVAR
# -------------------------------

def reservar():

    datos = buscar_funcion()

    if datos is None:
        return

    dia, sala, horario = datos

    asiento = input("Asiento (ejemplo A3): ").upper()

    letras = ["A", "B", "C", "D", "E"]

    if len(asiento) != 2:
        print("Asiento inválido.")
        return

    fila = asiento[0]

    try:
        columna = int(asiento[1])
    except:
        print("Asiento inválido.")
        return

    if fila not in letras or columna < 1 or columna > 6:
        print("Ese asiento no existe.")
        return

    numero_fila = letras.index(fila)

    if asientos[dia][sala][horario][numero_fila][columna - 1] == "X":
        print("Ese asiento ya está ocupado.")
        return

    asientos[dia][sala][horario][numero_fila][columna - 1] = "X"

    print("Reserva realizada correctamente.")


# -------------------------------
# FUNCIÓN: CANCELAR
# -------------------------------

def cancelar():

    datos = buscar_funcion()

    if datos is None:
        return

    dia, sala, horario = datos

    asiento = input("Asiento que desea cancelar: ").upper()

    letras = ["A", "B", "C", "D", "E"]

    if len(asiento) != 2:
        print("Asiento inválido.")
        return

    fila = asiento[0]

    try:
        columna = int(asiento[1])
    except:
        print("Asiento inválido.")
        return

    if fila not in letras or columna < 1 or columna > 6:
        print("Ese asiento no existe.")
        return

    numero_fila = letras.index(fila)

    if asientos[dia][sala][horario][numero_fila][columna - 1] == ".":
        print("Ese asiento está libre.")
        return

    asientos[dia][sala][horario][numero_fila][columna - 1] = "."

    print("Reserva cancelada correctamente.")


# -------------------------------
# FUNCIÓN: DISPONIBILIDAD
# -------------------------------

def disponibilidad():

    dia = input("Escriba el día: ").lower()

    if dia not in cartelera:
        print("Ese día no existe.")
        return

    print("\n===== DISPONIBILIDAD =====")

    for funcion in cartelera[dia]:

        sala = funcion["sala"]
        horario = funcion["horario"]

        matriz = asientos[dia][sala][horario]

        libres = 0
        ocupados = 0

        for fila in matriz:

            for asiento in fila:

                if asiento == ".":
                    libres += 1
                else:
                    ocupados += 1

        print("----------------------")
        print("Película:", funcion["pelicula"])
        print("Sala:", sala)
        print("Horario:", horario)
        print("Asientos libres:", libres)
        print("Asientos ocupados:", ocupados)


# -------------------------------
# MENÚ PRINCIPAL
# -------------------------------

opcion = 0

while opcion != 6:

    print("\n================================")
    print("       CINEMAX")
    print("   SISTEMA DE RESERVAS")
    print("================================")

    print("1. Ver cartelera de un día")
    print("2. Mostrar asientos de una función")
    print("3. Reservar asiento")
    print("4. Cancelar reserva")
    print("5. Ver disponibilidad")
    print("6. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:

        mostrar_cartelera()

    elif opcion == 2:

        mostrar_asientos()

    elif opcion == 3:

        reservar()

    elif opcion == 4:

        cancelar()

    elif opcion == 5:

        disponibilidad()

    elif opcion == 6:

        print("Gracias por utilizar CineMax.")

    else:

        print("Opción inválida.")


print("Programa finalizado.")