from collections import deque  # Importa deque, una estructura de datos similar a una cola doblemente enlazada
import heapq  # Importa heapq, un módulo que proporciona una implementación de cola de prioridad (min-heap)
from scipy.spatial import distance

class Grafo:
    def __init__(self, lista_adyacencia):
        # Inicializa el grafo con una lista de adyacencia que representa las conexiones entre nodos
        self.lista_adyacencia = lista_adyacencia

    def obtener_vecinos(self, v):
        # Devuelve los vecinos de un nodo 'v' utilizando la lista de adyacencia
        return self.lista_adyacencia[v]

    def h(self, nodo_actual, nodo_objetivo):
        # Calcula y devuelve la heurística basada en la distancia Manhattan
        # La distancia Manhattan es la suma de las diferencias absolutas de las coordenadas
        #return abs(nodo_actual[0] - nodo_objetivo[0]) + abs(nodo_actual[1] - nodo_objetivo[1])
        #return distance.chebyshev(nodo_actual, nodo_objetivo)
        return max(abs(a - b) for a, b in zip(nodo_actual, nodo_objetivo))

    def primero_profundidad(self, nodo_inicio, nodo_final):
        # Implementa el algoritmo de búsqueda en profundidad (DFS)
        visitados = set()  # Conjunto para rastrear los nodos visitados
        pila = [(nodo_inicio, [nodo_inicio])]  # Pila para realizar la búsqueda, almacenando el nodo actual y el camino recorrido

        while pila:
            (vertice, camino) = pila.pop()  # Extrae el nodo y el camino actual desde la pila
            if vertice in visitados:  # Si el nodo ya fue visitado, continúa con el siguiente
                continue

            for vecino, _ in self.obtener_vecinos(vertice):  # Itera sobre los vecinos del nodo actual
                if vecino == nodo_final:  # Si se encuentra el nodo objetivo, retorna el camino completo
                    return camino + [vecino]
                else:
                    pila.append((vecino, camino + [vecino]))  # Agrega el vecino a la pila con el camino actualizado

            visitados.add(vertice)  # Marca el nodo actual como visitado

        return None  # Retorna None si no se encuentra un camino al nodo objetivo

    def primero_anchura(self, nodo_inicio, nodo_final):
        # Implementa el algoritmo de búsqueda en anchura (BFS)
        visitados = set()  # Conjunto para rastrear los nodos visitados
        cola = deque([(nodo_inicio, [nodo_inicio])])  # Cola para realizar la búsqueda, almacenando el nodo actual y el camino recorrido

        while cola:
            (vertice, camino) = cola.popleft()  # Extrae el nodo y el camino actual desde la cola
            if vertice in visitados:  # Si el nodo ya fue visitado, continúa con el siguiente
                continue

            for vecino, _ in self.obtener_vecinos(vertice):  # Itera sobre los vecinos del nodo actual
                if vecino == nodo_final:  # Si se encuentra el nodo objetivo, retorna el camino completo
                    return camino + [vecino]
                else:
                    cola.append((vecino, camino + [vecino]))  # Agrega el vecino a la cola con el camino actualizado

            visitados.add(vertice)  # Marca el nodo actual como visitado

        return None  # Retorna None si no se encuentra un camino al nodo objetivo

    def a_estrella(self, nodo_inicio, nodo_final):
        # Implementa el algoritmo A* (A-estrella)
        open_set = []  # Lista que actúa como una cola de prioridad para los nodos por explorar
        heapq.heappush(open_set, (0, nodo_inicio, [nodo_inicio]))  # Inserta el nodo inicial en el open set con prioridad 0
        costos = {nodo_inicio: 0}  # Diccionario para almacenar el costo del camino más barato hasta cada nodo

        while open_set:
            _, actual, camino = heapq.heappop(open_set)  # Extrae el nodo con la menor prioridad (costo + heurística)

            if actual == nodo_final:  # Si se encuentra el nodo objetivo, retorna el camino completo
                return camino

            for vecino, costo in self.obtener_vecinos(actual):  # Itera sobre los vecinos del nodo actual
                nuevo_costo = costos[actual] + costo  # Calcula el costo acumulado para llegar al vecino
                if vecino not in costos or nuevo_costo < costos[vecino]:  # Si se encuentra un camino más barato, se actualiza
                    costos[vecino] = nuevo_costo  # Actualiza el costo del camino más barato al vecino
                    prioridad = nuevo_costo + self.h(vecino, nodo_final)  # Calcula la prioridad del vecino para el open set
                    heapq.heappush(open_set, (prioridad, vecino, camino + [vecino]))  # Agrega el vecino al open set con su prioridad

        return None  # Retorna None si no se encuentra un camino al nodo objetivo
    
