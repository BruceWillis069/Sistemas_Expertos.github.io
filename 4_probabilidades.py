# Clase que calcula el valor de la información adicional basada en la utilidad esperada
class ValorDeInformacion:
    def __init__(self, funcion_utilidad):
        # Inicializa con una función de utilidad que se usará para calcular los beneficios.
        self.funcion_utilidad = funcion_utilidad

    # Método que calcula el valor de la información
    # Recibe la probabilidad previa (antes de tener nueva información) y las probabilidades posteriores (después de obtener nueva información)
    def calcular_valor_informacion(self, probabilidad_previa, probabilidades_posteriores):
        # Calcula la utilidad antes de recibir información adicional
        utilidad_previa = self.funcion_utilidad.calcular_utilidad(probabilidad_previa)
        
        # Calcula la utilidad esperada después de recibir información adicional
        utilidad_esperada = sum(
            prob * self.funcion_utilidad.calcular_utilidad(prob_post) 
            for prob, prob_post in zip(probabilidad_previa, probabilidades_posteriores)
        )
        
        # Retorna la diferencia entre la utilidad esperada y la utilidad previa (valor de la información)
        return utilidad_esperada - utilidad_previa

# Clase que define una función de utilidad, que calcula el valor de un resultado según ciertos pesos
class FuncionUtilidad:
    def __init__(self, pesos):
        # Inicializa con los pesos, que reflejan la importancia de cada factor en la utilidad
        self.pesos = pesos

    # Método para calcular la utilidad de un resultado dado, usando los pesos
    def calcular_utilidad(self, resultado):
        # Multiplica cada peso por el valor correspondiente del resultado y suma los productos
        utilidad = sum(p * x for p, x in zip(self.pesos, resultado))
        return utilidad

# Ejemplo de uso: Decisión sobre qué ruta tomar con información previa y posterior al recibir nueva información
# Probabilidad inicial (previa) de elegir entre dos rutas (Ruta A y Ruta B)
probabilidad_previa = [0.5, 0.5]  # Ambas rutas tienen la misma probabilidad de ser elegidas inicialmente

# Probabilidades de cada ruta después de recibir nueva información sobre el tráfico
probabilidades_posteriores = [
    [0.7, 0.3],  # Nueva información indica que Ruta A tiene mayor probabilidad de ser mejor opción
    [0.4, 0.6]   # Para otra situación, Ruta B es la mejor opción
]

# Pesos utilizados en la función de utilidad:
# 10 representa minutos ahorrados en tiempo si eliges bien,
# -5 representa minutos perdidos debido al tráfico si eliges mal.
pesos = [10, -5]

# Crea una función de utilidad usando los pesos definidos
funcion_utilidad = FuncionUtilidad(pesos)

# Crea el objeto ValorDeInformacion con la función de utilidad asociada
valor_informacion = ValorDeInformacion(funcion_utilidad)

# Calcula el valor de la información adicional utilizando las probabilidades previas y las probabilidades posteriores
valor_info = valor_informacion.calcular_valor_informacion(probabilidad_previa, probabilidades_posteriores)

# Imprime el valor de la información adicional
print("Valor de la información adicional sobre las rutas:", valor_info)

# Este código muestra cómo calcular el beneficio de recibir información adicional, como actualizaciones sobre el tráfico,
# que te ayudan a tomar una mejor decisión sobre qué ruta seguir.
