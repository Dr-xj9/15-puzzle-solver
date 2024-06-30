# A* Algoritmo
from queue import PriorityQueue
import time

tiempo_inicio = time.time()
# Función heurística (distancia Manhattan)
def heuristica(estado):
    objetivo = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
    distancia = 0
    for i in range(4):
        for j in range(4):
            if estado[i][j] != objetivo[i][j] and estado[i][j] != 0:
                objetivo_pos = [(r, c) for r, row in enumerate(objetivo) for c, val in enumerate(row) if val == estado[i][j]][0]
                distancia += abs(i - objetivo_pos[0]) + abs(j - objetivo_pos[1])
    return distancia

# Funciones auxiliares
def acciones_posibles(estado):
    acciones = []
    i, j = encontrar_espacio_vacio(estado)
    if i > 0:
        acciones.append('up')
    if i < 3:
        acciones.append('down')
    if j > 0:
        acciones.append('left')
    if j < 3:
        acciones.append('right')
    return acciones

def encontrar_espacio_vacio(estado):
    for i in range(4):
        for j in range(4):
            if estado[i][j] == 0:
                return i, j

def aplicar_accion(estado, accion):
    i, j = encontrar_espacio_vacio(estado)
    nuevo_estado = [fila[:] for fila in estado]
    if accion == 'up':
        nuevo_estado[i][j], nuevo_estado[i - 1][j] = nuevo_estado[i - 1][j], nuevo_estado[i][j]
    elif accion == 'down':
        nuevo_estado[i][j], nuevo_estado[i + 1][j] = nuevo_estado[i + 1][j], nuevo_estado[i][j]
    elif accion == 'left':
        nuevo_estado[i][j], nuevo_estado[i][j - 1] = nuevo_estado[i][j - 1], nuevo_estado[i][j]
    elif accion == 'right':
        nuevo_estado[i][j], nuevo_estado[i][j + 1] = nuevo_estado[i][j + 1], nuevo_estado[i][j]
    return nuevo_estado

def es_objetivo(estado):
    return estado == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]

# Algoritmo A*
def a_estrella(estado_inicial):
    frontera = PriorityQueue()
    frontera.put((heuristica(estado_inicial), estado_inicial, []))

    visitados = set()
    movimientos = 0

    while not frontera.empty():
        _, estado_actual, camino = frontera.get()

        if es_objetivo(estado_actual):
            return camino, movimientos

        visitados.add(tuple(map(tuple, estado_actual)))

        for accion in acciones_posibles(estado_actual):
            nuevo_estado = aplicar_accion(estado_actual, accion)
            if tuple(map(tuple, nuevo_estado)) not in visitados:
                nuevo_camino = camino + [accion]
                costo = len(nuevo_camino) + heuristica(nuevo_estado)
                frontera.put((costo, nuevo_estado, nuevo_camino))
                movimientos += 1

    return None, 0 # No se encontró solución

estado_inicial = [[1, 2, 0, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 3, 15]]

solucion, movimientos = a_estrella(estado_inicial)

tiempo_fin = time.time()
tiempo_total = tiempo_fin - tiempo_inicio

with open("Tiempo_Astar.txt", 'w') as arc:
    arc.write("Tiempo total: " + str(tiempo_total) + "\n")
    arc.write("Total de movimientos: " + str(movimientos))
    
with open('Solucion_Astar.txt', 'w') as archivo:
    archivo.write('\n'.join(solucion))
