from collections import deque

class CentroComercial:
    def __init__(self, mapa=None):
        if mapa is None:
            mapa = {}
        self.mapa = mapa

    def agregar_paso(self, tienda_actual, tienda_vecina):
        if tienda_actual not in self.mapa:
            self.mapa[tienda_actual] = []
        self.mapa[tienda_actual].append(tienda_vecina)

    def buscar_ruta(self, inicio, destino):
        visitados = set()
        cola = deque([(inicio, [inicio])])

        while cola:
            tienda_actual, ruta = cola.popleft()
            visitados.add(tienda_actual)
            if tienda_actual == destino:
                return ruta
            for tienda_vecina in self.mapa.get(tienda_actual, []):
                if tienda_vecina not in visitados:
                    cola.append((tienda_vecina, ruta + [tienda_vecina]))
                    visitados.add(tienda_vecina)

# Ejemplo de uso: mapa de un centro comercial
centro_comercial = CentroComercial({
    'Entrada': ['Tienda A', 'Tienda B'],
    'Tienda A': ['Tienda C'],
    'Tienda B': ['Tienda D', 'Tienda E'],
    'Tienda C': ['Tienda F'],
    'Tienda D': [],
    'Tienda E': ['Tienda F'],
    'Tienda F': []
})

# Buscando la ruta desde la 'Entrada' hasta la 'Tienda F'
punto_inicio = 'Entrada'
tienda_destino = 'Tienda F'
ruta = centro_comercial.buscar_ruta(punto_inicio, tienda_destino)
print("Ruta encontrada:", ruta)

#simula cómo encontrarías el camino más corto dentro de un centro comercial entre dos tiendas.

