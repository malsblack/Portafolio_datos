import matplotlib.pyplot as plt
import pandas as pd
from tkinter import *
from tkinter import filedialog

def filtro():
    global df_imagen
    ruta_archivo = filedialog.askopenfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
    archivo=pd.read_excel(ruta_archivo)
    df_imagen=pd.DataFrame(archivo)

def grafica_linea(df_imagen,datos_x,datos_y,nombre_x,nombre_y):
    datos_x = df_imagen[datos_x]
    datos_y = df_imagen[datos_y]
    # Crear la gráfica de línea
    plt.plot(datos_x, datos_y)
    plt.xlabel(nombre_x)
    plt.ylabel(nombre_y)
    plt.title('Gráfica de Línea')
    plt.show()

def grafica_barras(df_imagen,datos_x,datos_y,nombre_x,nombre_y):
    datos_x = df_imagen[datos_x]
    datos_y = df_imagen[datos_y]
    # Crear la gráfica de línea
    plt.bar(datos_x, datos_y)
    plt.xlabel(nombre_x)
    plt.ylabel(nombre_y)
    plt.title('Gráfica de Barras')
    plt.show()

def grafica_pastel(df_imagen,datos_x,datos_y,nombre_x,nombre_y):
    datos_x = df_imagen[datos_x]
    datos_y = df_imagen[datos_y]
    aux=pd.DataFrame({f"{nombre_x}":datos_x,f"{nombre_y}":datos_y})
    data = aux[[nombre_x, nombre_y]].groupby(nombre_x).sum().reset_index()
    print(data)
    # Crear la gráfica de línea
    plt.pie(data[nombre_y], labels=data[nombre_x], autopct='%1.1f%%', startangle=90)
    plt.title('Gráfica de Barras')
    plt.show()



def info_linea(ventana_filtros):
    ventana_filtros.withdraw()
    ventana_linea = Tk()
    ventana_linea.title("Encabezados y Tipos de Datos")
    ventana_linea.configure(bg="#444654") 

    # Obtener los nombres de los encabezados
    encabezados = list(df_imagen.columns)

    # Obtener los tipos de datos
    tipos_datos = df_imagen.dtypes.values.tolist()

    # Crear un marco adicional
    marco_principal = Frame(ventana_linea)
    marco_principal.pack(padx=10, pady=5)
    marco_principal.configure(bg="#444654") 

    # Crear un marco secundario para mostrar los encabezados y tipos de datos
    marco = Frame(marco_principal)
    marco.grid(row=0, column=0, padx=10, pady=5)
    marco_principal.configure(bg="#444654") 

    etiqueta_encabezado = Label(marco, text="Encabezado", font=('Arial 14 bold'))
    etiqueta_encabezado.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
    etiqueta_tipo_dato = Label(marco, text="Tipo de Dato", font=('Arial 14 bold'))
    etiqueta_tipo_dato.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")

    # Mostrar los encabezados y tipos de datos en etiquetas
    for i in range(len(encabezados)):
        encabezado = encabezados[i]
        tipo_dato = str(tipos_datos[i])
        etiqueta = Label(marco, text=f"{encabezado}", font=('Arial 12'))
        etiqueta.grid(row=i + 1, column=0, padx=10, pady=5, sticky="nsew")

        etiqueta_dato = Label(marco, text=f"{tipo_dato}", font=('Arial 12'))
        etiqueta_dato.grid(row=i + 1, column=1, padx=10, pady=5, sticky="nsew")

    # Entradas para seleccionar los datos de las columnas x e y, y los nombres de las variables x e y
    etiqueta_dato_x = Label(marco_principal, text="Datos para X", font=('Arial 12'))
    etiqueta_dato_x.grid(row=len(encabezados) + 1, column=0, padx=10, pady=5, sticky="nsew")
    entrada_columna_x = Entry(marco_principal)
    entrada_columna_x.grid(row=len(encabezados) + 1, column=1, padx=10, pady=5, sticky="nsew")

    etiqueta_dato_x_label = Label(marco_principal, text="Etiqueta para X", font=('Arial 12'))
    etiqueta_dato_x_label.grid(row=len(encabezados) + 2, column=0, padx=10, pady=5, sticky="nsew")
    entrada_columna_x_label = Entry(marco_principal)
    entrada_columna_x_label.grid(row=len(encabezados) + 2, column=1, padx=10, pady=5, sticky="nsew")

    etiqueta_dato_y = Label(marco_principal, text="Datos para Y", font=('Arial 12'))
    etiqueta_dato_y.grid(row=len(encabezados) + 3, column=0, padx=10, pady=5, sticky="nsew")
    entrada_columna_y = Entry(marco_principal)
    entrada_columna_y.grid(row=len(encabezados) + 3, column=1, padx=10, pady=5, sticky="nsew")

    etiqueta_dato_y_label = Label(marco_principal, text="Etiqueta para Y", font=('Arial 12'))
    etiqueta_dato_y_label.grid(row=len(encabezados) + 4, column=0, padx=10, pady=5, sticky="nsew")
    entrada_columna_y_label = Entry(marco_principal)
    entrada_columna_y_label.grid(row=len(encabezados) + 4, column=1, padx=10, pady=5, sticky="nsew")

    # Botón para generar la gráfica
    boton_generar = Button(marco_principal, text="Generar Gráfica",
                           command=lambda: grafica_linea(df_imagen, entrada_columna_x.get(), entrada_columna_y.get(), entrada_columna_x_label.get(), entrada_columna_y_label.get()))
    boton_generar.grid(row=len(encabezados)+5, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
    boton_generar.config(font=("Arial", 14),fg="#444654")
    
    boton_menu = Button(marco_principal, text="Regresar",
                           command=lambda: menu_principal(ventana_linea,ventana_filtros))
    boton_menu.grid(row=len(encabezados)+6, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
    boton_menu.config(font=("Arial", 14),fg="#444654")

    ventana_linea.mainloop()
        
        
def info_barras(ventana_filtros):
    ventana_filtros.withdraw()
    ventana_linea = Tk()
    ventana_linea.title("Encabezados y Tipos de Datos")
    ventana_linea.configure(bg="#444654") 

    # Obtener los nombres de los encabezados
    encabezados = list(df_imagen.columns)

    # Obtener los tipos de datos
    tipos_datos = df_imagen.dtypes.values.tolist()

    # Crear un marco adicional
    marco_principal = Frame(ventana_linea)
    marco_principal.pack(padx=10, pady=5)
    marco_principal.configure(bg="#444654") 

    # Crear un marco secundario para mostrar los encabezados y tipos de datos
    marco = Frame(marco_principal)
    marco.grid(row=0, column=0, padx=10, pady=5)
    marco_principal.configure(bg="#444654") 

    etiqueta_encabezado = Label(marco, text="Encabezado", font=('Arial 14 bold'))
    etiqueta_encabezado.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
    etiqueta_tipo_dato = Label(marco, text="Tipo de Dato", font=('Arial 14 bold'))
    etiqueta_tipo_dato.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")

    # Mostrar los encabezados y tipos de datos en etiquetas
    for i in range(len(encabezados)):
        encabezado = encabezados[i]
        tipo_dato = str(tipos_datos[i])
        etiqueta = Label(marco, text=f"{encabezado}", font=('Arial 12'))
        etiqueta.grid(row=i + 1, column=0, padx=10, pady=5, sticky="nsew")

        etiqueta_dato = Label(marco, text=f"{tipo_dato}", font=('Arial 12'))
        etiqueta_dato.grid(row=i + 1, column=1, padx=10, pady=5, sticky="nsew")

    # Entradas para seleccionar los datos de las columnas x e y, y los nombres de las variables x e y
    etiqueta_dato_x = Label(marco_principal, text="Datos para X", font=('Arial 12'))
    etiqueta_dato_x.grid(row=len(encabezados) + 1, column=0, padx=10, pady=5, sticky="nsew")
    entrada_columna_x = Entry(marco_principal)
    entrada_columna_x.grid(row=len(encabezados) + 1, column=1, padx=10, pady=5, sticky="nsew")

    etiqueta_dato_x_label = Label(marco_principal, text="Etiqueta para X", font=('Arial 12'))
    etiqueta_dato_x_label.grid(row=len(encabezados) + 2, column=0, padx=10, pady=5, sticky="nsew")
    entrada_columna_x_label = Entry(marco_principal)
    entrada_columna_x_label.grid(row=len(encabezados) + 2, column=1, padx=10, pady=5, sticky="nsew")

    etiqueta_dato_y = Label(marco_principal, text="Datos para Y", font=('Arial 12'))
    etiqueta_dato_y.grid(row=len(encabezados) + 3, column=0, padx=10, pady=5, sticky="nsew")
    entrada_columna_y = Entry(marco_principal)
    entrada_columna_y.grid(row=len(encabezados) + 3, column=1, padx=10, pady=5, sticky="nsew")

    etiqueta_dato_y_label = Label(marco_principal, text="Etiqueta para Y", font=('Arial 12'))
    etiqueta_dato_y_label.grid(row=len(encabezados) + 4, column=0, padx=10, pady=5, sticky="nsew")
    entrada_columna_y_label = Entry(marco_principal)
    entrada_columna_y_label.grid(row=len(encabezados) + 4, column=1, padx=10, pady=5, sticky="nsew")

    # Botón para generar la gráfica
    boton_generar = Button(marco_principal, text="Generar Gráfica",
                           command=lambda: grafica_barras(df_imagen, entrada_columna_x.get(), entrada_columna_y.get(), entrada_columna_x_label.get(), entrada_columna_y_label.get()))
    boton_generar.grid(row=len(encabezados)+5, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
    boton_generar.config(font=("Arial", 14),fg="#444654")
    
    boton_menu = Button(marco_principal, text="Regresar",
                           command=lambda: menu_principal(ventana_linea,ventana_filtros))
    boton_menu.grid(row=len(encabezados)+6, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
    boton_menu.config(font=("Arial", 14),fg="#444654")

    ventana_linea.mainloop()
        
def info_pastel(ventana_filtros):
    ventana_filtros.withdraw()
    ventana_linea = Tk()
    ventana_linea.title("Encabezados y Tipos de Datos")
    ventana_linea.configure(bg="#444654") 

    # Obtener los nombres de los encabezados
    encabezados = list(df_imagen.columns)

    # Obtener los tipos de datos
    tipos_datos = df_imagen.dtypes.values.tolist()

    # Crear un marco adicional
    marco_principal = Frame(ventana_linea)
    marco_principal.pack(padx=10, pady=5)
    marco_principal.configure(bg="#444654") 

    # Crear un marco secundario para mostrar los encabezados y tipos de datos
    marco = Frame(marco_principal)
    marco.grid(row=0, column=0, padx=10, pady=5)
    marco_principal.configure(bg="#444654") 

    etiqueta_encabezado = Label(marco, text="Encabezado", font=('Arial 14 bold'))
    etiqueta_encabezado.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
    etiqueta_tipo_dato = Label(marco, text="Tipo de Dato", font=('Arial 14 bold'))
    etiqueta_tipo_dato.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")

    # Mostrar los encabezados y tipos de datos en etiquetas
    for i in range(len(encabezados)):
        encabezado = encabezados[i]
        tipo_dato = str(tipos_datos[i])
        etiqueta = Label(marco, text=f"{encabezado}", font=('Arial 12'))
        etiqueta.grid(row=i + 1, column=0, padx=10, pady=5, sticky="nsew")

        etiqueta_dato = Label(marco, text=f"{tipo_dato}", font=('Arial 12'))
        etiqueta_dato.grid(row=i + 1, column=1, padx=10, pady=5, sticky="nsew")

    # Entradas para seleccionar los datos de las columnas x e y, y los nombres de las variables x e y
    etiqueta_dato_x = Label(marco_principal, text="Datos para X", font=('Arial 12'))
    etiqueta_dato_x.grid(row=len(encabezados) + 1, column=0, padx=10, pady=5, sticky="nsew")
    entrada_columna_x = Entry(marco_principal)
    entrada_columna_x.grid(row=len(encabezados) + 1, column=1, padx=10, pady=5, sticky="nsew")

    etiqueta_dato_x_label = Label(marco_principal, text="Etiqueta para X", font=('Arial 12'))
    etiqueta_dato_x_label.grid(row=len(encabezados) + 2, column=0, padx=10, pady=5, sticky="nsew")
    entrada_columna_x_label = Entry(marco_principal)
    entrada_columna_x_label.grid(row=len(encabezados) + 2, column=1, padx=10, pady=5, sticky="nsew")

    etiqueta_dato_y = Label(marco_principal, text="Datos para Y", font=('Arial 12'))
    etiqueta_dato_y.grid(row=len(encabezados) + 3, column=0, padx=10, pady=5, sticky="nsew")
    entrada_columna_y = Entry(marco_principal)
    entrada_columna_y.grid(row=len(encabezados) + 3, column=1, padx=10, pady=5, sticky="nsew")

    etiqueta_dato_y_label = Label(marco_principal, text="Etiqueta para Y", font=('Arial 12'))
    etiqueta_dato_y_label.grid(row=len(encabezados) + 4, column=0, padx=10, pady=5, sticky="nsew")
    entrada_columna_y_label = Entry(marco_principal)
    entrada_columna_y_label.grid(row=len(encabezados) + 4, column=1, padx=10, pady=5, sticky="nsew")

    # Botón para generar la gráfica
    boton_generar = Button(marco_principal, text="Generar Gráfica",
                           command=lambda: grafica_pastel(df_imagen, entrada_columna_x.get(), entrada_columna_y.get(), entrada_columna_x_label.get(), entrada_columna_y_label.get()))
    boton_generar.grid(row=len(encabezados)+5, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
    boton_generar.config(font=("Arial", 14),fg="#444654")
    
    boton_menu = Button(marco_principal, text="Regresar",
                           command=lambda: menu_principal(ventana_linea,ventana_filtros))
    boton_menu.grid(row=len(encabezados)+6, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
    boton_menu.config(font=("Arial", 14),fg="#444654")

    ventana_linea.mainloop()
        

def menu_principal(ventana_filtros,root):
    ventana_filtros.destroy()
    root.deiconify()

def graficas(root):
    root.withdraw()  # Oculta la ventana principal
    ventana_filtros = Tk()
    ventana_filtros.title("Graficas")
    ventana_filtros.configure(bg="#444654")


    button_filtro = Button(ventana_filtros, text="Seleccionar Filtro", command=lambda: filtro(), )
    button_filtro.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
    button_filtro.config(font=("Arial", 14),bg="#d9d9d9",fg="#444654")

    button_barras =Button(ventana_filtros, text="Grafica de barras", command=lambda: info_barras(ventana_filtros),)
    button_barras.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
    button_barras.config(font=("Arial", 14),bg="#d9d9d9",fg="#444654")
    

    button_linea = Button(ventana_filtros, text="Grafica por linea", command=lambda: info_linea(ventana_filtros))
    button_linea.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")
    button_linea.config(font=("Arial", 14),bg="#d9d9d9",fg="#444654")
    
    button_pastel = Button(ventana_filtros, text="Grafica por pastel", command=lambda: info_pastel(ventana_filtros),)
    button_pastel.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")
    button_pastel.config(font=("Arial", 14),bg="#d9d9d9",fg="#444654")
    
    button_menu = Button(ventana_filtros, text="Menu Principal", command=lambda:menu_principal(ventana_filtros,root))
    button_menu.grid(row=4, column=0, padx=10, pady=5, sticky="nsew")
    button_menu.config(font=("Arial", 14),bg="#d9d9d9",fg="#444654")
    
    
    



    ventana_filtros.mainloop()


