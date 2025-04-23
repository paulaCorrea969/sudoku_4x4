from puzzles import obtener_tablero
from utils import mostrar_tablero, validar_tablero, tablero_completo
from scores import guardar_puntaje
import time

def jugar_sudoku(puntaje, rondas_ganadas):
    print("\n--- BIENVENIDO AL SUDOKU 4x4 ---")
    
    try:
        puntaje = int(puntaje)
    except ValueError:
        print("El puntaje debe ser un número entero. Usando 0 como valor por defecto.")
        puntaje = 0
        
    # Elegir tipo de visualización
    print("\nSelecciona tipo de visualización:")
    print("1. Numérico (1-4)")
    print("2. Letras (A-D)")
    print("3. Símbolos (♦, ♣, ♥, ♠)")
    opcion_visual = input("Opción (1-3): ")

    if opcion_visual == "1":
        tipo_visualizacion = "numeros"
        valores_validos = ["1", "2", "3", "4"]
    elif opcion_visual == "2":
        tipo_visualizacion = "letras"
        valores_validos = ["A", "B", "C", "D"]
    elif opcion_visual == "3":
        tipo_visualizacion = "simbolos"
        valores_validos = ["♦", "♣", "♥", "♠"]
    else:
        print("Opción inválida. Se usará tipo numérico por defecto.")
        tipo_visualizacion = "numeros"
        valores_validos = ["1", "2", "3", "4"]

    # Elegir dificultad
    print("\nSelecciona nivel de dificultad:")
    print("1. Fácil (6 vacías)")
    print("2. Difícil (10 vacías)")
    dificultad = input("Opción (1-2): ")
    if dificultad == "1":
        dificultad = "facil"
    elif dificultad == "2":
        dificultad = "dificil"
    else:
        print("Opción inválida. Se usará nivel fácil por defecto.")
        dificultad = "facil"

    # Obtener tablero inicial
    tablero = obtener_tablero(dificultad, tipo_visualizacion)

    while True:
        mostrar_tablero(tablero, tipo_visualizacion, dificultad)

        entrada = input("Ingresa fila, columna y valor (ej: 1 2 A o 1 2 0 para borrar): ")
        
        try:
            fila_str, col_str, val = entrada.strip().split()
            fila = int(fila_str)
            col = int(col_str)

            if not (1 <= fila <= 4 and 1 <= col <= 4):
                print("Fila y columna deben estar entre 1 y 4.")
                continue

            if val.upper() == "0":
                tablero[fila - 1][col - 1] = '·'
                print(f"Valor eliminado en ({fila},{col}).")
                continue

            if val.upper() not in valores_validos:
                print(f"Valor inválido. Debe ser uno de: {', '.join(valores_validos)}")
                continue

            tablero[fila - 1][col - 1] = val.upper()

        except ValueError:
            print("Entrada inválida. Usa formato: fila columna valor")
            continue

        if tablero_completo(tablero):
            if validar_tablero(tablero, valores_validos):
                # Convertir rondas_ganadas a entero y calcular puntos
                rondas_ganadas = int(rondas_ganadas)
                puntos = 10 + (2 ** rondas_ganadas - 1)
                puntaje += puntos
                rondas_ganadas += 1
                print(f"\n¡Felicidades! Completaste el tablero.")
                print(f"Puntaje ganado: {puntos} | Puntaje total: {puntaje}")
                time.sleep(2)
                break
            else:
                print("\nEl tablero está completo pero no es válido. Puedes corregir errores usando 0 para borrar.")

    return puntaje, rondas_ganadas
