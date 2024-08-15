import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw, ImageOps

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
#creamos los datos del usuario como objeto
class Datos:
    def __init__(self):
        # Inicializas los atributos vacíos
        self.nombre = ""
        self.dni = ""
        self.email = ""
        self.fecha = ""


#con la clase definida podemos ahora guardar los datos en una 

def mostrar_ventana_principal(datos):

    """ creamos la  ventana principal """

    ventana = tk.Tk()
    ventana.title('Aeroline.ARG')
    ventana.geometry('1200x700')

    #----------------cargar la imagen de fondo

    image_path = "file/image.png"  # Reemplaza con la ruta correcta de tu imagen
    image = Image.open(image_path)
    background_image = ImageTk.PhotoImage(image)

    #-----------------crear un widget Canvas
    
    canvas = tk.Canvas(ventana, width=900, height=700)
    canvas.pack(fill="both", expand=True)

    #colocar la imagen de fondo en el Canvas

    canvas.create_image(0, 0, image=background_image, anchor="nw")
    #canvas.background_image = background_image #mantener una referencia de la imagen para evitar que sea eliminada por el garbage collector
    #tenia error 
    #-------------------------------------------------------------------------------------------------------------

    style = ttk.Style()
    style.configure("Transparent.TLabel", background="#fcfefb", foreground="black")

    # Crear un marco para los widgets que usan grid

    marco_logotipo = ttk.Frame(ventana, style="Transparent.TLabel")
    marco_logotipo.place(relx=0.22, rely=0.22, anchor="center", width=500, height=300)

    marco_formulario = ttk.Frame(ventana, style="Transparent.TLabel")
    marco_formulario.place(relx=0.18, rely=0.3, anchor="center", width=450, height=200)

    marco_formulario2 = ttk.Frame(ventana, style="Transparent.TLabel")
    marco_formulario2.place(relx=0.52, rely=0.25, anchor="center", width=300, height=300)

    marco_formulario3 = ttk.Frame(ventana, style="Transparent.TLabel")
    marco_formulario3.place(relx=0.23, rely=0.7, anchor="center", width=450, height=350)

    #-------------------------------------------------------------------------------------------------------------

    # Cargar la imagen (logo)

    image_path = "file/logo.jpg"  # Reemplaza con la ruta correcta de tu logo
    imagen_logo = Image.open(image_path)
    imagen_logo = imagen_logo.resize((420, 80))  # Redimensiona la imagen si es necesario
    imagen_logo = ImageTk.PhotoImage(imagen_logo)

    # Crear un Label para mostrar la imagen

    label_logo = tk.Label(marco_logotipo, image=imagen_logo)
    label_logo.grid(row=0, column=0, padx=10, pady=10)  # Ajusta fila, columna, y relleno

    #-------------------------------------------------------------------------------------------------------------

    """
    Para agregar una imagen de fondo a un ttk.Frame y colocar dos Label en la parte superior de ese Frame utilizando grid, 
    puedes seguir estos pasos:

    Crear un Frame para la imagen de fondo.
    Agregar la imagen al Frame usando un Label.
    Colocar los Label encima de la imagen utilizando grid.
    """
    # Cargar la Imagen de Fondo
    image_path = "file/background_m2.jpg"  # Ruta de la imagen
    imagen_fondo = Image.open(image_path)
    imagen_fondo = imagen_fondo.resize((450, 350))
    imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

    #Crear el Frame y el Label para la Imagen:

    label_fondo = tk.Label(marco_formulario3, image=imagen_fondo)
    label_fondo.place(relx=0, rely=0, relwidth=1, relheight=1)

    ##ingresamos labels
    """
    Los Label se colocan en la parte superior del Frame usando grid. 
    Ajusta sticky para la alineación y padx, pady para el espaciado.
    """
    """
    Configuramos la expansión de filas y columnas para asegurar que el Frame y los Label se ajusten correctamente.
    """

    marco_formulario3.grid_rowconfigure(0, weight=1)
    marco_formulario3.grid_rowconfigure(1, weight=1)
    marco_formulario3.grid_columnconfigure(0, weight=1)

    #--------------------------------------------------------------------------------------------------------------
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

    # configurar la columna del `marco_formulario` para que el `entrada` no se expanda mas de lo necesario

    marco_formulario.columnconfigure(1, weight=1)
    marco_formulario.columnconfigure(2, weight=0)

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

    # Reservar espacio para `info_label` y configurar `sticky`

    info_label = tk.Label(marco_formulario3, text="Seleccione la provincia", background="#8ed0dc", width=30)
    info_label.pack(padx=5, pady=15, anchor='w')

    # vincular el evento de seleccion

    provincias_con_precios = list(zip(provincias_argentinas, provincias_precios))


    def on_select(event):
        seleccion_index = lista.curselection()
        if seleccion_index:
            seleccion = seleccion_index[0]
            provincia, precio = provincias_con_precios[seleccion]
            mostrar_informacion(provincia, precio)

    
    ##chatgpt no sabia

    lista.bind('<<ListboxSelect>>', on_select)

    ##definimos la seleccion de lista
    


    def mostrar_informacion(provincia, precios):
        info_label.config(text=f"Precio del vuelos ${precios}")
        info_label2.config(text=f"{provincia}")

    info_label2 = tk.Label(marco_formulario3, text="Aeropuertos", font=("Arial", 15),width=20, background="#89cfdb")
    info_label2.pack(padx=8, pady=110, anchor='w')

    #-------------------------------------------------------------------------------------------------------------
    #guardar datos y mostrar mensaje de completado
    





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
        
        flagse = [entrada == "" for entrada in entradas]

        mensajes_error = [errores[i] for i, flag in enumerate(flagse) if flag]
        
        return mensajes_error
    
    def imprimir_informacion_compra():
        if not lista.curselection():
            venta_completada = tk.Toplevel()
            venta_completada.title('¡Error al completar los datos!')
            venta_completada.geometry('450x450')

            etiqueta_bienvenida = tk.Label(venta_completada, text=f"¡Seleccione una provincia!")
            etiqueta_bienvenida.pack(pady=20)

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

    def compra_realizada():
        venta_completada = tk.Toplevel()
        venta_completada.title('Informacion del Ticket')
        venta_completada.geometry('250x250')

        # Utiliza el atributo 'nombre' de la instancia 'usuario_creado'
        etiqueta_bienvenida = tk.Label(venta_completada, text=f"¡Compra completada {datos.nombre}!")
        etiqueta_bienvenida.pack(pady=20)

        boton_continuar = tk.Button(venta_completada, text="Continuar", command=venta_completada.destroy)
        boton_continuar.pack(pady=20)

    def compra_error(mensajes_error):
        venta_completada = tk.Toplevel()
        venta_completada.title('¡Error al completar los datos!')
        venta_completada.geometry('450x450')

        for mensaje in mensajes_error:
            etiqueta_bienvenida = tk.Label(venta_completada, text=mensaje)
            etiqueta_bienvenida.pack(pady=5)


        boton_continuar = tk.Button(venta_completada, text="Continuar", command=compra_error.destroy)
        boton_continuar.pack(pady=20)

    # botones que no se moveran

    boton_comprar = tk.Button(marco_formulario3, text="Comprar", command=imprimir_informacion_compra)
    boton_comprar.pack(padx=5, pady=5, anchor='s')

    ventana.mainloop()

mis_datos = Datos()

mostrar_ventana_principal(Datos)



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