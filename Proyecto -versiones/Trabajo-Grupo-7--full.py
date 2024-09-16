import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import calendar
from datetime import datetime


##definicion de funciones de bordeado para imagenes
#verificacion de conexion para poder tener actualizado el programa de compra


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

meses = [
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre"
]




#creamos los datos del usuario como objeto
class Datos:
    def __init__(self):
        self.nombre = ""
        self.dni = ""
        self.email = ""
        self.provincia = ""
        self.precio = ""
    



#creamos una clase para la ventana
class Ventana:
    def __init__(self):
        pass



def mostrar_ventana_principal(datos):

    #-------------------------------------------------------------------------------------
    #                                   ventana principal
    #-------------------------------------------------------------------------------------  

    ventana = tk.Tk()
    ventana.title('Aeroline.ARG')
    ventana.geometry('1200x700') #width x height
    
    

    #----------------cargar la imagen de fondo

    image_path = "file/image.png"  # --------------------------------definimos la ruta de la imagen
    image = Image.open(image_path) # --------------------------------abrimos la imagen con el modulo Image
    background_image = ImageTk.PhotoImage(image) #-------------------definimos background image con el modulo de tk ImageTK y usamos la clase PhotoImage(con la imagen)

    #-----------------crear un cuadraditos Canvas ------------------ aca aclaro que saque de chatgpt la implementacion porq no sabia usar images como fondo

    canvas = tk.Canvas(ventana, width=900, height=700)
    canvas.pack(fill="both", expand=True)

    #--------------------------------------------------------------- colocar la imagen de fondo en el Canvas

    canvas.create_image(0, 0, image=background_image, anchor="nw")

    


    #-------------------------------------------------------------------------------------------------------------
    #                   aqui creamos los Frames para meter la estrutura del programa donde queremos con place
    #-------------------------------------------------------------------------------------------------------------
    global style
    style = ttk.Style() #definimos el estilo
    style.configure("Transparent.TLabel", background="#fcfefb", foreground="black") #color de fondo

    #----------------------------------------------------------------------------------marco para los cuadraditoss
    marco_logotipo = ttk.Frame(ventana, style="Transparent.TLabel")
    marco_logotipo.place(relx=0.22, rely=0.22, anchor="center", width=500, height=300)
    #--------------------eje x ----- eje y --------------------ancho-------alto-----

    marco_formulario = ttk.Frame(ventana, style="Transparent.TLabel")#Label y entry
    marco_formulario.place(relx=0.18, rely=0.3, anchor="center", width=450, height=200)
    #--------------------eje x ----- eje y --------------------ancho-------alto-----

    marco_formulario2 = ttk.Frame(ventana, style="Transparent.TLabel")#Scrollbar
    marco_formulario2.place(relx=0.35, rely=0.28, anchor="center", width=200, height=200)
    #--------------------eje x ----- eje y --------------------ancho-------alto-----

    marco_formulario3 = ttk.Frame(ventana, style="Transparent.TLabel") #imagen de azul que tiene la informacion de aeropuerto y precio
    marco_formulario3.place(relx=0.23, rely=0.7, anchor="center", width=450, height=350)
    #--------------------eje x ----- eje y --------------------ancho-------alto-----

    #-------------------------------------------------------------------- el frame que no sirve
    marco_formulario4 = ttk.Frame(ventana, style="Transparent.TLabel")
    marco_formulario4.place(relx=0.5, rely=0.2, anchor="center", width=150, height=150)
    #--------------------eje x ----- eje y --------------------ancho-------alto---------

    marco_formulario5 = ttk.Frame(ventana, style="Transparent.TLabel") # calendario
    marco_formulario5.place(relx=0.53, rely=0.26, anchor="center", width=310, height=215)
    #--------------------eje x ----- eje y --------------------ancho-------alto---------


    #-------------------------------------------------------------------------------------------------------------
    #                           EL Laber que contiene la primera imagen (logo)
    #-------------------------------------------------------------------------------------------------------------
    # Cargar la imagen (logo)

    image_path = "file/logo.jpg"                                            # Reemplaza con la ruta correcta de tu logo
    imagen_logo = Image.open(image_path)
    imagen_logo = imagen_logo.resize((420, 80))                             # Redimensiona la imagen si es necesario
    imagen_logo = ImageTk.PhotoImage(imagen_logo)
    #------------------------------------------------------------------------ Crear un Label para mostrar la imagen


    label_logo = tk.Label(marco_logotipo, image=imagen_logo)
    label_logo.grid(row=0, column=0, padx=10, pady=10)                       # Ajusta fila, columna, y relleno

    #-------------------------------------------------------------------------------------------------------------
    #                           EL Laber que contiene la segunda imagen (imagen de azul)
    #-------------------------------------------------------------------------------------------------------------
    
    #Para agregar una imagen de fondo a un ttk.Frame y colocar dos Label en la parte superior de ese Frame utilizando grid 
    #crear un Frame para la imagen de fondo.
    #agregar la imagen al Frame usando un Label.
    #colocar los Label encima de la imagen utilizando grid.

    #-------------------------------------------------------------------------------------cargar la Imagen de Fondo
    image_path = "file/background_m2.jpg"  # Ruta de la imagen
    imagen_fondo = Image.open(image_path)
    imagen_fondo = imagen_fondo.resize((450, 350))
    imagen_fondo = ImageTk.PhotoImage(imagen_fondo)
 
    #Crear el Frame y el Label para la Imagen:

    label_fondo = tk.Label(marco_formulario3, image=imagen_fondo)
    label_fondo.place(relx=0, rely=0, relwidth=1, relheight=1)

    #-------------------------------------------------------------------------------------------ingresamos labels
    #Los Label se colocan en la parte superior del Frame usando grid. 
    #Ajusta sticky para la alineacion //// padx, pady para el espaciado.
    #Configuramos la expansión de filas y columnas para asegurar que el Frame y los Label se ajusten correctamente.

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

    

    #guardo los datos en el class
    
    def guardar_datos(): #----------------------------------------------------------funcion para guardar los datos
        datos.nombre = entrada1.get() #--------------------------la unica forma de entrar a los entry es con el .get
        datos.dni = entrada2.get() 
        datos.email = entrada3.get()


    #-------------------------------------------------------------------------------------------------------------
    #                           se crea el Scrollbar para poder ver las provincias
    #-------------------------------------------------------------------------------------------------------------

    # configurar la columna del `marco_formulario` para que el `entrada` no se expanda mas de lo necesario

    

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
    #                           Primero un Label de Informacion de las provincias
    #-------------------------------------------------------------------------------------------------------------

    # Reservar espacio para mostrar el nombre de las provincias seleccionada

    info_label = tk.Label(marco_formulario3, text="Seleccione la provincia", background="#8ed0dc", width=30)
    info_label.pack(padx=5, pady=15, anchor='w')

    # vincular el evento de seleccion y el scrollbar

    #primero unimos las listas para formar un diccionario, provincia : precio

    provincias_con_precios = list(zip(provincias_argentinas, provincias_precios))

    #-------------------- Con la siguiente funcion podemos llamar las provincias y sus precios con dar clicl
    
    destinos = []
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

    ##definimos la seleccion de lista

    def mostrar_informacion(provincia, precios):
        global destino
        info_label.config(text=f"Precio del vuelos ${precios}")
        info_label2.config(text=f"{provincia}")
        #etiqueta_bienvenida3.config(text=f"Destino: {provincia}")

    info_label2 = tk.Label(marco_formulario3, text="Aeropuertos", font=("Arial", 15),width=20, background="#89cfdb")
    info_label2.pack(padx=8, pady=110, anchor='w')


    datos.provincia = provincia


    #-------------------------------------------------------------------------------------------------------------
    #                                                   optionmenu
    #-------------------------------------------------------------------------------------------------------------

    global mes
    global dia
    dia = ''
    dia2 = ''

    var = tk.StringVar(ventana)
    var.set("Elegir")
    
    optionmenu = tk.OptionMenu(ventana, var, *meses, command=lambda mes=var.get(): primer_cambio())
    optionmenu.config(width=15)
    optionmenu.place(relx=0.11, rely=0.39)
            

    #definimos el primer cambio para que cuando se cambie el mes se reinicie el label
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


    #aqui definimos que mes selecciono el usuario y lo guardamos en la variable mes

    # Vincular el cambio en el OptionMenu con la función option_menu
    


    #definimos los dias para que funcione el calendario
    
    def seleccionador_fechas(dia,dia2):
        """Actualiza el label con el día y mes seleccionados."""
        if dia != '' and dia2 == '':
            dia2 = dia
            info_label3.config(text=f" {dia} - {var.get()} - {year_var.get()}")
        elif dia == '' and dia2 == '':
            info_label3.config(text=f" dia - {var.get()} - {year_var.get()}")
        elif dia == '' and dia2 != '':
            info_label3.config(text=f"{dia2} - {var.get()} - {year_var.get()}")
        elif dia != '' and dia2 != '':
            info_label3.config(text=f"{dia} - {var.get()} - {year_var.get()}")


        global dia_comprado
        global mes_comprado
        mes_comprado = var.get()
        dia_comprado = dia
        print({var.get()})

    #-------------------------------------------------------------------------------------------------------------
    #                                                   calendario
    #-------------------------------------------------------------------------------------------------------------
    
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

        optionmenu.bind('<<OptionMenuSelect>>', seleccionador_fechas)
    
        #if var.trace('write', lambda *args: seleccionador_fechas(dia))
        #if var.get() != 'Elegir':
        #    var.trace('w', lambda *args: seleccionador_fechas(dia))
        #llamamos la funcion seleccionador_fechas cuando cambie el valor de la variable var
        

        #optionmenu.event_generate("<<OptionMenuSelect>>", seleccionar_dia)

        #optionmenu.bind('<<OptionMenuSelect>>', seleccionador_fechas())#vincula la el clicl con la lista

        ##chatgpt no sabia

    
        #funcion que actualiza los mese - llama a la funcion cargar

        # Función para actualizar el calendario
        def calendario(year_var,month_var,calendar_frame): #year_var = anio, month_var = mes
        #---------------------------------------------------------------------- Limpiar la cuadrícula existente
            for cuadraditos in calendar_frame.winfo_children(): #limpiamos el frame
                cuadraditos.destroy() #limpiamos el frame
            
            #--------------------------------------------------------------------- Obtener el mes y el año seleccionados
            año = int(year_var.get()) #obtenemos el anio
            mes = meses.index(month_var.get()) + 1 #obtenemos el mes

            # ---------------------------------------------------------------------Obtener los días de la semana y los días del mes
            dias_semana = ["L", "M", "M", "J", "V", "S", "D"] #dias de la semana
            calendario_mes = calendar.monthcalendar(año, mes) #dias del mes

            # --------------------------------------------------------------------- Crear encabezados para los años de la semana
            #
            #--------------------------------------------------------------------------------------

            #idea! crear una lista con las posiciones de comienzo de cada mes, luego de seleccionarlo que el for se acomode en el calendario
            #posicionando cada label en la posicion correspondiente del mes


            
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
                        button.grid(row=semana+1, column=dia) #colocamos el boton
                    else: #si el dia es 0
                        label = tk.Label(calendar_frame, text="", background='white') #creamos un label
                        label.grid(row=semana+1, column=dia)#colocamos el label
        
        calendario(year_var,month_var,calendar_frame) #llamamos la funcion calendario


    
    #label_info_fecha

    #-------------------------------------------------------------------------------------------------------------
    #                              guardar datos y mostrar mensaje de completado
    #-------------------------------------------------------------------------------------------------------------

    #aqui lo que hacemos es definir cual entry es el que esta vacio para imprimir un mensaje
    #no es eficiente pero ahorramos codigo

    def validar_entradas():
        entradas = [
            entrada1.get(), entrada2.get(), entrada3.get(), 
            entrada4.get(), entrada5.get()#, entrada6.get()
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

        flagse = []  # Creamos una lista vacia para almacenar los resultados

        for entrada in entradas: #recorremos la lista de entradas  
            if entrada == "":  # Si la entrada es vacia
                flagse.append(True) # Agregamos True a la lista  
            else:
                flagse.append(False) # Agregamos False a la lista


        #mensajes_error = [errores[i] for i, flag in enumerate(flagse) if flag]

        mensajes_error = []  

        for i, flag in enumerate(flagse):  
            if flag:  
                mensajes_error.append(errores[i])# Si la entrada es vacia, agrega el error correspondiente
        return mensajes_error #devuelve el resultado de la operacion


    #-------------------------------------------------------------------------------------------------------------
    #                                 funcion para imprimir la compra realizada
    #-------------------------------------------------------------------------------------------------------------

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

        etiqueta_bienvenida2 = tk.Label(venta_completada, text=f"La fecha del viaje: {mes_comprado}, {dia_comprado}")
        etiqueta_bienvenida2.pack(pady=20)

        """etiqueta_bienvenida3 = tk.Label(venta_completada, text=f"Destino: ")
        etiqueta_bienvenida3.pack(pady=20)"""

        boton_continuar = tk.Button(venta_completada, text="Continuar", command=venta_completada.destroy)
        boton_continuar.pack(pady=20)
        guardar_datos()

    def compra_error(mensajes_error):
        venta_completada = tk.Toplevel()
        venta_completada.title('¡Error al completar los datos!')
        venta_completada.geometry('400x250')

        for mensaje in mensajes_error:
            etiqueta_bienvenida = tk.Label(venta_completada, text=mensaje)
            etiqueta_bienvenida.pack(pady=30, anchor="center")


        boton_continuar = tk.Button(venta_completada, text="Continuar", command=compra_error.destroy)
        boton_continuar.pack(pady=20)
        guardar_datos()

    # NO TOCAR LA POSICION DE LOS BOTONES PORQUE NO FUNCIONAN DESPUES
    

    boton_comprar = tk.Button(marco_formulario3, text="Comprar", command=imprimir_informacion_compra)
    boton_comprar.pack(padx=5, pady=5, anchor='s')

    mostrar_calendario()
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
    sticky='n': Alinea el cuadraditos al borde norte (superior) de la celda.
    sticky='e': Alinea el cuadraditos al borde este (derecho) de la celda.
    sticky='s': Alinea el cuadraditos al borde sur (inferior) de la celda.
    sticky='w': Alinea el cuadraditos al borde oeste (izquierdo) de la celda.
    sticky='ne': Alinea el cuadraditos en la esquina noreste (superior derecha) de la celda.
    sticky='sw': Alinea el cuadraditos en la esquina suroeste (inferior izquierda) de la celda.
    sticky='ns': Expande el cuadraditos verticalmente para llenar toda la altura de la celda.
    sticky='ew': Expande el cuadraditos horizontalmente para llenar toda la anchura de la celda.
    sticky='nsew': Expande el cuadraditos para llenar toda la celda, tanto horizontal como verticalmente.
"""

"""
pack es uno de los métodos de gestión de geometría en Tkinter, utilizado para organizar cuadraditoss en la ventana.

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
Estrategias para Mantener la Posición de los cuadraditoss

Configura el sticky Adecuadamente:
El parámetro sticky en grid controla cómo se expanden los cuadraditoss dentro de sus celdas. Puedes usar valores como 'n', 's', 'e', 'w' para anclar el cuadraditos a los bordes de la celda.

Configura Pesos de Filas y Columnas:
Utiliza grid_rowconfigure y grid_columnconfigure para ajustar los pesos de las filas y columnas. Esto controla cómo se distribuye el espacio disponible cuando la ventana se redimensiona.

Usa padx y pady:
Ajusta los márgenes alrededor de los cuadraditoss para evitar que se muevan innecesariamente.
"""