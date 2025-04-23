def mostrar_tablero(tablero, tipo, dificultad):
    bordes = "*" if dificultad == "facil" else "-"
    print(bordes * 17)
    for fila in tablero:
        linea = ""
        for celda in fila:
            linea += f" {celda} "
        print(f"{bordes}{linea}{bordes}")
    print(bordes * 17)


def validar_tablero(tablero, valores_validos):
    def regiones_validas(tablero):
        regiones = [
            [tablero[0][0], tablero[0][1], tablero[1][0], tablero[1][1]],
            [tablero[0][2], tablero[0][3], tablero[1][2], tablero[1][3]],
            [tablero[2][0], tablero[2][1], tablero[3][0], tablero[3][1]],
            [tablero[2][2], tablero[2][3], tablero[3][2], tablero[3][3]],
        ]
        for region in regiones:
            if sorted(region) != sorted(valores_validos):
                return False
        return True

    for fila in tablero:
        if sorted(fila) != sorted(valores_validos):
            return False

    for col in range(4):
        columna = [tablero[fila][col] for fila in range(4)]
        if sorted(columna) != sorted(valores_validos):
            return False

    return regiones_validas(tablero)


def tablero_completo(tablero):
    for fila in tablero:
        if "·" in fila:
            return False
    return True
