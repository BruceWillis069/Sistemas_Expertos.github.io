from collections import deque  # Importa deque, una estructura de datos tipo cola eficiente para recorridos en anchura (BFS).

# Definición del mapa del yermo usando un diccionario.
# Las llaves son los lugares (nodos) y los valores son listas de lugares adyacentes (vecinos a los que se puede viajar directamente).
yermo = {
    'Refugio 101': ['Megatón', 'Supermercado'],  # Desde el 'Refugio 101' se puede ir a 'Megatón' y 'Supermercado'
    'Megatón': ['Tienda de Moira', 'Lucas Simms'],  # Desde 'Megatón' se puede ir a la 'Tienda de Moira' o hablar con 'Lucas Simms'
    'Supermercado': ['Red Rocket', 'Ciudadela'],  # Desde el 'Supermercado' se puede ir a 'Red Rocket' o a la 'Ciudadela'
    'Tienda de Moira': ['Red Rocket'],  # La 'Tienda de Moira' tiene una conexión directa a 'Red Rocket'
    'Lucas Simms': [],  # 'Lucas Simms' no tiene lugares adyacentes
    'Red Rocket': ['Enclave', 'Ciudadela'],  # Desde 'Red Rocket' se puede ir a 'Enclave' o a la 'Ciudadela'
    'Enclave': [],  # 'Enclave' no tiene lugares adyacentes
    'Ciudadela': []  # 'Ciudadela' no tiene lugares adyacentes
}

# Función para explorar el yermo usando un recorrido en anchura (BFS)
def explorar_yermo(yermo, inicio):
    visitados = set()  # Conjunto para almacenar los lugares que ya han sido visitados
    cola = deque([inicio])  # Cola para el recorrido BFS, inicializada con el lugar de inicio
    visitados.add(inicio)  # Marca el lugar inicial como visitado
    
    # Bucle que recorre la cola mientras haya lugares por explorar
    while cola:
        lugar = cola.popleft()  # Extrae el primer lugar en la cola
        print(lugar, end=' ')  # Imprime el lugar actual con un espacio para separarlo
        
        # Recorre todos los vecinos (lugares adyacentes) del lugar actual
        for vecino in yermo[lugar]:
            if vecino not in visitados:  # Si el vecino no ha sido visitado aún
                cola.append(vecino)  # Lo añade a la cola para ser explorado
                visitados.add(vecino)  # Marca al vecino como visitado para evitar visitarlo dos veces

# Ejemplo de uso: exploración del yermo empezando desde el 'Refugio 101'
print("Exploración por el yermo empezando desde el 'Refugio 101':")
explorar_yermo(yermo, 'Refugio 101')  # Llama a la función para recorrer el yermo


#se desarrolla un paseon en el yermo empezando por el refugio 101
