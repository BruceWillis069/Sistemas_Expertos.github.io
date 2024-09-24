import math  # Se importa la biblioteca math para realizar cálculos matemáticos, como la raíz cuadrada.

# Clase que representa las rutas de los camiones en un mapa
class RutasCamiones:
    def __init__(self, mapa_rutas=None):
        # Inicializa el mapa de rutas, que es un diccionario de nodos y sus vecinos con las distancias respectivas.
        if mapa_rutas is None:
            mapa_rutas = {}
        self.mapa_rutas = mapa_rutas

    # Método para agregar una ruta entre dos nodos con una distancia específica
    def agregar_ruta(self, nodo, vecino, distancia):
        # Si el nodo no existe en el mapa de rutas, se crea una entrada para él.
        if nodo not in self.mapa_rutas:
            self.mapa_rutas[nodo] = {}
        # Se añade el vecino y la distancia a la lista de rutas del nodo.
        self.mapa_rutas[nodo][vecino] = distancia

# Función que implementa una heurística basada en la distancia euclidiana entre dos nodos
def heuristica(nodo, objetivo):
    # Desempaqueta las coordenadas (x, y) de los nodos
    x1, y1 = nodo
    x2, y2 = objetivo
    # Retorna la distancia euclidiana entre los dos puntos
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Implementación del algoritmo A* para encontrar el camino más corto
def a_star(rutas, inicio, objetivo):
    # Conjunto de nodos a explorar (nodos abiertos)
    conjunto_abierto = {inicio}
    # Conjunto de nodos ya explorados (nodos cerrados)
    conjunto_cerrado = set()

    # Inicializa el g_score para todos los nodos con infinito (la distancia mínima conocida desde el inicio)
    g_score = {nodo: float('inf') for nodo in rutas.mapa_rutas}
    g_score[inicio] = 0  # La distancia al nodo inicial es 0

    # Inicializa el f_score (g_score + heurística) con infinito para todos los nodos
    f_score = {nodo: float('inf') for nodo in rutas.mapa_rutas}
    f_score[inicio] = heuristica(inicio, objetivo)  # f_score del nodo inicial es solo la heurística

    # Bucle que continúa hasta que se hayan explorado todos los nodos abiertos
    while conjunto_abierto:
        # Selecciona el nodo con el menor f_score de los nodos abiertos
        actual = min(conjunto_abierto, key=lambda nodo: f_score[nodo])

        # Si el nodo actual es el objetivo, se ha encontrado el camino más corto
        if actual == objetivo:
            return True  # Se encontró un camino

        # Mueve el nodo actual del conjunto abierto al conjunto cerrado
        conjunto_abierto.remove(actual)
        conjunto_cerrado.add(actual)

        # Recorre los vecinos del nodo actual
        for vecino, distancia in rutas.mapa_rutas[actual].items():
            # Calcula el puntaje g tentativo para el vecino (distancia desde el inicio hasta el vecino)
            puntaje_g_tentativo = g_score[actual] + distancia

            # Si el puntaje g tentativo es mejor que el g_score actual del vecino
            if puntaje_g_tentativo < g_score[vecino]:
                # Actualiza el g_score y f_score del vecino
                g_score[vecino] = puntaje_g_tentativo
                f_score[vecino] = g_score[vecino] + heuristica(vecino, objetivo)

                # Si el vecino no está en el conjunto cerrado, se añade al conjunto abierto para explorarlo
                if vecino not in conjunto_cerrado:
                    conjunto_abierto.add(vecino)

    # Si el bucle termina y no se ha encontrado un camino, retorna False
    return False  # No se encontró un camino

# Ejemplo de uso del algoritmo A* en un mapa de rutas de camiones
rutas = RutasCamiones({
    # Coordenadas (latitud, longitud) de los puntos, junto con las distancias a los nodos vecinos
    (20.6597, -103.3496): {(20.6597, -103.3480): 1, (20.6580, -103.3496): 2},  # Centro de Guadalajara
    (20.6597, -103.3480): {(20.6597, -103.3496): 1, (20.6605, -103.3480): 1.5},
    (20.6580, -103.3496): {(20.6597, -103.3496): 2, (20.6605, -103.3496): 1.5},
    (20.6605, -103.3480): {(20.6597, -103.3480): 1.5, (20.6605, -103.3496): 1}
})

nodo_inicio = (20.6597, -103.3496)  # Punto de inicio (por ejemplo, punto de carga de un camión)
nodo_objetivo = (20.6605, -103.3480)  # Punto de destino (punto de entrega)
resultado = a_star(rutas, nodo_inicio, nodo_objetivo)

# Imprime si se encontró un camino o no
print("¿Se encontró un camino al objetivo?", resultado)

# Este código modela la navegación de camiones en Guadalajara, donde se busca la mejor ruta entre dos puntos específicos.
# El algoritmo A* optimiza la búsqueda considerando la distancia recorrida y la distancia estimada restante.


# navegación de camiones tumbados en Guadalajara, donde se busca la mejor ruta entre dos puntos específicos. 
# El algoritmo A* se utiliza para optimizar la ruta, considerando tanto la distancia actual como la estimación 
# de la distancia restante
