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
    def __init__(self): # constructor
        self.nombre = ""
        self.dni = ""
        self.email = ""
        self.provincia = ""
        self.precio = ""
        self.dia_comprado = ""
        self.mes_comprado = ""
        self.id_comprado = ""

# Inicializamos la clase Datos de forma global
def inicializar_datos(): # constructor de la clase que inicializa los datos de forma global con la instancia datos
    global datos
    datos = Datos()

# Declaramos globales y funciones que necesiten acceso a variables globales
def guardar_datos():
    global datos
    datos.nombre = entrada1.get()
    datos.dni = entrada2.get()
    datos.email = entrada3.get()

# mostrar la ventana principal
def mostrar_ventana_principal():
    global ventana, provincias_con_precios, destinos, lista, mes, dia, dia_comprado, mes_comprado,imagen_logo, imagen_fondo,dia2,num_id

    ventana = tk.Tk()
    ventana.title('Aeroline.ARG')
    ventana.geometry('1200x700') 


    # Definimos más variables globales necesarias para el funcionamiento
    provincias_con_precios = list(zip(provincias_argentinas, provincias_precios))
    destinos = []
    mes = ''
    dia = ''
    dia2 = ''
    dia_comprado = ''
    mes_comprado = ''
    num_id = 1
    # Aquí puedes continuar con las configuraciones de la ventana principal, botones, etiquetas, etc.
    
    Fondo_principal()
    creando_frames()

    logotipo()
    imagen_informacion()
    Ingresado_informacion()

    #carga de los widgets
    Scrollbar()
    option_menu()
    mostrar_calendario()

    #boton
    boton_comprar = tk.Button(marco_formulario3, text="Comprar", command=imprimir_informacion_compra)
    boton_comprar.pack(padx=5, pady=5, anchor='s')

    ventana.mainloop()

def creando_frames():

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
    global info_label3,entrada1,entrada2,entrada3,entrada4,entrada5

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
    

    guardar_datos()



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
    lista.bind('<<ListboxSelect>>', on_select)#vincula la el clic con la lista
    datos.provincia = provincia



def mostrar_informacion(provincia, precios):
    info_label.config(text=f"Precio del vuelos ${precios}")
    info_label2.config(text=f"{provincia}")


def option_menu():
    global dia,dia2,var
    global dia_comprado
    global mes_comprado
    

    var = tk.StringVar(ventana)
    var.set("Elegir")
    global optionmenu
    optionmenu = tk.OptionMenu(ventana, var, *meses, command=lambda mes=var.get(): primer_cambio()) #(ventana, var, *meses, command=lambda mes=var.get(): primer_cambio()) 
    optionmenu.config(width=15)
    optionmenu.place(relx=0.11, rely=0.39)

    global primer_cambio,seleccionador_fechas

    def primer_cambio():
        if dia == '' and var.get():
            seleccionador_fechas(dia,dia2)
        elif dia != '' and var.get() != 'Elegir':
            seleccionador_fechas(dia,dia2)
        elif dia2 != '' and var.get() != 'Elegir':
            seleccionador_fechas(dia,dia2)
        elif dia2 == '' and var.get() != 'Elegir':
            seleccionador_fechas(dia,dia2)
        elif dia2 == '' and dia != '':
            seleccionador_fechas(dia,dia2)

    def seleccionador_fechas(dia,dia2):
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



def mostrar_calendario():
    # Frame para el calendario
    global calendar_frame
    calendar_frame = tk.Frame(marco_formulario5, background='white')
    calendar_frame.pack(pady=20)

    # Obtener el mes y el año actual
    now = datetime.now()
    global month_var
    mes_actual = now.month
    año_actual = now.year

    global year_var
    # Variables para el mes y el año seleccionados
    month_var = tk.StringVar(value=meses[mes_actual-1])
    year_var = tk.StringVar(value=str(año_actual))


    # Botón para actualizar el calendario
    optionmenu.bind('<<OptionMenuSelect>>', seleccionador_fechas(dia,dia2))


    # Funcion para actualizar el calendario
    def calendario(): #year_var = anio, month_var = mes
        #---------------------------------------------------------------------- limpiar la cuadricula existente
        for cuadraditos in calendar_frame.winfo_children(): #limpiamos el frame
            cuadraditos.destroy() #limpiamos el frame
        
        #--------------------------------------------------------------------- Obtener el mes y el año seleccionados
        año = int(year_var.get()) #obtenemos el anio
        mes = meses.index(month_var.get()) + 1 #obtenemos el mes

        # ---------------------------------------------------------------------Obtener los días de la semana y los dias del mes
        dias_semana = ["L", "M", "M", "J", "V", "S", "D"] #dias de la semana
        calendario_mes = calendar.monthcalendar(año, mes) #dias del mes


        # Crear encabezados para los dias de la semana
        for i, dia in enumerate(dias_semana): #primero enumeramos la cantidad de elementos que posee dias_semana que son los 7 dias de la semana
            label = tk.Label(calendar_frame, text=dia, background='white') #creamos un label haciendo dando el frame correspondiente, luego tenemos los dias y al final damos el color de fondo
            label.grid(row=0, column=i)#colocamos el label en una posicion
            label.config(width=2)#le damos el ancho

        # Rellenar el calendario con los días como botones
        for semana in range(len(calendario_mes)): #primero enumeramos la cantidad de elementos que posee calendario_mes que son las semanas
            for dia in range(7): #ahora enumeramos la cantidad de elementos que posee cada semana
                dia_numero = calendario_mes[semana][dia] #luego enumeramos la cantidad de elementos que posee cada dia
                if dia_numero != 0: #si el dia no es 0
                    button = tk.Button(calendar_frame, text=str(dia_numero),width=1, background='white',command=lambda dia=dia_numero: seleccionador_fechas(dia,dia2))#creamos un boton con el dia y le damos el command para que al darle click se llame a la funcion seleccionar dia
                    #command=lambda dia=dia_numero: seleccionador_fechas(dia,dia2)
                    button.grid(row=semana+1, column=dia) #colocamos el boton
                else: #si el dia es 0
                    label = tk.Label(calendar_frame, text="", background='white') #creamos un label
                    label.grid(row=semana+1, column=dia)#colocamos el label
    
    calendario() #llamamos la funcion calendario


###FUNCIONES DE VALIDACIONES ------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------
#                              guardar datos y mostrar mensaje de completado
#-------------------------------------------------------------------------------------------------------------

    #aqui lo que hacemos es definir cual entry es el que esta vacio para imprimir un mensaje
    #no es eficiente pero ahorramos codigo

def validar_entradas():

    entradas = [
        entrada1.get(), entrada2.get(), entrada3.get(), 
        entrada4.get(), entrada5.get(),datos.dia_comprado
    ]

    errores = [
        "Ingresar nombre",
        "Ingresar DNI",
        "Ingresar Email",
        "Ingresar N/T",
        "Ingresar CVV",
        "Ingresar Fecha"
    ]
    

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

def generar_id():
    global num_id
    datos.id_comprado = num_id
    num_id += 1
    return datos.id_comprado
    



def compra_realizada():
    venta_completada = tk.Toplevel()
    venta_completada.title('Informacion del Ticket')
    venta_completada.geometry('400x250')

    # Utiliza el atributo 'nombre' de la instancia 'usuario_creado'
    etiqueta_bienvenida = tk.Label(venta_completada, text=f"¡Compra completada {datos.nombre}!")
    etiqueta_bienvenida.pack(pady=20)
    
    generar_id()

    etiqueta_bienvenida2 = tk.Label(venta_completada, text=f"La fecha del viaje: {datos.mes_comprado}, {datos.dia_comprado} \n Su ID de compra es: \n {datos.id_comprado}")
    etiqueta_bienvenida2.pack(pady=20)

    """etiqueta_bienvenida3 = tk.Label(venta_completada, text=f"Destino: ")
    etiqueta_bienvenida3.pack(pady=20)"""

    boton_continuar = tk.Button(venta_completada, text="Continuar", command=venta_completada.destroy)
    boton_continuar.pack(pady=20)


def compra_error():
    venta_error = tk.Toplevel()
    venta_error.title('¡Error al completar los datos!')
    venta_error.geometry('400x250')

    for mensaje in mensajes_error:
        etiqueta_bienvenida = tk.Label(venta_error, text=mensaje)
        etiqueta_bienvenida.pack(pady=15, anchor="center")

    boton_continuar = tk.Button(venta_error, text="Continuar", command=venta_error.destroy)
    boton_continuar.pack(pady=20)



def imprimir_informacion_compra():
    if not lista.curselection():

        venta_error_provincia = tk.Toplevel()
        venta_error_provincia.title('¡Error al completar los datos!')
        venta_error_provincia.geometry('350x150')

        etiqueta_bienvenida = tk.Label(venta_error_provincia, text=f"¡Seleccione una provincia!")
        etiqueta_bienvenida.pack(pady=55)

        boton_continuar = tk.Button(venta_error_provincia, text="Continuar", command=venta_error_provincia.destroy)
        boton_continuar.pack(pady=20)
    else:
        mensajes_error = validar_entradas()
        if mensajes_error:
            compra_error()
        elif mensajes_error == "Ingresar Fecha":
            compra_error()
        else:
            guardar_datos()
            compra_realizada()





def __init__():
    inicializar_datos()
    mostrar_ventana_principal()

__init__()










