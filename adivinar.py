import random
import json
import tkinter as tk
from tkinter import messagebox

# Base de datos de personajes con sus características
personajes = [
    {"nombre": "Luke Skywalker", "sable_luz": True, "humano": True, "lado_oscuro": False, "jedi": True, "droide": False, "cazarrecompensas": False, "casco": False, "sith": False, "rebelde": True, "wookie": False, "lider_batalla": False, "relacion_familiar": True},
    {"nombre": "Leia Organa", "sable_luz": False, "humano": True, "lado_oscuro": False, "jedi": False, "droide": False, "cazarrecompensas": False, "casco": False, "sith": False, "rebelde": True, "wookie": False},
    {"nombre": "Darth Vader", "sable_luz": True, "humano": True, "lado_oscuro": True, "jedi": False, "droide": False, "cazarrecompensas": False, "casco": True, "sith": True, "rebelde": False, "wookie": False},
    {"nombre": "Emperador Palpatine", "sable_luz": False, "humano": True, "lado_oscuro": True, "jedi": False, "droide": False, "cazarrecompensas": False, "casco": False, "sith": True, "rebelde": False, "wookie": False},
    {"nombre": "Mace Windu", "sable_luz": True, "humano": True, "lado_oscuro": False, "jedi": True, "droide": False, "cazarrecompensas": False, "casco": False, "sith": False, "rebelde": False, "wookie": False, "lider_batalla": True, "relacion_familiar": False},
    {"nombre": "Yoda", "sable_luz": True, "humano": False, "lado_oscuro": False, "jedi": True, "droide": False, "cazarrecompensas": False, "casco": False, "sith": False, "rebelde": False, "wookie": False},
    {"nombre": "Chewbacca", "sable_luz": False, "humano": False, "lado_oscuro": False, "jedi": False, "droide": False, "cazarrecompensas": False, "casco": False, "sith": False, "rebelde": True, "wookie": True},
    {"nombre": "Cad Bane", "sable_luz": False, "humano": False, "lado_oscuro": True, "jedi": False, "droide": False, "cazarrecompensas": True, "casco": True, "sith": False, "rebelde": False, "wookie": False},
    {"nombre": "Jango Fett", "sable_luz": False, "humano": True, "lado_oscuro": False, "jedi": False, "droide": False, "cazarrecompensas": True, "casco": True, "sith": False, "rebelde": False, "wookie": False},
    {"nombre": "R2-D2", "sable_luz": False, "humano": False, "lado_oscuro": False, "jedi": False, "droide": True, "cazarrecompensas": False, "casco": False, "sith": False, "rebelde": True, "wookie": False}
]

# Preguntas predefinidas basadas en las características
preguntas = [
    ("sable_luz", "¿El personaje tiene un sable de luz?"),
    ("humano", "¿El personaje es humano?"),
    ("lado_oscuro", "¿El personaje pertenece al lado oscuro?"),
    ("jedi", "¿El personaje es un Jedi?"),
    ("wookie", "¿El personaje es un Wookie?"),
    ("droide", "¿El personaje es un droide?"),
    ("cazarrecompensas", "¿El personaje es un cazarrecompensas?"),
    ("casco", "¿El personaje usa casco?"),
    ("sith", "¿El personaje es un Sith?"),
    ("rebelde", "¿El personaje pertenece a la Alianza Rebelde?"),
    ("lider_batalla", "¿El personaje ha liderado una batalla importante?"),  # Nueva pregunta
    ("relacion_familiar", "¿El personaje tiene una relación familiar con otro personaje importante?")  # Nueva pregunta
]

# Sistema para almacenar el aprendizaje
historial_aprendizaje = {"preguntas_utiles": {}, "respuestas_correctas": 0, "respuestas_erroneas": 0}

def inicializar_aprendizaje():
    for pregunta in preguntas:
        historial_aprendizaje["preguntas_utiles"][pregunta[1]] = 0

# Función que realiza el filtrado de personajes según las respuestas
def filtrar_personajes(personajes, caracteristica, respuesta):
    return [p for p in personajes if p[caracteristica] == respuesta]

# Función que aprende a hacer preguntas más útiles
def aprender_pregunta(pregunta, utilidad):
    historial_aprendizaje["preguntas_utiles"][pregunta] += utilidad

# Función para obtener la pregunta con mayor utilidad, sin repetir preguntas
def obtener_mejor_pregunta(preguntas_realizadas):
    preguntas_disponibles = {pregunta: utilidad for pregunta, utilidad in historial_aprendizaje["preguntas_utiles"].items() if pregunta not in preguntas_realizadas}
    if preguntas_disponibles:
        return max(preguntas_disponibles, key=preguntas_disponibles.get)
    return None

# Guardar la información de la partida en un archivo de texto
def guardar_informacion(personaje_adivinado, preguntas_realizadas):
    try:
        with open("historial_aprendizaje.txt", "a") as archivo:
            archivo.write(f"Personaje adivinado: {personaje_adivinado}\n")
            archivo.write("Preguntas realizadas:\n")
            for pregunta in preguntas_realizadas:
                archivo.write(f"- {pregunta}\n")
            archivo.write("\n")
        messagebox.showinfo("Información guardada", "La información ha sido guardada en el archivo 'historial_aprendizaje.txt'.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al guardar la información: {e}")

# Función principal del juego con GUI
class AdivinaPersonaje:
    def __init__(self, root):
        self.root = root
        self.root.title("Adivina el Personaje - Star Wars")
        self.personajes_restantes = personajes.copy()
        self.preguntas_realizadas = []
        self.mejor_pregunta = None

        # Mostrar personajes disponibles al inicio
        personajes_nombres = [p["nombre"] for p in personajes]
        messagebox.showinfo("Personajes disponibles", f"Personajes: {', '.join(personajes_nombres)}")

        # Interfaz
        self.label = tk.Label(root, text="Piensa en un personaje de Star Wars", font=("Arial", 14))
        self.label.pack(pady=20)

        # Cargar la imagen
        self.imagen = tk.PhotoImage(file=r"C:\Users\Axel\Desktop\Sistemas expertos\georgedroid.gif")  # Asegúrate de que la imagen está en formato GIF
        self.imagen_label = tk.Label(root, image=self.imagen)
        self.imagen_label.pack(pady=10)

        self.pregunta_label = tk.Label(root, text="", font=("Arial", 12))
        self.pregunta_label.pack(pady=10)

        self.si_button = tk.Button(root, text="Sí", command=self.responder_si)
        self.no_button = tk.Button(root, text="No", command=self.responder_no)
        self.si_button.pack(side="left", padx=20, pady=10)
        self.no_button.pack(side="right", padx=20, pady=10)

        self.siguiente_pregunta()

    def siguiente_pregunta(self):
        self.mejor_pregunta = obtener_mejor_pregunta(self.preguntas_realizadas)
        if self.mejor_pregunta:
            self.pregunta_label.config(text=self.mejor_pregunta)
        else:
            self.finalizar_juego()  # Esto se asegura de que terminemos el juego si no quedan preguntas

    def responder_si(self):
        self.responder(True)

    def responder_no(self):
        self.responder(False)

    def responder(self, respuesta):
        for caracteristica, pregunta in preguntas:
            if pregunta == self.mejor_pregunta:
                self.personajes_restantes = filtrar_personajes(self.personajes_restantes, caracteristica, respuesta)
                break
        
        self.preguntas_realizadas.append(self.mejor_pregunta)
        if len(self.personajes_restantes) == 1:
            personaje_adivinado = self.personajes_restantes[0]["nombre"]
            messagebox.showinfo("Adivinanza", f"¡He adivinado! El personaje es: {personaje_adivinado}")
            guardar_informacion(personaje_adivinado, self.preguntas_realizadas)
            self.root.quit()
        else:
            self.siguiente_pregunta()

# Inicializar y ejecutar la aplicación
if __name__ == "__main__":
    inicializar_aprendizaje()
    root = tk.Tk()
    app = AdivinaPersonaje(root)
    root.mainloop()
