
import tkinter as tk
import random

# Lista de palabras para el juego
palabras = ["python", "java", "programacion", "tkinter", "desarrollador", "algoritmo"]

# Función para iniciar el juego
def iniciar_juego():
    global palabra_secreta, palabra_guiones, intentos, letras_usadas
    palabra_secreta = random.choice(palabras)  # Escoge una palabra aleatoria
    palabra_guiones = ["_"] * len(palabra_secreta)  # Inicializa la palabra con guiones
    intentos = 6  # Número de intentos
    letras_usadas = []  # Lista de letras que ya han sido usadas
    etiqueta_palabra.config(text=" ".join(palabra_guiones))
    etiqueta_intentos.config(text=f"Intentos restantes: {intentos}")
    etiqueta_letras_usadas.config(text="Letras usadas: ")
    entrada_letra.delete(0, tk.END)
    etiqueta_mensaje.config(text="¡Empieza a adivinar!")

# Función que se ejecuta cuando el jugador ingresa una letra
def adivinar():
    global palabra_guiones, intentos, letras_usadas
    letra = entrada_letra.get().lower()

    if letra in letras_usadas:
        etiqueta_mensaje.config(text="Ya has usado esa letra.")
        return
    if len(letra) != 1 or not letra.isalpha():
        etiqueta_mensaje.config(text="Por favor, ingresa solo una letra.")
        return

    letras_usadas.append(letra)

    if letra in palabra_secreta:
        # Reemplazar los guiones por la letra en la palabra secreta
        for i in range(len(palabra_secreta)):
            if palabra_secreta[i] == letra:
                palabra_guiones[i] = letra
        etiqueta_palabra.config(text=" ".join(palabra_guiones))
    else:
        intentos -= 1
        etiqueta_intentos.config(text=f"Intentos restantes: {intentos}")

    etiqueta_letras_usadas.config(text=f"Letras usadas: {', '.join(letras_usadas)}")

    # Verificar si el jugador ha ganado o perdido
    if "_" not in palabra_guiones:
        etiqueta_mensaje.config(text="¡Has ganado!")
    elif intentos == 0:
        etiqueta_mensaje.config(text=f"¡Perdiste! La palabra era: {palabra_secreta}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Juego de Ahorcado")

# Etiquetas
etiqueta_titulo = tk.Label(ventana, text="¡Juego de Ahorcado!", font=("Arial", 20))
etiqueta_titulo.pack(pady=10)

etiqueta_palabra = tk.Label(ventana, text="_ " * 6, font=("Arial", 18))
etiqueta_palabra.pack(pady=10)

etiqueta_intentos = tk.Label(ventana, text="Intentos restantes: 6", font=("Arial", 14))
etiqueta_intentos.pack(pady=5)

etiqueta_letras_usadas = tk.Label(ventana, text="Letras usadas: ", font=("Arial", 12))
etiqueta_letras_usadas.pack(pady=5)

entrada_letra = tk.Entry(ventana, font=("Arial", 14), width=5)
entrada_letra.pack(pady=5)

boton_adivinar = tk.Button(ventana, text="Adivinar", font=("Arial", 14), command=adivinar)
boton_adivinar.pack(pady=10)

boton_iniciar = tk.Button(ventana, text="Iniciar Nuevo Juego", font=("Arial", 14), command=iniciar_juego)
boton_iniciar.pack(pady=10)

etiqueta_mensaje = tk.Label(ventana, text="", font=("Arial", 14))
etiqueta_mensaje.pack(pady=10)

# Iniciar el juego al abrir la ventana
iniciar_juego()

# Ejecutar la ventana
ventana.mainloop()
