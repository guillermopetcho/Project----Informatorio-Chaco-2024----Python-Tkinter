import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import calendar
from datetime import datetime



from Grupo_7_Proyecto import *


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
    def __init__(self): # constructor
        self.nombre = "" #atributo publico
        self._dni = "" #atributo protegido
        self.email = ""
        self.provincia = ""
        self.precio = ""
        self.__code = ""#atributo privado
        self.__cvv = ""
        self.dia_comprado = ""
        self.mes_comprado = ""
        self.id_comprado = ""

# Inicializamos la clase Datos de forma global
def inicializar_datos(): # constructor de la clase que inicializa los datos de forma global con la instancia datos
    global datos
    datos = Datos()


def guardar_datos(entrada1, entrada2, entrada3, entrada4, entrada5, datos):
    datos.nombre = entrada1.get()
    datos._dni = entrada2.get()
    datos.email = entrada3.get()
    datos.__code = entrada4.get()
    datos.__cvv = entrada5.get()




def validar_entradas(entrada1, entrada2, entrada3, entrada4, entrada5, datos):

    entradas = [
        entrada1.get(), entrada2.get(), entrada3.get(), 
        entrada4.get(), entrada5.get(),datos.dia_comprado
    ]

    errores = [
        "Ingresar nombre",
        "Ingresar _DNI",
        "Ingresar Email",
        "Ingresar N/T",
        "Ingresar CVV",
        "Ingresar Fecha"
    ]
    
    #flagse = [entrada == "" for entrada in entradas]

    flagse = []  # Creamos una lista vacia para almacenar los resultados

    for entrada in entradas: #recorremos la lista de entradas  
        if entrada == "":  # Si la entrada es vacia
            flagse.append(True) # Agregamos True a la lista  
        else:
            flagse.append(False) # Agregamos False a la lista


    #mensajes_error = [errores[i] for i, flag in enumerate(flagse) if flag]
    global mensajes_error
    mensajes_error = []  

    for i, flag in enumerate(flagse):  
        if flag:  
            mensajes_error.append(errores[i])# Si la entrada es vacia, agrega el error correspondiente
    return mensajes_error #devuelve el resultado de la operacion




#generador de id

def generar_id(datos):
    global num_id
    datos.id_comprado = num_id
    num_id += 1
    return datos.id_comprado
    

def Fondo_principal(ventana):
    global image_path, image, background_image
    image_path = "file/image.png"
    image = Image.open(image_path)
    background_image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(ventana, width=900, height=700)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_image, anchor="nw")

    return background_image



def logotipo(marco_logotipo):
    #-------------------------------------------------------------------------------------------------------------
    #                           EL Laber que contiene la primera imagen (logo)
    #-------------------------------------------------------------------------------------------------------------
    # cargar la imagen (logo)
    global image_path, imagen_logo, label_logo

    image_path = "file/logo.jpg"  # reemplaza con la ruta correcta de tu logo
    imagen_logo = Image.open(image_path)
    imagen_logo = imagen_logo.resize((420, 80))  # redimensiona la imagen si es necesario
    imagen_logo = ImageTk.PhotoImage(imagen_logo)

    # Crear un Label para mostrar la imagen
    label_logo = tk.Label(marco_logotipo, image=imagen_logo)
    label_logo.grid(row=0, column=0, padx=10, pady=10)

    return label_logo

        
def imagen_informacion(marco_formulario3):
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

    
    return label_fondo



"""def primer_cambio(dia,dia2,var):
    if dia == '' and var.get() != 'Elegir':
        seleccionador_fechas(dia,dia2)
    elif dia != '' and var.get() != 'Elegir':
        seleccionador_fechas(dia,dia2)
    elif dia2 != '' and var.get() != 'Elegir':
        seleccionador_fechas(dia,dia2)
    elif dia2 == '' and var.get() != 'Elegir':
        seleccionador_fechas(dia,dia2)
    elif dia2 == '' and dia != '':
        seleccionador_fechas(dia,dia2)
"""

def seleccionador_fechas(dia,dia2,year_var,datos,var,info_label3):
    if dia != '' and dia2 == '':
        info_label3.config(text=f" {dia} - {var.get()} - {year_var.get()}")
    elif dia == '' and dia2 == '':
        info_label3.config(text=f" dia - {var.get()} - {year_var.get()}")
    elif dia == '' and dia2 != '':
        info_label3.config(text=f"{dia2} - {var.get()} - {year_var.get()}")
    elif dia != '' and dia2 != '':
        info_label3.config(text=f"{dia} - {var.get()} - {year_var.get()}")



    datos.dia_comprado = dia
    datos.mes_comprado = var.get()
    return info_label3, datos.dia_comprado,datos.mes_comprado

@property
def imprimir_informacion_compra(datos,entrada1, entrada2, entrada3, entrada4, entrada5,lista,mensajes_error):
    if not lista.curselection():

        venta_error_provincia = tk.Toplevel()
        venta_error_provincia.title('¡Error al completar los datos!')
        venta_error_provincia.geometry('350x150')

        etiqueta_bienvenida = tk.Label(venta_error_provincia, text=f"¡Seleccione una provincia!")
        etiqueta_bienvenida.pack(pady=55)

        boton_continuar = tk.Button(venta_error_provincia, text="Continuar", command=venta_error_provincia.destroy)
        boton_continuar.pack(pady=20)
    else:
        mensajes_error = validar_entradas(entrada1, entrada2, entrada3, entrada4, entrada5, datos)
        if mensajes_error:
            compra_error(mensajes_error)
        elif mensajes_error == "Ingresar Fecha":
            compra_error(mensajes_error)
        else:
            guardar_datos(datos)
            compra_realizada(datos)

