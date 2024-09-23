class Ciudad:
    def __init__(self, mapa_calles=None):
        if mapa_calles is None:
            mapa_calles = {}
        self.mapa_calles = mapa_calles

    def agregar_calle(self, lugar_actual, lugar_vecino):
        if lugar_actual not in self.mapa_calles:
            self.mapa_calles[lugar_actual] = []
        self.mapa_calles[lugar_actual].append(lugar_vecino)

    def buscar_restaurante(self, inicio, restaurante_deseado, limite_giros, visitados=None):
        if visitados is None:
            visitados = set()
        if limite_giros >= 0:
            visitados.add(inicio)
            print(f"Visitando: {inicio}")
            if inicio == restaurante_deseado:
                return True
            if limite_giros == 4:
                return False
            for lugar_vecino in self.mapa_calles.get(inicio, []):
                if lugar_vecino not in visitados:
                    if self.buscar_restaurante(lugar_vecino, restaurante_deseado, limite_giros - 1, visitados):
                        return True
        return False

# Ejemplo de uso
ciudad = Ciudad({
    'Casa': ['Plaza', 'Centro Comercial'],
    'Plaza': ['Restaurante A', 'Cafetería'],
    'Centro Comercial': ['Restaurante B', 'Parque'],
    'Restaurante A': [],
    'Cafetería': [],
    'Restaurante B': ['Museo'],
    'Parque': ['Restaurante C'],
    'Museo': [],
    'Restaurante C': []
})

# Buscando el 'Restaurante C' desde la 'Casa' con un límite de 3 giros
punto_inicio = 'Casa'
restaurante_deseado = 'Restaurante C'
limite_giros = 3
print("Búsqueda de restaurante con un límite de giros:")
ciudad.buscar_restaurante(punto_inicio, restaurante_deseado, limite_giros)

#se simula una búsqueda donde quieres encontrar un restaurante específico, pero solo puedes realizar hasta 3 giros o cambios de dirección en las calles. Si llegas al límite de giros sin encontrar el restaurante, te detienes.