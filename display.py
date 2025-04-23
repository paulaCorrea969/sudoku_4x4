def obtener_simbolos(opcion):
    if opcion == "1":
        return ["1", "2", "3", "4"]
    elif opcion == "2":
        return ["A", "B", "C", "D"]
    elif opcion == "3":
        return ["♦", "♣", "♥", "♠"]
    else:
        return ["1", "2", "3", "4"]  # por defecto

def convertir_valor(valor, visualizacion):
    simbolos = obtener_simbolos(visualizacion)
    if valor == 0:
        return "·"
    return simbolos[valor - 1]

def mostrar_tablero(tablero, visualizacion, dificultad):
    borde = "*" if dificultad == "1" else "-"
    print("\n" + borde * 17)
    for i, fila in enumerate(tablero):
        print(borde, end=" ")
        for j, valor in enumerate(fila):
            simbolo = convertir_valor(valor, visualizacion)
            print(simbolo, end=" ")
        print(borde)
    print(borde * 17)
