import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import calendar
from datetime import datetime

provincias_argentinas = [
    "Buenos Aires", "Catamarca", "Chaco", "Chubut", "Córdoba", "Corrientes",
    "Entre Ríos", "Formosa", "Jujuy", "La Pampa", "La Rioja", "Mendoza",
    "Misiones", "Neuquén", "Río Negro", "Salta", "San Juan", "San Luis",
    "Santa Cruz", "Santa Fe", "Santiago del Estero", "Tierra del Fuego",
    "Tucumán"
]

provincias_precios = [
    "10000", "10100", "10200", "10300", "10400", "10500",
    "10600", "10600", "10700", "10800", "10900", "11000",
    "11100", "11200", "11300", "11400", "11500", "11600",
    "11700", "11800", "11900", "12000",
    "12100"
]

meses = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
]

datos = None  # Variable global para almacenar la clase Datos

# Clase Datos global
class Datos:
    def __init__(self):
        self.nombre = ""
        self.dni = ""
        self.email = ""
        self.provincia = ""
        self.precio = ""

# Inicializamos la clase Datos de forma global
def inicializar_datos():
    global datos
    datos = Datos()

# Declaramos globales y funciones que necesiten acceso a variables globales
def guardar_datos(entrada1, entrada2, entrada3):
    global datos
    datos.nombre = entrada1.get()
    datos.dni = entrada2.get()
    datos.email = entrada3.get()

# Función para mostrar la ventana principal
def mostrar_ventana_principal():
    global ventana, provincias_con_precios, destinos, lista, mes, dia, dia_comprado, mes_comprado,imagen_logo, imagen_fondo

    ventana = tk.Tk()
    ventana.title('Aeroline.ARG')
    ventana.geometry('1200x700') 

    
    
    # Definimos más variables globales necesarias para el funcionamiento
    provincias_con_precios = list(zip(provincias_argentinas, provincias_precios))
    destinos = []
    mes = ''
    dia = ''
    dia_comprado = ''
    mes_comprado = ''

    # Aquí puedes continuar con las configuraciones de la ventana principal, botones, etiquetas, etc.
    
    Fondo_principal()
    creando_frames()

    logotipo()
    imagen_informacion()
    Ingresado_informacion()

    #carga de los widgets
    Scrollbar()

    ventana.mainloop()

def creando_frames():
    # Global para evitar que las imágenes se destruyan

    #-------------------------------------------------------------------------------------------------------------
    #                   aqui creamos los Frames para meter la estrutura del programa donde queremos con place
    #-------------------------------------------------------------------------------------------------------------
    global style,marco_formulario,marco_formulario2,marco_formulario3,marco_formulario4,marco_formulario5,marco_logotipo
    style = ttk.Style() #definimos el estilo
    style.configure("Transparent.TLabel", background="#fcfefb", foreground="black") 

    #----------------------------------------------------------------------------------marco para los cuadraditos
    marco_logotipo = ttk.Frame(ventana, style="Transparent.TLabel")
    marco_logotipo.place(relx=0.22, rely=0.22, anchor="center", width=500, height=300)

    marco_formulario = ttk.Frame(ventana, style="Transparent.TLabel")
    marco_formulario.place(relx=0.18, rely=0.3, anchor="center", width=450, height=200)

    marco_formulario2 = ttk.Frame(ventana, style="Transparent.TLabel")
    marco_formulario2.place(relx=0.35, rely=0.28, anchor="center", width=200, height=200)

    marco_formulario3 = ttk.Frame(ventana, style="Transparent.TLabel")
    marco_formulario3.place(relx=0.23, rely=0.7, anchor="center", width=450, height=350)

    marco_formulario4 = ttk.Frame(ventana, style="Transparent.TLabel")
    marco_formulario4.place(relx=0.5, rely=0.2, anchor="center", width=150, height=150)

    marco_formulario5 = ttk.Frame(ventana, style="Transparent.TLabel")
    marco_formulario5.place(relx=0.53, rely=0.26, anchor="center", width=310, height=215)



def Fondo_principal():
    global image_path, image, background_image
    image_path = "file/image.png"
    image = Image.open(image_path)
    background_image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(ventana, width=900, height=700)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_image, anchor="nw")

    return background_image



def logotipo():
    #-------------------------------------------------------------------------------------------------------------
    #                           EL Laber que contiene la primera imagen (logo)
    #-------------------------------------------------------------------------------------------------------------
    # Cargar la imagen (logo)
    global image_path, imagen_logo, label_logo

    image_path = "file/logo.jpg"  # Reemplaza con la ruta correcta de tu logo
    imagen_logo = Image.open(image_path)
    imagen_logo = imagen_logo.resize((420, 80))  # Redimensiona la imagen si es necesario
    imagen_logo = ImageTk.PhotoImage(imagen_logo)

    # Crear un Label para mostrar la imagen
    label_logo = tk.Label(marco_logotipo, image=imagen_logo)
    label_logo.grid(row=0, column=0, padx=10, pady=10)

    return label_logo

        
def imagen_informacion():
    #-------------------------------------------------------------------------------------------------------------
    #                           EL Laber que contiene la segunda imagen (fondo)
    #-------------------------------------------------------------------------------------------------------------
    # Cargar la imagen (fondo)
    global image_path, imagen_fondo, label_fondo
    image_path = "file/background_m2.jpg"  # Ruta de la imagen
    imagen_fondo = Image.open(image_path)
    imagen_fondo = imagen_fondo.resize((450, 350))
    imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

    # Crear el Frame y el Label para la Imagen:
    label_fondo = tk.Label(marco_formulario3, image=imagen_fondo)
    label_fondo.place(relx=0, rely=0, relwidth=1, relheight=1)

    labels_informacion()

    return label_fondo


def labels_informacion():
    global info_label, info_label2
    info_label = tk.Label(marco_formulario3, text="Seleccione la provincia", background="#8ed0dc", width=30)
    info_label.pack(padx=5, pady=15, anchor='w')
    info_label2 = tk.Label(marco_formulario3, text="Aeropuertos", font=("Arial", 15),width=20, background="#89cfdb")
    info_label2.pack(padx=8, pady=110, anchor='w')


    



def Ingresado_informacion():
    #-------------------------------------------------------------------------------------------------------------
    #                                           Ingresamos los Label y Entry
    #-------------------------------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------Retornar la instancia creada
    # ---------------------------------------------------------------------------------Para la seccion de logeo
    
    ttk.Label(marco_formulario, text="Nombre:", style="Transparent.TLabel").grid(row=1, column=0, padx=15, pady=2, sticky='e')
    entrada1 = ttk.Entry(marco_formulario)
    entrada1.grid(row=1, column=1, padx=5, pady=2, sticky='ew')
    
    
    ttk.Label(marco_formulario, text="DNI:", style="Transparent.TLabel").grid(row=2, column=0, padx=15, pady=2, sticky='e')
    entrada2 = ttk.Entry(marco_formulario)
    entrada2.grid(row=2, column=1, padx=5, pady=2, sticky='ew')
    
    
    ttk.Label(marco_formulario, text="Correo Electronico:", style="Transparent.TLabel").grid(row=3, column=0, padx=15, pady=2, sticky='e')
    entrada3 = ttk.Entry(marco_formulario)
    entrada3.grid(row=3, column=1, padx=5, pady=2, sticky='ew')
    
    
    ttk.Label(marco_formulario, text="N/T:", style="Transparent.TLabel").grid(row=4, column=0, padx=15, pady=2, sticky='e')
    entrada4 = ttk.Entry(marco_formulario)
    entrada4.grid(row=4, column=1, padx=5, pady=2, sticky='ew')
    

    ttk.Label(marco_formulario, text="CVV:", style="Transparent.TLabel").grid(row=5, column=0, padx=15, pady=2, sticky='e')
    entrada5 = ttk.Entry(marco_formulario)
    entrada5.grid(row=5, column=1, padx=5, pady=2, sticky='ew')
    
    ttk.Label(marco_formulario, text="Fecha:", style="Transparent.TLabel").grid(row=6, column=0, padx=15, pady=2, sticky='e')
    info_label3 = tk.Label(marco_formulario, text="Seleccionar Fecha") #widget
    info_label3.grid(row=6, column=1, padx=5, pady=2, sticky='ew')

    guardar_datos(entrada1, entrada2, entrada3)
    


#dentro de la ventana informacion creamos unos labels que nos permiten mostrar la informacion para el usuario




def Scrollbar():
    global destino, lista, scrollbar

    marco_lista = tk.Frame(marco_formulario2)
    marco_lista.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='w')

    scrollbar = tk.Scrollbar(marco_lista)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    lista = tk.Listbox(marco_lista, yscrollcommand=scrollbar.set)
    lista.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    for provincia in provincias_argentinas:
        lista.insert(tk.END, provincia)

    scrollbar.config(command=lista.yview)

    def on_select(event): #como es un click se define como evento
        seleccion_index = lista.curselection() #lista.curselection() me permite saber si le dimos click
        if seleccion_index:                     #ahora que le diste click nos da la infomacion de la seleccion
            seleccion = seleccion_index[0]      #donde le diste click lo guarda en seleccion, iniciando desde 0
            provincia, precio = provincias_con_precios[seleccion] #luego busca la provincia y su precio segun tu seleccion
            mostrar_informacion(provincia, precio)                 #nos deja la informacion en mostrar informacion
            destino = (provincia, precio) #guardo la tupla
            destinos.append(destino) #agrego el destino

    ##----------------------------------------chatgpt no sabia
    lista.bind('<<ListboxSelect>>', on_select)#vincula la el clicl con la lista
    datos.provincia = provincia

def mostrar_informacion(provincia, precios):
    info_label.config(text=f"Precio del vuelos ${precios}")
    info_label2.config(text=f"{provincia}")















def __init__():
    inicializar_datos()
    mostrar_ventana_principal()




__init__()










