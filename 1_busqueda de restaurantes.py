# Definición de la clase Ciudad para modelar un mapa de calles y realizar búsquedas de lugares
class Ciudad:
    def __init__(self, mapa_calles=None):
        # Inicializa el mapa de calles como un diccionario donde cada lugar tiene una lista de lugares vecinos.
        if mapa_calles is None:
            mapa_calles = {}
        self.mapa_calles = mapa_calles

    # Método para agregar una calle entre dos lugares
    def agregar_calle(self, lugar_actual, lugar_vecino):
        # Si el lugar actual no está en el mapa de calles, se agrega con una lista vacía
        if lugar_actual not in self.mapa_calles:
            self.mapa_calles[lugar_actual] = []
        # Se añade el lugar vecino a la lista de calles conectadas al lugar actual
        self.mapa_calles[lugar_actual].append(lugar_vecino)

    # Método para buscar un restaurante específico dentro de la ciudad con un límite de giros permitidos
    def buscar_restaurante(self, inicio, restaurante_deseado, limite_giros, visitados=None):
        # Inicializa un conjunto de lugares ya visitados para evitar ciclos (si no se ha proporcionado uno)
        if visitados is None:
            visitados = set()
        # Si el límite de giros es mayor o igual a cero, se puede seguir buscando
        if limite_giros >= 0:
            # Marca el lugar actual como visitado
            visitados.add(inicio)
            print(f"Visitando: {inicio}")  # Imprime el lugar que se está visitando
            
            # Si el lugar actual es el restaurante deseado, retorna True indicando que se ha encontrado
            if inicio == restaurante_deseado:
                return True
            
            # Si el límite de giros es igual a 4, se detiene la búsqueda (condición de parada por giros)
            if limite_giros == 4:
                return False

            # Recorre los lugares vecinos del lugar actual
            for lugar_vecino in self.mapa_calles.get(inicio, []):
                # Si el lugar vecino no ha sido visitado, se busca recursivamente en él
                if lugar_vecino not in visitados:
                    # Reduce el límite de giros y realiza la búsqueda desde el lugar vecino
                    if self.buscar_restaurante(lugar_vecino, restaurante_deseado, limite_giros - 1, visitados):
                        return True  # Si se encuentra el restaurante en algún camino, retorna True
        
        # Si se termina de explorar el lugar actual y sus vecinos sin encontrar el restaurante, retorna False
        return False

# Ejemplo de uso: mapa de calles de una ciudad
ciudad = Ciudad({
    'Casa': ['Plaza', 'Centro Comercial'],
    'Plaza': ['Restaurante A', 'Cafetería'],
    'Centro Comercial': ['Restaurante B', 'Parque'],
    'Restaurante A': [],  # Restaurante A no tiene vecinos
    'Cafetería': [],      # La Cafetería no tiene vecinos
    'Restaurante B': ['Museo'],
    'Parque': ['Restaurante C'],
    'Museo': [],          # El Museo no tiene vecinos
    'Restaurante C': []    # Restaurante C no tiene vecinos
})

# Buscando el 'Restaurante C' desde 'Casa' con un límite de 3 giros permitidos
punto_inicio = 'Casa'
restaurante_deseado = 'Restaurante C'
limite_giros = 3  # Establecemos que solo se pueden realizar hasta 3 giros
print("Búsqueda de restaurante con un límite de giros:")
ciudad.buscar_restaurante(punto_inicio, restaurante_deseado, limite_giros)

# Este código modela una ciudad con calles conectadas entre lugares. El objetivo es buscar un restaurante específico
# partiendo desde un lugar inicial ('Casa') y con un límite de giros o cambios de dirección (en este caso, 3).
# Si se llega al límite de giros sin encontrar el restaurante, la búsqueda se detiene.


#se simula una búsqueda donde quieres encontrar un restaurante específico, pero solo puedes realizar hasta 3 giros o cambios de dirección en las calles. Si llegas al límite de giros sin encontrar el restaurante, te detienes.
