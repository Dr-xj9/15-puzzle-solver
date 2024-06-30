# BFS en 15 puzzle
from collections import deque
import time

tiempo_inicio = time.time()

def print_puzzle(state):
    for row in state:
        print(" ".join(map(str, row)))
    print()

def get_blank_location(state):
    for i in range(4):
        for j in range(4):
            if state[i][j] == 0:
                return i, j

def is_valid_move(i, j):
    return 0 <= i < 4 and 0 <= j < 4

def apply_move(state, move):
    i, j = get_blank_location(state)
    new_state = [row.copy() for row in state]

    if move == 'UP' and is_valid_move(i - 1, j):
        new_state[i][j], new_state[i - 1][j] = new_state[i - 1][j], new_state[i][j]
    elif move == 'DOWN' and is_valid_move(i + 1, j):
        new_state[i][j], new_state[i + 1][j] = new_state[i + 1][j], new_state[i][j]
    elif move == 'LEFT' and is_valid_move(i, j - 1):
        new_state[i][j], new_state[i][j - 1] = new_state[i][j - 1], new_state[i][j]
    elif move == 'RIGHT' and is_valid_move(i, j + 1):
        new_state[i][j], new_state[i][j + 1] = new_state[i][j + 1], new_state[i][j]

    return new_state

def is_goal_state(state):
    goal_state = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 0]
    ]
    return state == goal_state

def bfs_15_puzzle(initial_state):
    visited_states = set()
    queue = deque([(initial_state, [])])
    movimientos = 0

    while queue:
        current_state, path = queue.popleft()

        if is_goal_state(current_state):
            with open("Solucion_bfs.txt",'w') as archivo:
                for move in path:
                    print(move)
                    archivo.write(move + '\n')
            return movimientos

        if tuple(map(tuple, current_state)) not in visited_states:
            visited_states.add(tuple(map(tuple, current_state)))

            for next_move in ['UP', 'DOWN', 'LEFT', 'RIGHT']:
                new_state = apply_move(current_state, next_move)
                queue.append((new_state, path + [next_move]))
                movimientos += 1

    print("No se encontró una solución.")

initial_puzzle = [
    [1, 2, 0, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 3, 15]
]

movs = bfs_15_puzzle(initial_puzzle)
tiempo_fin = time.time()

tiempo_total = tiempo_fin - tiempo_inicio
with open("Tiempo_bfs.txt", 'w')as arc:
    arc.write("Tiempo total: " + str(tiempo_total) + "\n")
    arc.write("Total de movimientos: " + str(movs))
