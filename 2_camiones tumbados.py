import math

class RutasCamiones:
    def __init__(self, mapa_rutas=None):
        if mapa_rutas is None:
            mapa_rutas = {}
        self.mapa_rutas = mapa_rutas

    def agregar_ruta(self, nodo, vecino, distancia):
        if nodo not in self.mapa_rutas:
            self.mapa_rutas[nodo] = {}
        self.mapa_rutas[nodo][vecino] = distancia

def heuristica(nodo, objetivo):
    # Heurística de distancia euclidiana
    x1, y1 = nodo
    x2, y2 = objetivo
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def a_star(rutas, inicio, objetivo):
    conjunto_abierto = {inicio}
    conjunto_cerrado = set()
    g_score = {nodo: float('inf') for nodo in rutas.mapa_rutas}
    g_score[inicio] = 0
    f_score = {nodo: float('inf') for nodo in rutas.mapa_rutas}
    f_score[inicio] = heuristica(inicio, objetivo)

    while conjunto_abierto:
        actual = min(conjunto_abierto, key=lambda nodo: f_score[nodo])
        if actual == objetivo:
            return True  # Se encontró un camino
        conjunto_abierto.remove(actual)
        conjunto_cerrado.add(actual)

        for vecino, distancia in rutas.mapa_rutas[actual].items():
            puntaje_g_tentativo = g_score[actual] + distancia
            if puntaje_g_tentativo < g_score[vecino]:
                g_score[vecino] = puntaje_g_tentativo
                f_score[vecino] = g_score[vecino] + heuristica(vecino, objetivo)
                if vecino not in conjunto_cerrado:
                    conjunto_abierto.add(vecino)

    return False  # No se encontró un camino

# Ejemplo de uso
rutas = RutasCamiones({
    (20.6597, -103.3496): {(20.6597, -103.3480): 1, (20.6580, -103.3496): 2},  # Centro de GDL
    (20.6597, -103.3480): {(20.6597, -103.3496): 1, (20.6605, -103.3480): 1.5},
    (20.6580, -103.3496): {(20.6597, -103.3496): 2, (20.6605, -103.3496): 1.5},
    (20.6605, -103.3480): {(20.6597, -103.3480): 1.5, (20.6605, -103.3496): 1}
})

nodo_inicio = (20.6597, -103.3496)  # Punto de carga
nodo_objetivo = (20.6605, -103.3480)  # Punto de entrega
resultado = a_star(rutas, nodo_inicio, nodo_objetivo)
print("¿Se encontró un camino al objetivo?", resultado)

# navegación de camiones tumbados en Guadalajara, donde se busca la mejor ruta entre dos puntos específicos. 
# El algoritmo A* se utiliza para optimizar la ruta, considerando tanto la distancia actual como la estimación 
# de la distancia restante
