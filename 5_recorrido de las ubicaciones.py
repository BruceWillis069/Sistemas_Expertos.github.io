from collections import deque

# Definición del mapa del yermo como un diccionario de listas de adyacencia
yermo = {
    'Refugio 101': ['Megatón', 'Supermercado'],
    'Megatón': ['Tienda de Moira', 'Lucas Simms'],
    'Supermercado': ['Red Rocket', 'Ciudadela'],
    'Tienda de Moira': ['Red Rocket'],
    'Lucas Simms': [],
    'Red Rocket': ['Enclave', 'Ciudadela'],
    'Enclave': [],
    'Ciudadela': []
}

def explorar_yermo(yermo, inicio):
    visitados = set()
    cola = deque([inicio])
    visitados.add(inicio)
    
    while cola:
        lugar = cola.popleft()
        print(lugar, end=' ')
        
        for vecino in yermo[lugar]:
            if vecino not in visitados:
                cola.append(vecino)
                visitados.add(vecino)

# Ejemplo de uso del recorrido por el yermo
print("Exploración por el yermo empezando desde el 'Refugio 101':")
explorar_yermo(yermo, 'Refugio 101')

#se desarrolla un paseon en el yermo empezando por el refugio 101
