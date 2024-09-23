class ValorDeInformacion:
    def __init__(self, funcion_utilidad):
        self.funcion_utilidad = funcion_utilidad

    def calcular_valor_informacion(self, probabilidad_previa, probabilidades_posteriores):
        utilidad_previa = self.funcion_utilidad.calcular_utilidad(probabilidad_previa)
        utilidad_esperada = sum(prob * self.funcion_utilidad.calcular_utilidad(prob_post) 
                                for prob, prob_post in zip(probabilidad_previa, probabilidades_posteriores))
        return utilidad_esperada - utilidad_previa

class FuncionUtilidad:
    def __init__(self, pesos):
        self.pesos = pesos

    def calcular_utilidad(self, resultado):
        utilidad = sum(p * x for p, x in zip(self.pesos, resultado))
        return utilidad

# Ejemplo de uso: Decisión sobre qué ruta tomar con información previa y posterior
probabilidad_previa = [0.5, 0.5]  # Probabilidad previa de elegir entre Ruta A o Ruta B
probabilidades_posteriores = [[0.7, 0.3], [0.4, 0.6]]  # Probabilidades de tráfico en cada ruta tras recibir nueva información
pesos = [10, -5]  # Pesos para calcular la utilidad (tiempo ahorrado en minutos y tiempo perdido por tráfico)

funcion_utilidad = FuncionUtilidad(pesos)
valor_informacion = ValorDeInformacion(funcion_utilidad)

valor_info = valor_informacion.calcular_valor_informacion(probabilidad_previa, probabilidades_posteriores)
print("Valor de la información adicional sobre las rutas:", valor_info)

#cómo calcular el beneficio de recibir información adicional, como actualizaciones sobre el tráfico, que te ayuda a tomar una mejor decisión sobre qué ruta seguir.