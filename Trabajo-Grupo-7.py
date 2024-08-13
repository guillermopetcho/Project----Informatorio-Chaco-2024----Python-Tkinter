import tkinter as tk
from tkinter import ttk
from tkinter import *


#definimos las listas
provincias_argentinas = [
    "Buenos Aires", "Catamarca", "Chaco", "Chubut", "Córdoba", "Corrientes",
    "Entre Ríos", "Formosa", "Jujuy", "La Pampa", "La Rioja", "Mendoza",
    "Misiones", "Neuquén", "Río Negro", "Salta", "San Juan", "San Luis",
    "Santa Cruz", "Santa Fe", "Santiago del Estero", "Tierra del Fuego",
    "Tucumán"
]

#ventana de compra realizada
def compra_realizada():
    venta_completada = tk.Toplevel()
    venta_completada.title('Información de la compra')
    venta_completada.geometry('450x450')

    etiqueta_bienvenida = tk.Label(venta_completada, text="¡Compra completada!")
    etiqueta_bienvenida.pack(pady=20)

    boton_continuar = tk.Button(venta_completada, text="Continuar", command=venta_completada.destroy)
    boton_continuar.pack(pady=20)

#definimos la ventana principal

def mostrar_ventana_principal():
    
   
    ventana = tk.Tk()
    ventana.title('Aeroline.ARG')
    ventana.geometry('900x500') 
    
    #grid
    #explicacion del uso
    """asegura q las columnas se expandan proporcionalmente si se redimensiona la ventana"""
    ventana.columnconfigure(0, weight=1)
    ventana.columnconfigure(1, weight=1)

    
    #entrada

    #posicionamiento de los label con grid
    #filas (abajo) 0 - 1 - 2 - 3 - 4 con pad 5

    """sticky='e' (este) y sticky='w' (oeste) 
    en grid alinea los widgets en las celdas de la cuadricula"""
    #creamos la seccion de logeo
    
    tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=10, pady=5, sticky='nsw')
    entry1 = tk.Entry(ventana)
    entry1.grid(row=0, column=1, padx=2, pady=5, sticky='nw')

    tk.Label(ventana, text="Apellido:").grid(row=1, column=0, padx=10, pady=5, sticky='nsw')
    entry2 = tk.Entry(ventana)
    entry2.grid(row=1, column=1, padx=2, pady=5, sticky='nw')

    tk.Label(ventana, text="DNI:").grid(row=2, column=0, padx=10, pady=5, sticky='nsw')
    entry3 = tk.Entry(ventana)
    entry3.grid(row=2, column=1, padx=2, pady=5, sticky='nw')

    tk.Label(ventana, text="Correo Electrónico:").grid(row=3, column=0, padx=10, pady=5, sticky='nsw')
    entry4 = tk.Entry(ventana)
    entry4.grid(row=3, column=1, padx=2, pady=5, sticky='nw')


    ##separamos
    separator_h = tk.Frame(ventana, bg="black", height=2)
    separator_h.grid(row=5, column=0, columnspan=2, sticky='ew')

    # el marco para la lista de provincias
    marco = tk.Frame(ventana)
    marco.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky='n')

    scrollbar = tk.Scrollbar(marco)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    lista = tk.Listbox(marco, yscrollcommand=scrollbar.set)
    for provincia in provincias_argentinas:
        lista.insert(tk.END, provincia)
    lista.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar.config(command=lista.yview)

    info_label = tk.Label(ventana, text="")
    info_label.grid(row=6, column=0, columnspan=2, padx=10, pady=20, sticky='w')

    def on_select(event):
        seleccion = lista.get(lista.curselection())
        mostrar_informacion(seleccion)

    lista.bind('<<ListboxSelect>>', on_select)

    def mostrar_informacion(provincia):
        """Función para mostrar información sobre la provincia seleccionada."""
        info_label.config(text=f"Información sobre {provincia}: Aquí puedes agregar detalles interesantes.")

    # Botones
    boton_comprar = tk.Button(ventana, text="Comprar", command=compra_realizada)
    boton_comprar.grid(row=9, column=0, padx=10, pady=5)

    boton_volver = tk.Button(ventana, text="Volver", command=ventana.destroy)
    boton_volver.grid(row=9, column=1, padx=10, pady=5)

    ventana.mainloop()

# llamada a funcion
mostrar_ventana_principal()


"""
Valores Comunes de sticky
    sticky='n': Alinea el widget al borde norte (superior) de la celda.
    sticky='e': Alinea el widget al borde este (derecho) de la celda.
    sticky='s': Alinea el widget al borde sur (inferior) de la celda.
    sticky='w': Alinea el widget al borde oeste (izquierdo) de la celda.
    sticky='ne': Alinea el widget en la esquina noreste (superior derecha) de la celda.
    sticky='sw': Alinea el widget en la esquina suroeste (inferior izquierda) de la celda.
    sticky='ns': Expande el widget verticalmente para llenar toda la altura de la celda.
    sticky='ew': Expande el widget horizontalmente para llenar toda la anchura de la celda.
    sticky='nsew': Expande el widget para llenar toda la celda, tanto horizontal como verticalmente.
"""