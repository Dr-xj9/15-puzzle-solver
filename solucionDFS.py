import time

def encontrar_espacio_vacio(estado):
    for i in range(4):
        for j in range(4):
            if estado[i][j] == 0:
                return i, j

def aplicar_accion(estado, accion):
    i, j = encontrar_espacio_vacio(estado)
    nuevo_estado = [fila[:] for fila in estado]
    if accion == 'UP':
        nuevo_estado[i][j], nuevo_estado[i - 1][j] = nuevo_estado[i - 1][j], nuevo_estado[i][j]
    elif accion == 'DOWN':
        nuevo_estado[i][j], nuevo_estado[i + 1][j] = nuevo_estado[i + 1][j], nuevo_estado[i][j]
    elif accion == 'LEFT':
        nuevo_estado[i][j], nuevo_estado[i][j - 1] = nuevo_estado[i][j - 1], nuevo_estado[i][j]
    elif accion == 'RIGHT':
        nuevo_estado[i][j], nuevo_estado[i][j + 1] = nuevo_estado[i][j + 1], nuevo_estado[i][j]
    return nuevo_estado

def acciones_posibles(estado):
    acciones = []
    i, j = encontrar_espacio_vacio(estado)
    if i > 0:
        acciones.append('UP')
    if i < 3:
        acciones.append('DOWN')
    if j > 0:
        acciones.append('LEFT')
    if j < 3:
        acciones.append('RIGHT')
    return acciones

def es_objetivo(estado):
    return estado == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]

def dfs(estado):
    stack = [(estado, [], 0)]  # Se añade un tercer elemento a la tupla para contar los cambios

    while stack:
        estado_actual, camino, cambios = stack.pop()

        if es_objetivo(estado_actual):
            return camino, cambios

        for accion in acciones_posibles(estado_actual):
            nuevo_estado = aplicar_accion(estado_actual, accion)
            if nuevo_estado not in camino:
                nuevo_camino = camino + [accion]
                stack.append((nuevo_estado, nuevo_camino, cambios + 1))

    return None, None  # No se encontró solución

tiempo_inicio = time.time()

estado_inicial = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 0, 15]
]

solucion_dfs, cambios_dfs = dfs(estado_inicial)

tiempo_fin = time.time()
tiempo_total = tiempo_fin - tiempo_inicio

with open("Tiempo_dfs.txt", 'w') as arc:
    arc.write("Tiempo total: " + str(tiempo_total) + " \n")
    arc.write("\n\nTotal de cambios realizados: " + str(cambios_dfs))

with open("Solucion_dfs.txt", "w") as archivo:
    if solucion_dfs is not None:
        archivo.write('\n'.join(solucion_dfs))
    else:
        archivo.write("No se encontró solución.")
