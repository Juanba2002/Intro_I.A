import matplotlib.pyplot as plt
import numpy as np
def leer_laberinto(archivo):
    with open(archivo, 'r') as f:
        lines = f.readlines()

    laberinto = []
    for line in lines[1:]:  # Saltamos la primera línea que contiene el tamaño del laberinto
        fila = list(map(int, line.strip()[1:-1].split(',')))
        laberinto.append(fila)

    return laberinto

def laberinto_a_grafo(laberinto):
    grafo = {}
    filas = len(laberinto)
    columnas = len(laberinto[0])

    for i in range(filas):
        for j in range(columnas):
            if laberinto[i][j] != 1:  # Si no es una pared
                vecinos = []
                if i > 0 and laberinto[i-1][j] != 1:  # Arriba
                    vecinos.append(((i-1, j), 1))
                if i < filas-1 and laberinto[i+1][j] != 1:  # Abajo
                    vecinos.append(((i+1, j), 1))
                if j > 0 and laberinto[i][j-1] != 1:  # Izquierda
                    vecinos.append(((i, j-1), 1))
                if j < columnas-1 and laberinto[i][j+1] != 1:  # Derecha
                    vecinos.append(((i, j+1), 1))

                grafo[(i, j)] = vecinos

    return grafo
def encontrar_inicio_y_fin(laberinto):
    inicio = None
    fin = None

    for i in range(len(laberinto)):
        for j in range(len(laberinto[0])):
            if laberinto[i][j] == 2:
                inicio = (i, j)
            elif laberinto[i][j] == 3:
                fin = (i, j)

    return inicio, fin
def mostrar_laberinto(laberinto, camino, titulo):
    laberinto_np = np.array(laberinto)
    fig, ax = plt.subplots()
    
    # Mapa de colores: 1 para paredes, 0 para caminos, 2 para inicio, 3 para meta
    cmap = plt.cm.colors.ListedColormap(['white', 'black', 'red', 'green'])
    bounds = [-0.5, 0.5, 1.5, 2.5, 3.5]
    norm = plt.cm.colors.BoundaryNorm(bounds, cmap.N)

    ax.imshow(laberinto_np, cmap=cmap, norm=norm)

    # Marca el camino en el laberinto
    for (i, j) in camino:
        ax.plot(j, i, 'o', color='blue')

    ax.set_title(titulo)
    plt.show()