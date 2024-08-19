def convertir_a_lista_adyacencia(laberinto):
    lista_adyacencia = {}
    filas = len(laberinto)
    columnas = len(laberinto[0])
    for i in range(filas):
        for j in range(columnas):
            # Consideramos 0, 2 y 3 como celdas transitables
            if laberinto[i][j] in [0, 2, 3]:
                lista_adyacencia[(i, j)] = []
                for (di, dj) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < filas and 0 <= nj < columnas and laberinto[ni][nj] in [0, 2, 3]:
                        lista_adyacencia[(i, j)].append((ni, nj))
    return lista_adyacencia
def encontrar_inicio_y_fin(laberinto):
    for i in range(len(laberinto)):
        for j in range(len(laberinto[0])):
            if laberinto[i][j] == 2:
                inicio = (i, j)
            elif laberinto[i][j] == 3:
                fin = (i, j)
    return inicio, fin
class Grafo:

    def __init__(self, lista_adyacencia):
        self.lista_adyacencia = lista_adyacencia

    def obtener_vecinos(self, v):
        return self.lista_adyacencia[v]

    # funcion heuristica
    def h(self, n, objetivo):
        # Distancia de Manhattan
        return abs(n[0] - objetivo[0]) + abs(n[1] - objetivo[1])

    def primero_profundidad(self, nodo_inicio, nodo_final):
        visitados = set()
        pila = [(nodo_inicio, [nodo_inicio])]

        while pila:
            (vertice, camino) = pila.pop()
            if vertice not in visitados:
                if vertice == nodo_final:
                    return camino
                visitados.add(vertice)
                for vecino in self.obtener_vecinos(vertice):
                    pila.append((vecino, camino + [vecino]))
        return None

    def primero_anchura(self, nodo_inicio, nodo_final):
        visitados = set()
        cola = [(nodo_inicio, [nodo_inicio])]

        while cola:
            (vertice, camino) = cola.pop(0)
            if vertice not in visitados:
                if vertice == nodo_final:
                    return camino
                visitados.add(vertice)
                for vecino in self.obtener_vecinos(vertice):
                    cola.append((vecino, camino + [vecino]))
        return None

    def a_estrella(self, nodo_inicio, nodo_final):
        from heapq import heappop, heappush

        open_set = []
        heappush(open_set, (0, nodo_inicio, [nodo_inicio]))
        g_score = {nodo_inicio: 0}
        f_score = {nodo_inicio: self.h(nodo_inicio, nodo_final)}

        while open_set:
            _, current, camino = heappop(open_set)
            if current == nodo_final:
                return camino

            for vecino in self.obtener_vecinos(current):
                tentative_g_score = g_score[current] + 1  # Asume un costo uniforme
                if vecino not in g_score or tentative_g_score < g_score[vecino]:
                    g_score[vecino] = tentative_g_score
                    f_score[vecino] = tentative_g_score + self.h(vecino, nodo_final)
                    heappush(open_set, (f_score[vecino], vecino, camino + [vecino]))
        return None
       

if __name__ == '__main__':
    laberinto = [
    [2, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 3]
]

# Convertimos el laberinto en una lista de adyacencia
    

    lista_adyacencia = convertir_a_lista_adyacencia(laberinto)
    inicio,fin=encontrar_inicio_y_fin(laberinto)
    grafo = Grafo(lista_adyacencia)
    camino_dfs = grafo.primero_profundidad(inicio, fin)
    print("Camino DFS:", camino_dfs)
    camino_bfs = grafo.primero_anchura(inicio, fin)
    print("Camino BFS:", camino_bfs)
    camino_a_estrella = grafo.a_estrella(inicio, fin)
    print("Camino A*:", camino_a_estrella)
