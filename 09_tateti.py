"""
1. Tablero
2. Fichas
3. Solicitar al jugador que ponga la ficha en el tablero nueve veces
"""
datos = [["_", "_", "_"],["_", "_", "_"],["_", "_", "_"]]
posicion = 0
def tablero():
    for fila in datos:
        for columna in fila:
            print(columna, end='')
        print('')

def pedirPosicion(ficha):
    posicion = int(input('Poner la ficha ' + ficha + ' en la posición: '))
    return posicion

def ponerFicha(ficha, posicion):
    if posicion >= 1 and posicion <= 3:
        datos[0][posicion - 1] = ficha
    if posicion >= 4 and posicion <= 6:
        datos[1][posicion - 4] = ficha
    if posicion >= 7 and posicion <= 9:
        datos[2][posicion - 7] = ficha

tablero()
for veces in range(1,10):
    ficha = 'X'
    if veces % 2 == 0:
        ficha = 'O'
    posicion = pedirPosicion(ficha)
    ponerFicha(ficha, posicion)
    tablero()


