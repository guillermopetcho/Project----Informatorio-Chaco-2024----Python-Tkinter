from Grupo_7_Proyecto import *


import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import calendar
from datetime import datetime



def compra_realizada(datos):
    venta_completada = tk.Toplevel()
    venta_completada.title('Informacion del Ticket')
    venta_completada.geometry('400x250')

    # Utiliza el atributo 'nombre' de la instancia 'usuario_creado'
    etiqueta_bienvenida = tk.Label(venta_completada, text=f"¡Compra completada {datos.nombre}!")
    etiqueta_bienvenida.pack(pady=20)
    

    etiqueta_bienvenida2 = tk.Label(venta_completada, text=f"La fecha del viaje: {datos.mes_comprado}, {datos.dia_comprado} \n Su ID de compra es: \n")
    etiqueta_bienvenida2.pack(pady=20)

    """etiqueta_bienvenida3 = tk.Label(venta_completada, text=f"Destino: ")
    etiqueta_bienvenida3.pack(pady=20)"""

    boton_continuar = tk.Button(venta_completada, text="Continuar", command=venta_completada.destroy)
    boton_continuar.pack(pady=20)


def compra_error(mensajes_error):
    venta_error = tk.Toplevel()
    venta_error.title('¡Error al completar los datos!')
    venta_error.geometry('400x250')

    for mensaje in mensajes_error:
        etiqueta_bienvenida = tk.Label(venta_error, text=mensaje)
        etiqueta_bienvenida.pack(pady=15, anchor="center")

    boton_continuar = tk.Button(venta_error, text="Continuar", command=venta_error.destroy)
    boton_continuar.pack(pady=20)

