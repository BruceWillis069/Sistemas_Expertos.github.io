from collections import deque  # Importa deque, que es una cola de doble extremo eficiente para la búsqueda en anchura (BFS).

# Clase que modela el centro comercial y las rutas entre tiendas
class CentroComercial:
    def __init__(self, mapa=None):
        # Si no se proporciona un mapa al crear el centro comercial, inicializa uno vacío.
        if mapa is None:
            mapa = {}
        # Guarda el mapa del centro comercial (grafo) donde cada tienda tiene una lista de tiendas vecinas.
        self.mapa = mapa

    # Método para agregar una conexión o paso entre tiendas
    def agregar_paso(self, tienda_actual, tienda_vecina):
        # Si la tienda actual no está en el mapa, la inicializa con una lista vacía.
        if tienda_actual not in self.mapa:
            self.mapa[tienda_actual] = []
        # Agrega la tienda vecina a la lista de tiendas conectadas a la tienda actual.
        self.mapa[tienda_actual].append(tienda_vecina)

    # Método para buscar la ruta más corta entre dos tiendas utilizando BFS
    def buscar_ruta(self, inicio, destino):
        visitados = set()  # Conjunto para rastrear las tiendas que ya se han visitado.
        # Cola que almacena las tiendas por explorar junto con la ruta que lleva hasta ellas.
        cola = deque([(inicio, [inicio])])

        # Bucle que recorre la cola mientras haya tiendas por explorar.
        while cola:
            # Extrae el primer elemento de la cola (tienda actual y la ruta hasta ella).
            tienda_actual, ruta = cola.popleft()
            # Marca la tienda actual como visitada.
            visitados.add(tienda_actual)
            # Si la tienda actual es el destino, retorna la ruta completa.
            if tienda_actual == destino:
                return ruta
            # Recorre las tiendas vecinas de la tienda actual.
            for tienda_vecina in self.mapa.get(tienda_actual, []):
                # Si la tienda vecina no ha sido visitada aún, la agrega a la cola con la ruta actualizada.
                if tienda_vecina not in visitados:
                    cola.append((tienda_vecina, ruta + [tienda_vecina]))
                    visitados.add(tienda_vecina)  # Marca la vecina como visitada para evitar ciclos.

# Ejemplo de uso: se define un mapa de tiendas en un centro comercial.
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
# Se busca la ruta más corta entre la entrada y la tienda F usando BFS.
ruta = centro_comercial.buscar_ruta(punto_inicio, tienda_destino)
print("Ruta encontrada:", ruta)  # Muestra la ruta encontrada.


#simula cómo encontrarías el camino más corto dentro de un centro comercial entre dos tiendas.

