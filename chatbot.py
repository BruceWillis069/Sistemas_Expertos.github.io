import sqlite3

print('hola como estas de que te gustaria hablar?')
# Conectar a la base de datos (se crea si no existe)
conn = sqlite3.connect('chatbot.db')
c = conn.cursor()

# Crear una tabla para almacenar respuestas si no existe
c.execute('''CREATE TABLE IF NOT EXISTS responses (
                user_input TEXT PRIMARY KEY, 
                bot_response TEXT)''')

conn.commit()

# Función para buscar respuestas en la base de datos
def find_response(user_input):
    c.execute("SELECT bot_response FROM responses WHERE user_input = ?", (user_input,))
    result = c.fetchone()
    if result:
        return result[0]  # Retornar la respuesta del bot
    else:
        return None

# Función para agregar una nueva respuesta a la base de datos
def add_response(user_input, bot_response):
    try:
        c.execute("INSERT INTO responses (user_input, bot_response) VALUES (?, ?)", (user_input, bot_response))
        conn.commit()
    except sqlite3.IntegrityError:
        print("Ya existe una respuesta para esa entrada.")

# Función del chat
def chat(user_input):
    # Convertir input del usuario a minúsculas
    user_input = user_input.lower()

    # Buscar respuesta en la base de datos
    response = find_response(user_input)
    
    if response:
        return response
    else:
        # Si no encuentra respuesta, solicitar al usuario más información
        new_question = "No entiendo eso aún. ¿Qué debería responder a eso?"
        print("Bot:", new_question)
        new_response = input("Tú: ")
        
        # Almacenar la nueva respuesta en la base de datos
        add_response(user_input, new_response)
        return "Gracias, lo recordaré para la próxima vez."

# Ciclo de conversación
while True:
    user_input = input("Tú: ")
    if user_input.lower() == "salir":
        print("Bot: ¡Hasta luego!")
        break

    response = chat(user_input)
    print("Bot:", response)

# Cerrar la conexión a la base de datos cuando termine el programa
conn.close()
