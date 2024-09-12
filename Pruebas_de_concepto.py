import tkinter as tk
from tkinter import ttk
import time
import threading

def cargar():
    # Función para simular carga y mostrar mensajes
    for i in range(3):
        time.sleep(3.33)  # Espera 3.33 segundos (10 segundos / 3 mensajes)
        progreso.set((i + 1) * 33)  # Actualiza la barra de progreso
        mensaje_label.config(text=mensajes[i])  # Actualiza el mensaje
        ventana.update_idletasks()  # Actualiza la interfaz gráfica

def iniciar_carga():
    # Inicia la barra de carga en un hilo separado
    threading.Thread(target=cargar).start()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title('Barra de Carga')
ventana.geometry('400x200')

# Crear la barra de progreso
progreso = tk.DoubleVar()
barra_progreso = ttk.Progressbar(ventana, orient="horizontal", length=300, mode="determinate", variable=progreso)
barra_progreso.pack(pady=20)

# Crear una etiqueta para mostrar mensajes
mensaje_label = tk.Label(ventana, text="Preparando...", font=("Arial", 14))
mensaje_label.pack(pady=10)

# Mensajes que se mostrarán durante la carga
mensajes = [
    "Cargando, por favor espere...",
    "Aún cargando, no cierre la aplicación.",
    "Casi listo, un momento más..."
]

# Botón para iniciar la carga
boton_iniciar = tk.Button(ventana, text="Iniciar Carga", command=iniciar_carga)
boton_iniciar.pack(pady=10)

ventana.mainloop()
