import os

ARCHIVO_PUNTAJES = "mejores_puntajes.txt"

def cargar_puntajes():
    puntajes = []
    if os.path.exists(ARCHIVO_PUNTAJES):
        with open(ARCHIVO_PUNTAJES, "r") as archivo:
            for linea in archivo:
                nombre, puntos = linea.strip().split(",")
                puntajes.append((nombre, int(puntos)))
    return sorted(puntajes, key=lambda x: x[1], reverse=True)

def guardar_puntaje(nombre, puntaje):
    puntajes = cargar_puntajes()
    puntajes.append((nombre, puntaje))
    puntajes = sorted(puntajes, key=lambda x: x[1], reverse=True)[:10]  # guarda top 10

    with open(ARCHIVO_PUNTAJES, "w") as archivo:
        for nombre, puntos in puntajes:
            archivo.write(f"{nombre},{puntos}\n")

def mostrar_puntajes():
    puntajes = cargar_puntajes()
    print("\n--- MEJORES PUNTAJES ---")
    if not puntajes:
        print("Aún no hay puntajes registrados.")
    else:
        for i, (nombre, puntos) in enumerate(puntajes, start=1):
            print(f"{i}. {nombre}: {puntos} puntos")
    print()

