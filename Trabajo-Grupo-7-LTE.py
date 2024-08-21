import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk

##definicion de funciones de bordeado para imagenes

# Definimos las listas

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

fechas_index = [
    "1", "2", "3", "4", "5", "6",
    "7", "8", "9", "10", "11", "12"
]

dias_index = [
    "1", "2", "3", "4", "5", "6",
    "7", "8", "9", "10", "11", "12"
]

#creamos los datos del usuario como objeto
class Datos:
    def __init__(self):
        self.nombre = ""
        self.dni = ""
        self.email = ""
        self.fecha = ""
        self.provincia = ""
        self.precio = ""


#con la clase definida podemos ahora guardar los datos en una 

def mostrar_ventana_principal(datos):

    """ creamos la  ventana principal """

    ventana = tk.Tk()
    ventana.title('Aeroline.ARG')
    ventana.geometry('1200x700')
    #implementacion de un color de fondo 3333333333333333333333333333333333333333333333333333333
    ventana.configure(bg='white')
    

    #-------------------------------------------------------------------------------------------------------------
    #                   aqui creamos los Frames para meter la estrutura del programa donde queremos con place
    #-------------------------------------------------------------------------------------------------------------
    style = ttk.Style()
    #style.configure("Transparent.TLabel", background="#fcfefb", foreground="black")
    style.configure("Transparent.TLabel", background="green", foreground="black") #color de fondo 333333333333333333333333333333333333333333333333333

    #----------------------------------------------------------------------------------marco para los widgets
    marco_logotipo = ttk.Frame(ventana, style="Transparent.TLabel")
    marco_logotipo.place(relx=0.22, rely=0.22, anchor="center", width=500, height=300)
    #--------------------eje x ----- eje y --------------------ancho-------alto-----

    marco_formulario = ttk.Frame(ventana, style="Transparent.TLabel")
    marco_formulario.place(relx=0.18, rely=0.3, anchor="center", width=450, height=200)
    #--------------------eje x ----- eje y --------------------ancho-------alto-----

    marco_formulario2 = ttk.Frame(ventana, style="Transparent.TLabel")
    marco_formulario2.place(relx=0.47, rely=0.28, anchor="center", width=200, height=200)
    #--------------------eje x ----- eje y --------------------ancho-------alto-----

    marco_formulario3 = ttk.Frame(ventana, style="Transparent.TLabel")
    marco_formulario3.place(relx=0.23, rely=0.7, anchor="center", width=450, height=350)
    #--------------------eje x ----- eje y --------------------ancho-------alto-----

    marco_formulario4 = ttk.Frame(ventana, style="Transparent.TLabel")
    marco_formulario4.place(relx=0.6, rely=0.7, anchor="center", width=450, height=350)
    #--------------------eje x ----- eje y --------------------ancho-------alto-----

    #-------------------------------------------------------------------------------------------------------------
    #                                           Ingresamos los Label y Entry
    #-------------------------------------------------------------------------------------------------------------
    # Retornar la instancia creada
    # seccion de logeo
    
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
    entrada6 = ttk.Entry(marco_formulario)
    entrada6.grid(row=6, column=1, padx=5, pady=2, sticky='ew')

    #guardo los datos en el class
    
    def guardar_datos():
        datos.nombre = entrada1.get() #la unica forma de entrar a los entry es con el .get
        datos.dni = entrada2.get()
        datos.email = entrada3.get()
        datos.fecha = entrada6.get()

    #-------------------------------------------------------------------------------------------------------------
    #                           se crea el Scrollbar para poder ver las provincias
    #-------------------------------------------------------------------------------------------------------------

    # listado de lasss provincias

    marco_lista = tk.Frame(marco_formulario2)
    marco_lista.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='w')

    scrollbar = tk.Scrollbar(marco_lista)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    lista = tk.Listbox(marco_lista, yscrollcommand=scrollbar.set)
    lista.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    for provincia in provincias_argentinas:
        lista.insert(tk.END, provincia)

    scrollbar.config(command=lista.yview)



    #-------------------------------------------------------------------------------------------------------------
    #                           se crea el Scrollbar para poder ver las provincias
    #-------------------------------------------------------------------------------------------------------------

    # listado de lasss provincias

    marco_lista2 = tk.Frame(marco_formulario4)
    marco_lista2.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='w')

    scrollbar = tk.Scrollbar(marco_lista2)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    lista2 = tk.Listbox(marco_lista2, yscrollcommand=scrollbar.set)
    lista2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    for fechas in fechas_index:
        lista2.insert(tk.END, fechas)

    scrollbar.config(command=lista.yview)




    #-------------------------------------------------------------------------------------------------------------
    #                           Primero un Label de Informacion de las provincias
    #-------------------------------------------------------------------------------------------------------------

    # Reservar espacio para mostrar el nombre de las provincias seleccionada

    info_label = tk.Label(marco_formulario3, text="Seleccione la provincia", background="#8ed0dc", width=30)
    info_label.pack(padx=5, pady=15, anchor='w')

    # vincular el evento de seleccion y el scrollbar

    #primero unimos las listas para formar un diccionario, provincia : precio

    provincias_con_precios = list(zip(provincias_argentinas, provincias_precios))

    #-------------------- Con la siguiente funcion podemos llamar las provincias y sus precios con dar clicl
    # provincias : precios 
    destino = None
    def on_select(event): #como es un click se define como evento
        seleccion_index = lista.curselection() #lista.curselection() me permite saber si le dimos click
        if seleccion_index:                     #ahora que le diste click nos da la infomacion de la seleccion
            seleccion = seleccion_index[0]      #donde le diste click lo guarda en seleccion, iniciando desde 0
            provincia, precio = provincias_con_precios[seleccion] #luego busca la provincia y su precio segun tu seleccion
            mostrar_informacion(provincia, precio)                 #nos deja la informacion en mostrar informacion

    ##chatgpt no sabia
    lista.bind('<<ListboxSelect>>', on_select)#vincula la el clicl con la lista

    ##definimos la seleccion de lista

    def mostrar_informacion(provincia, precios):
        global destino
        info_label.config(text=f"Precio del vuelos ${precios}")
        info_label2.config(text=f"{provincia}")

    info_label2 = tk.Label(marco_formulario3, text="Aeropuertos", font=("Arial", 15),width=20, background="#89cfdb")
    info_label2.pack(padx=8, pady=110, anchor='w')


    datos.provincia = provincia


    #-------------------------------------------------------------------------------------------------------------
    #                              guardar datos y mostrar mensaje de completado
    #-------------------------------------------------------------------------------------------------------------

    #aqui lo que hacemos es definir cual entry es el que esta vacio para imprimir un mensaje
    #no es eficiente pero ahorramos codigo



    def validar_entradas():
        entradas = [
            entrada1.get(), entrada2.get(), entrada3.get(), 
            entrada4.get(), entrada5.get(), entrada6.get()
        ]
        errores = [
            "Ingresar nombre",
            "Ingresar DNI",
            "Ingresar Email",
            "Ingresar N/T",
            "Ingresar CVV",
            "Ingresar Fecha"
        ]
        
        #flagse = [entrada == "" for entrada in entradas]

        flagse = []  # Creamos una lista 

        for entrada in entradas:  
            if entrada == "":  
                flagse.append(True)  
            else:
                flagse.append(False) 


        #mensajes_error = [errores[i] for i, flag in enumerate(flagse) if flag]

        mensajes_error = []  

        for i, flag in enumerate(flagse):  
            if flag:  
                mensajes_error.append(errores[i])  

        
        return mensajes_error #devuelve el resultado de la operacion
    
    def imprimir_informacion_compra():
        if not lista.curselection():
            venta_completada = tk.Toplevel()
            venta_completada.title('¡Error al completar los datos!')
            venta_completada.geometry('350x150')

            etiqueta_bienvenida = tk.Label(venta_completada, text=f"¡Seleccione una provincia!")
            etiqueta_bienvenida.pack(pady=55)

            boton_continuar = tk.Button(venta_completada, text="Continuar", command=compra_error.destroy)
            boton_continuar.pack(pady=20)
        else:
            mensajes_error = validar_entradas()
            if mensajes_error:
                compra_error(mensajes_error)
            else:
                guardar_datos()
                compra_realizada()



            
    #-------------------------------------------------------------------------------------------------------------
    #                           ventanas de compra realizada /// ventana de error///
    #-------------------------------------------------------------------------------------------------------------

    def compra_realizada():
        venta_completada = tk.Toplevel()
        venta_completada.title('Informacion del Ticket')
        venta_completada.geometry('400x250')

        # Utiliza el atributo 'nombre' de la instancia 'usuario_creado'
        etiqueta_bienvenida = tk.Label(venta_completada, text=f"¡Compra completada {datos.nombre}!")
        etiqueta_bienvenida.pack(pady=40)

        etiqueta_bienvenida2 = tk.Label(venta_completada, text=f"La fecha del viaje: {datos.fecha}")
        etiqueta_bienvenida2.pack(pady=20)

        etiqueta_bienvenida3 = tk.Label(venta_completada, text=f"Destino: {provincias_argentinas[provincia]}")
        etiqueta_bienvenida3.pack(pady=20)

        boton_continuar = tk.Button(venta_completada, text="Continuar", command=venta_completada.destroy)
        boton_continuar.pack(pady=20)

    def compra_error(mensajes_error):
        venta_completada = tk.Toplevel() 
        venta_completada.title('¡Error al completar los datos!') 
        venta_completada.geometry('400x250')

        for mensaje in mensajes_error:
            etiqueta_bienvenida = tk.Label(venta_completada, text=mensaje)
            etiqueta_bienvenida.pack(pady=30, anchor="center")


        boton_continuar = tk.Button(venta_completada, text="Continuar", command=compra_error.destroy)
        boton_continuar.pack(pady=20)

    # NO TOCAR LA POSICION DE LOS BOTONES PORQUE NO FUNCIONAN DESPUES

    boton_comprar = tk.Button(marco_formulario3, text="Comprar", command=imprimir_informacion_compra)
    boton_comprar.pack(padx=5, pady=5, anchor='s')

    ventana.mainloop()


#CARGA Y LLAMADA
mis_datos = Datos()
mostrar_ventana_principal(Datos)


















""" ESTRUCTURA """

#LISTAS
#CLASE USUARIO PARA MANEJAR LOS DATOS COMO OBJETOS DONDE YA CADA DATO ES UN ATRIBUTO
#CREAMOS LE VENTANA PRINCIPAL Y CARGAMOS LA CLASE USUARIO (datos)










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

"""
pack es uno de los métodos de gestión de geometría en Tkinter, utilizado para organizar widgets en la ventana.

side=tk.LEFT coloca el Listbox en el lado izquierdo del contenedor donde se encuentra.
fill=tk.BOTH hace que el Listbox se expanda para llenar todo el espacio disponible tanto en la dirección horizontal como en la vertical.
expand=True permite que el Listbox se expanda para ocupar cualquier espacio adicional en la ventana si esta se redimensiona.
"""

"""
scrollbar.config(command=lista.yview):

scrollbar es la barra de desplazamiento que acompaña al Listbox.
config(command=lista.yview) vincula la barra de desplazamiento al Listbox. yview es el método que gestiona la vista vertical del Listbox, permitiendo que la barra de desplazamiento controle la visualización del contenido del Listbox.

"""
    

"""
Estrategias para Mantener la Posición de los Widgets

Configura el sticky Adecuadamente:
El parámetro sticky en grid controla cómo se expanden los widgets dentro de sus celdas. Puedes usar valores como 'n', 's', 'e', 'w' para anclar el widget a los bordes de la celda.

Configura Pesos de Filas y Columnas:
Utiliza grid_rowconfigure y grid_columnconfigure para ajustar los pesos de las filas y columnas. Esto controla cómo se distribuye el espacio disponible cuando la ventana se redimensiona.

Usa padx y pady:
Ajusta los márgenes alrededor de los widgets para evitar que se muevan innecesariamente.
"""