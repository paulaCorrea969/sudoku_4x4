from game import jugar_sudoku
from scores import mostrar_puntajes, guardar_puntaje

def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Jugar Sudoku")
    print("2. Mostrar puntajes")
    print("3. Salir")

def elegir_visualizacion():
    print("\n--- TIPOS DE VISUALIZACIÓN ---")
    print("1. Números (1-4)")
    print("2. Letras (A-D)")
    print("3. Símbolos (♦ ♣ ♥ ♠)")
    opcion = input("Selecciona una opción (1-3): ")
    return opcion

def elegir_dificultad():
    print("\n--- NIVELES DE DIFICULTAD ---")
    print("1. Fácil (6 casillas vacías)")
    print("2. Difícil (10 casillas vacías)")
    opcion = input("Selecciona una opción (1-2): ")
    return opcion

def main():
    puntaje_actual = 0
    juegos_continuos = 0

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            visualizacion = elegir_visualizacion()
            dificultad = elegir_dificultad()

            exito = jugar_sudoku(visualizacion, dificultad)
            
            if exito:
                puntos_extra = 2 ** juegos_continuos if juegos_continuos else 0
                puntaje_actual += 10 + puntos_extra
                juegos_continuos += 1
                print(f"¡Bien hecho! Puntaje actual: {puntaje_actual}")
            else:
                print("Juego perdido. Puntaje reiniciado.")
                puntaje_actual = 0
                juegos_continuos = 0

        elif opcion == "2":
            mostrar_puntajes()

        elif opcion == "3":
            # Pide el nombre del jugador antes de guardar el puntaje
            nombre_jugador = input("Ingresa tu nombre: ")
            guardar_puntaje(nombre_jugador, puntaje_actual)
            print(f"Nuevo puntaje guardado para {nombre_jugador}!")
            print("Gracias por jugar.")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    main()

