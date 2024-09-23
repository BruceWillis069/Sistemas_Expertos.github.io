from collections import deque

# Definición de un mapa de la ciudad como un diccionario de listas de adyacencia
ciudad = {
    'Casa': ['Parque', 'Tienda'],
    'Parque': ['Café'],
    'Tienda': ['Cine', 'Restaurante'],
    'Café': ['Trabajo'],
    'Cine': [],
    'Restaurante': ['Trabajo'],
    'Trabajo': []
}

def recorrer_ciudad(ciudad, inicio):
    visitados = set()
    cola = deque([inicio])
    visitados.add(inicio)
    
    while cola:
        lugar = cola.popleft()
        print(lugar, end=' ')
        
        for vecino in ciudad[lugar]:
            if vecino not in visitados:
                cola.append(vecino)
                visitados.add(vecino)

# Ejemplo de uso del recorrido en la ciudad
print("Recorrido por las ubicaciones empezando desde la 'Casa':")
recorrer_ciudad(ciudad, 'Casa')