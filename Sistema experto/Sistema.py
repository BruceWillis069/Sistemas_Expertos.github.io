import tkinter as tk
from tkinter import ttk, messagebox
import json

# Cargar la base de datos de juegos
def cargar_base_datos():
    try:
        with open("juegos.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Motor de inferencia para recomendar juegos
def recomendar_juegos(edad, caracteristicas, base_datos):
    recomendaciones = []
    for juego in base_datos:
        puntuacion = 0
        for caracteristica, valor in caracteristicas.items():
            if caracteristica == "plataforma" and valor not in juego.get("plataformas", []):
                puntuacion = 0  # Descartar si la plataforma no coincide
                break
            elif caracteristica == "categoria":
                if valor in juego.get("categorias", []):
                    puntuacion += 3  # Coincidencia exacta
                else:
                    puntuacion += 1  # Coincidencia parcial
            elif valor in juego.get(caracteristica, []):
                puntuacion += 3
        if puntuacion > 0 and juego["edad_minima"] <= edad <= juego["edad_maxima"]:
            puntuacion += 3
        if puntuacion > 0:
            recomendaciones.append((juego, puntuacion))
    recomendaciones.sort(key=lambda x: x[1], reverse=True)
    return [rec[0]["nombre"] for rec in recomendaciones]

# Función para mostrar la pantalla de recomendaciones
def pantalla_recomendaciones():
    ventana_rec = tk.Toplevel(root)
    ventana_rec.title("Recomendador de Juegos")
    ventana_rec.geometry("600x700+100+50")
    ventana_rec.configure(bg="#101010")

    tk.Label(ventana_rec, text="=== RECOMENDADOR DE JUEGOS ===", font=("Courier", 16, "bold"), bg="#101010", fg="#33FF33").pack(pady=20)

    frame_form = tk.Frame(ventana_rec, bg="#101010")
    frame_form.pack(pady=10)

    ttk.Label(frame_form, text="NOMBRE DE USUARIO:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
    entry_usuario = ttk.Entry(frame_form, width=30)
    entry_usuario.grid(row=0, column=1, padx=10, pady=5)

    ttk.Label(frame_form, text="EDAD:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
    entry_edad = ttk.Entry(frame_form, width=30)
    entry_edad.grid(row=1, column=1, padx=10, pady=5)

    preguntas = {
        "CATEGORÍA:": ["Acción", "Aventura", "Rol", "Estrategia", "Deportes", "Simulación", "Terror", "Casual"],
        "DURACIÓN:": ["Corta", "Media", "Larga"],
        "DIFICULTAD:": ["Fácil", "Intermedia", "Difícil"],
        "PLATAFORMA:": ["PC", "PlayStation", "Xbox", "Nintendo Switch", "Móvil"],
        "MULTIJUGADOR:": ["Sí", "No"],
        "VIOLENCIA:": ["Alta", "Moderada", "Baja"],
        "DOBLAJE AL ESPAÑOL:": ["Sí", "No"],
        "GRÁFICOS:": ["Excelentes", "Buenos", "Aceptables"],
        "REJUGABILIDAD:": ["Alta", "Moderada", "Baja"]
    }

    combos = {}
    row = 2
    for pregunta, opciones in preguntas.items():
        ttk.Label(frame_form, text=pregunta).grid(row=row, column=0, sticky="w", padx=10, pady=5)
        combo = ttk.Combobox(frame_form, state="readonly", values=opciones)
        combo.grid(row=row, column=1, padx=10, pady=5)
        combos[pregunta] = combo
        row += 1

    def procesar_recomendacion():
        usuario = entry_usuario.get().strip()
        edad_str = entry_edad.get().strip()
        caracteristicas = {
            "categoria": combos["CATEGORÍA:"].get(),
            "duracion": combos["DURACIÓN:"].get(),
            "dificultad": combos["DIFICULTAD:"].get(),
            "plataforma": combos["PLATAFORMA:"].get(),
            "multijugador": combos["MULTIJUGADOR:"].get(),
            "violencia": combos["VIOLENCIA:"].get(),
            "doblaje": combos["DOBLAJE AL ESPAÑOL:"].get(),
            "graficos": combos["GRÁFICOS:"].get(),
            "rejugabilidad": combos["REJUGABILIDAD:"].get()
        }

        if not usuario or not edad_str or not all(caracteristicas.values()):
            messagebox.showerror("Error", "Por favor, completa todos los campos antes de continuar.")
            return

        try:
            edad = int(edad_str)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa una edad válida.")
            return

        recomendaciones = recomendar_juegos(edad, caracteristicas, base_datos)

        if recomendaciones:
            texto_recomendaciones = "\n".join(recomendaciones[:3])
            messagebox.showinfo("Recomendaciones", f"¡Hola {usuario}!\nTe recomendamos:\n\n{texto_recomendaciones}")
        else:
            messagebox.showinfo("Recomendaciones", f"¡Hola {usuario}!\nNo encontramos juegos que coincidan con tus preferencias estrictas. Intenta nuevamente.")

    ttk.Button(ventana_rec, text="GENERAR RECOMENDACIONES", command=procesar_recomendacion).pack(pady=20)

# Pantalla para mostrar juegos GOTY
def pantalla_goty():
    ventana_goty = tk.Toplevel(root)
    ventana_goty.title("Juegos GOTY")
    ventana_goty.geometry("500x400+120+70")
    ventana_goty.configure(bg="#101010")

    tk.Label(ventana_goty, text="=== JUEGOS GANADORES DE GOTY ===", font=("Courier", 14, "bold"), bg="#101010", fg="#33FF33").pack(pady=10)

    goty_juegos = [
        "The Legend of Zelda: Breath of the Wild",
        "The Last of Us Part II",
        "God of War",
        "Elden Ring",
        "Sekiro: Shadows Die Twice",
    ]

    for juego in goty_juegos:
        tk.Label(ventana_goty, text=juego, font=("Courier", 12), bg="#101010", fg="#33FF33").pack(pady=5)

# Pantalla para mostrar sagas populares
def pantalla_sagas():
    ventana_sagas = tk.Toplevel(root)
    ventana_sagas.title("Sagas Populares")
    ventana_sagas.geometry("600x500+140+80")
    ventana_sagas.configure(bg="#101010")

    tk.Label(ventana_sagas, text="=== SAGAS POPULARES ===", font=("Courier", 14, "bold"), bg="#101010", fg="#33FF33").pack(pady=10)

    sagas = {
        "The Legend of Zelda": [
        "The Legend of Zelda (1986)",
        "Zelda II: The Adventure of Link (1987)",
        "A Link to the Past (1991)",
        "Link's Awakening (1993)",
        "Ocarina of Time (1998)",
        "Majora's Mask (2000)",
        "Oracle of Seasons (2001)",
        "Oracle of Ages (2001)",
        "Four Swords (2002)",
        "The Wind Waker (2002)",
        "Four Swords Adventures (2004)",
        "The Minish Cap (2004)",
        "Twilight Princess (2006)",
        "Phantom Hourglass (2007)",
        "Spirit Tracks (2009)",
        "Skyward Sword (2011)",
        "A Link Between Worlds (2013)",
        "Tri Force Heroes (2015)",
        "Breath of the Wild (2017)",
        "Tears of the Kingdom (2023)"],
        "Assassin's Creed": [
        "Assassin's Creed (2007)",
        "Assassin's Creed II (2009)",
        "Assassin's Creed: Brotherhood (2010)",
        "Assassin's Creed: Revelations (2011)",
        "Assassin's Creed III (2012)",
        "Assassin's Creed IV: Black Flag (2013)",
        "Assassin's Creed: Rogue (2014)",
        "Assassin's Creed: Unity (2014)",
        "Assassin's Creed: Syndicate (2015)",
        "Assassin's Creed: Origins (2017)",
        "Assassin's Creed: Odyssey (2018)",
        "Assassin's Creed: Valhalla (2020)"],
        "Final Fantasy": [
        "Final Fantasy (1987)",
        "Final Fantasy II (1988)",
        "Final Fantasy III (1990)",
        "Final Fantasy IV (1991)",
        "Final Fantasy V (1992)",
        "Final Fantasy VI (1994)",
        "Final Fantasy VII (1997)",
        "Final Fantasy VIII (1999)",
        "Final Fantasy IX (2000)",
        "Final Fantasy X (2001)",
        "Final Fantasy XI (2002)",
        "Final Fantasy XII (2006)",
        "Final Fantasy XIII (2009)",
        "Final Fantasy XIV (2010)",
        "Final Fantasy XV (2016)",
        "Final Fantasy XVI (2023)"],
        "The Elder Scrolls": [
        "The Elder Scrolls: Arena (1994)",
        "The Elder Scrolls II: Daggerfall (1996)",
        "The Elder Scrolls III: Morrowind (2002)",
        "The Elder Scrolls IV: Oblivion (2006)",
        "The Elder Scrolls V: Skyrim (2011)"],
        "Mass Effect": ["Mass Effect 1", "Mass Effect 2", "Mass Effect 3", "Andromeda"]
      }

    def mostrar_juegos(saga):
        juegos = "\n".join(sagas[saga])
        messagebox.showinfo(f"Juegos de {saga}", f"{saga} incluye:\n\n{juegos}")

    for saga, juegos in sagas.items():
        ttk.Button(ventana_sagas, text=saga, command=lambda s=saga: mostrar_juegos(s)).pack(pady=10)

# Pantalla principal
root = tk.Tk()
root.title("Computadora Retrofuturista")
root.geometry("800x600")
root.configure(bg="#101010")

tk.Label(root, text="=== SISTEMA RETROFUTURISTA ===", font=("Courier", 16, "bold"), bg="#101010", fg="#33FF33").pack(pady=20)

ttk.Button(root, text="Recomendar Juegos", command=pantalla_recomendaciones).pack(pady=10)
ttk.Button(root, text="Ver Juegos GOTY", command=pantalla_goty).pack(pady=10)
ttk.Button(root, text="Sagas Populares", command=pantalla_sagas).pack(pady=10)

# Botón para salir
ttk.Button(root, text="Salir", command=root.quit).pack(pady=10)

base_datos = cargar_base_datos()
root.mainloop()
