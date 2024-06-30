import matplotlib.pyplot as plt

with open("Tiempo_bfs.txt", 'r') as archivo:
    lineas = archivo.readlines()

tiempoBFS = float(lineas[0].split(':')[-1].strip())
movsBFS = int(lineas[1].split(':')[-1].strip())

with open("Tiempo_Astar.txt", 'r') as archivo:
    lineas = archivo.readlines()

tiempoAstar = float(lineas[0].split(':')[-1].strip())
movsAstar = int(lineas[1].split(':')[-1].strip())

fig, ax = plt.subplots()

algs = ['A*', 'BFS', 'DFS']
tiempos = [tiempoAstar, tiempoBFS, 0]
bar_labels = ['red', 'blue', '_red']
bar_colors = ['tab:red', 'tab:blue', 'tab:red']

ax.bar(algs, tiempos, label=bar_labels, color=bar_colors)
ax.set_ylabel('Tiempo de ejecución en segundos')
ax.set_title('Eficicencia temporal en resolver 15 puzzle')
plt.annotate("Excedió memoria", xy=(2, 10), ha='center')

plt.show()

fig, ax = plt.subplots()

algs = ['A*', 'BFS', 'DFS']
tiempos = [movsAstar, movsBFS, 0]
bar_labels = ['red', 'blue', '_red']
bar_colors = ['tab:red', 'tab:blue', 'tab:red']

ax.bar(algs, tiempos, label=bar_labels, color=bar_colors)
ax.set_ylabel('Movimientos')
ax.set_title('Cantidad de movimientos al resolver 15 puzzle')
plt.annotate("Excedió memoria", xy=(2, 10), ha='center')

plt.show()



