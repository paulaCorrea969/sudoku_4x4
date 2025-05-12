import random

VALORES = {
    "numeros": ["1", "2", "3", "4"],
    "letras": ["A", "B", "C", "D"],
    "simbolos": ["", "", "", ""]
}

TABLEROS_COMPLETOS = [
    [
        ["1", "2", "3", "4"],
        ["3", "4", "1", "2"],
        ["2", "1", "4", "3"],
        ["4", "3", "2", "1"]
    ],
    [
        ["4", "3", "2", "1"],
        ["2", "1", "4", "3"],
        ["3", "4", "1", "2"],
        ["1", "2", "3", "4"]
    ]
]

def obtener_tablero(dificultad, tipo_visualizacion):
    tablero_base = random.choice(TABLEROS_COMPLETOS)
    valores = VALORES[tipo_visualizacion]
    
    conversion = dict(zip(["1", "2", "3", "4"], valores))
    tablero = [[conversion[val] for val in fila] for fila in tablero_base]

    vacias = 6 if dificultad == "facil" else 10
    posiciones = [(i, j) for i in range(4) for j in range(4)]
    random.shuffle(posiciones)

    for _ in range(vacias):
        i, j = posiciones.pop()
        tablero[i][j] = "·"

    return tablero
