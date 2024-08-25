from laberinto import leer_laberinto, laberinto_a_grafo, encontrar_inicio_y_fin, mostrar_laberinto
from grafo import Grafo


def resolver_laberinto(archivo_laberinto):
    laberinto = leer_laberinto(archivo_laberinto)
    grafo = laberinto_a_grafo(laberinto)
    g = Grafo(grafo)

    inicio,final=encontrar_inicio_y_fin(laberinto)
    nodo_inicio = inicio  # Esto dependerá de dónde esté tu salida
    nodo_final = final  # Esto dependerá de dónde esté tu meta

    # Escoger algoritmo
    camino_profundidad = g.primero_profundidad(nodo_inicio, nodo_final)
    camino_anchura = g.primero_anchura(nodo_inicio, nodo_final)
    camino_a_estrella = g.a_estrella(nodo_inicio, nodo_final)

    print("Solución con Búsqueda en Profundidad:", camino_profundidad)
    print("Solución con Búsqueda en Anchura:", camino_anchura)
    print("Solución con A*:", camino_a_estrella)

    if camino_profundidad:
        mostrar_laberinto(laberinto, camino_profundidad, "Camino profundidad")
    if camino_anchura:
        mostrar_laberinto(laberinto, camino_anchura, "Camino anchura")
    if camino_a_estrella:
        mostrar_laberinto(laberinto, camino_a_estrella, "Camino A*")

if __name__ == "__main__":
    resolver_laberinto('laberinto2.txt')
