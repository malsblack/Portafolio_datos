import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

def media(df_imagen,datos_x):
    datos_x = df_imagen[datos_x]
    valor=np.mean(datos_x)
    messagebox.showinfo("Mediana",f"El valor de la media es: {valor}")


def info_media(ventana_filtros):
     # Obtener las columnas de tipo int
    columnas_int = df_imagen.select_dtypes(include=['int'])

    # Crear la ventana
    ventana_linea = Tk()
    ventana_linea.title("Encabezados y Tipos de Datos")
    ventana_linea.configure(bg="#444654") 

    # Obtener los nombres de los encabezados
    encabezados = list(columnas_int.columns)

    # Crear un marco adicional
    marco_principal = Frame(ventana_linea)
    marco_principal.pack(padx=10, pady=5)
    marco_principal.configure(bg="#444654") 

    # Crear un marco secundario para mostrar los encabezados
    marco = Frame(marco_principal)
    marco.grid(row=0, column=0, padx=10, pady=5)
    marco_principal.configure(bg="#444654") 

    etiqueta_encabezado = Label(marco, text="Encabezado", font=('Arial 14 bold'))
    etiqueta_encabezado.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")

    # Mostrar los encabezados en etiquetas
    for i in range(len(encabezados)):
        encabezado = encabezados[i]
        etiqueta = Label(marco, text=f"{encabezado}", font=('Arial 12'))
        etiqueta.grid(row=i + 1, column=0, padx=10, pady=5, sticky="nsew")
        etiqueta = Label(marco, text="INT", font=('Arial 12'))
        etiqueta.grid(row=i + 1, column=1, padx=10, pady=5, sticky="nsew")

    
    # Entradas para seleccionar los datos de las columnas x e y, y los nombres de las variables x e y
    etiqueta_dato_x = Label(marco_principal, text="Datos para X", font=('Arial 12'))
    etiqueta_dato_x.grid(row=len(encabezados) + 1, column=0, padx=10, pady=5, sticky="nsew")
    entrada_columna_x = Entry(marco_principal)
    entrada_columna_x.grid(row=len(encabezados) + 1, column=1, padx=10, pady=5, sticky="nsew")


    
    # Botón para generar la calculi
    boton_generar = Button(marco_principal, text="Calcular",
                           command=lambda: media(df_imagen, entrada_columna_x.get()))
    boton_generar.grid(row=len(encabezados)+5, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
    boton_generar.config(font=("Arial", 14),fg="#444654")
    
    boton_menu = Button(marco_principal, text="Regresar",
                           command=lambda: menu_principal(ventana_linea,ventana_filtros))
    boton_menu.grid(row=len(encabezados)+6, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
    boton_menu.config(font=("Arial", 14),fg="#444654")

    ventana_linea.mainloop()


def moda(df_imagen,datos_x):
    datos_x = df_imagen[datos_x]
    valores, conteos = np.unique(datos_x, return_counts=True)
    indice_moda = np.argmax(conteos)
    valor = valores[indice_moda]
    messagebox.showinfo("Mediana",f"El valor de la moda es: {valor}")


def info_moda(ventana_filtros):
        
    # Obtener las columnas de tipo int
    columnas_int = df_imagen.select_dtypes(include=['int'])

    # Crear la ventana
    ventana_linea = Tk()
    ventana_linea.title("Encabezados y Tipos de Datos")
    ventana_linea.configure(bg="#444654") 

    # Obtener los nombres de los encabezados
    encabezados = list(columnas_int.columns)

    # Crear un marco adicional
    marco_principal = Frame(ventana_linea)
    marco_principal.pack(padx=10, pady=5)
    marco_principal.configure(bg="#444654") 

    # Crear un marco secundario para mostrar los encabezados
    marco = Frame(marco_principal)
    marco.grid(row=0, column=0, padx=10, pady=5)
    marco_principal.configure(bg="#444654") 

    etiqueta_encabezado = Label(marco, text="Encabezado", font=('Arial 14 bold'))
    etiqueta_encabezado.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")

    # Mostrar los encabezados en etiquetas
    for i in range(len(encabezados)):
        encabezado = encabezados[i]
        etiqueta = Label(marco, text=f"{encabezado}", font=('Arial 12'))
        etiqueta.grid(row=i + 1, column=0, padx=10, pady=5, sticky="nsew")
        etiqueta = Label(marco, text="INT", font=('Arial 12'))
        etiqueta.grid(row=i + 1, column=1, padx=10, pady=5, sticky="nsew")

    
    # Entradas para seleccionar los datos de las columnas x e y, y los nombres de las variables x e y
    etiqueta_dato_x = Label(marco_principal, text="Datos para X", font=('Arial 12'))
    etiqueta_dato_x.grid(row=len(encabezados) + 1, column=0, padx=10, pady=5, sticky="nsew")
    entrada_columna_x = Entry(marco_principal)
    entrada_columna_x.grid(row=len(encabezados) + 1, column=1, padx=10, pady=5, sticky="nsew")


    
    # Botón para generar la calculi
    boton_generar = Button(marco_principal, text="Calcular",
                           command=lambda: moda(df_imagen, entrada_columna_x.get()))
    boton_generar.grid(row=len(encabezados)+5, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
    boton_generar.config(font=("Arial", 14),fg="#444654")
    
    boton_menu = Button(marco_principal, text="Regresar",
                           command=lambda: menu_principal(ventana_linea,ventana_filtros))
    boton_menu.grid(row=len(encabezados)+6, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
    boton_menu.config(font=("Arial", 14),fg="#444654")

    ventana_linea.mainloop()
        


def mediana(df_imagen,datos_x):
    datos_x = df_imagen[datos_x]
    valor=np.median(datos_x)
    messagebox.showinfo("Mediana",f"El valor de la mediana es: {valor}")


def info_mediana(ventana_filtros):
        
    # Obtener las columnas de tipo int
    columnas_int = df_imagen.select_dtypes(include=['int'])

    # Crear la ventana
    ventana_linea = Tk()
    ventana_linea.title("Encabezados y Tipos de Datos")
    ventana_linea.configure(bg="#444654") 

    # Obtener los nombres de los encabezados
    encabezados = list(columnas_int.columns)

    # Crear un marco adicional
    marco_principal = Frame(ventana_linea)
    marco_principal.pack(padx=10, pady=5)
    marco_principal.configure(bg="#444654") 

    # Crear un marco secundario para mostrar los encabezados
    marco = Frame(marco_principal)
    marco.grid(row=0, column=0, padx=10, pady=5)
    marco_principal.configure(bg="#444654") 

    etiqueta_encabezado = Label(marco, text="Encabezado", font=('Arial 14 bold'))
    etiqueta_encabezado.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")

    # Mostrar los encabezados en etiquetas
    for i in range(len(encabezados)):
        encabezado = encabezados[i]
        etiqueta = Label(marco, text=f"{encabezado}", font=('Arial 12'))
        etiqueta.grid(row=i + 1, column=0, padx=10, pady=5, sticky="nsew")
        etiqueta = Label(marco, text="INT", font=('Arial 12'))
        etiqueta.grid(row=i + 1, column=1, padx=10, pady=5, sticky="nsew")

    
    # Entradas para seleccionar los datos de las columnas x e y, y los nombres de las variables x e y
    etiqueta_dato_x = Label(marco_principal, text="Datos para X", font=('Arial 12'))
    etiqueta_dato_x.grid(row=len(encabezados) + 1, column=0, padx=10, pady=5, sticky="nsew")
    entrada_columna_x = Entry(marco_principal)
    entrada_columna_x.grid(row=len(encabezados) + 1, column=1, padx=10, pady=5, sticky="nsew")


    
    # Botón para generar la calculi
    boton_generar = Button(marco_principal, text="Calcular",
                           command=lambda: mediana(df_imagen, entrada_columna_x.get()))
    boton_generar.grid(row=len(encabezados)+5, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
    boton_generar.config(font=("Arial", 14),fg="#444654")
    
    boton_menu = Button(marco_principal, text="Regresar",
                           command=lambda: menu_principal(ventana_linea,ventana_filtros))
    boton_menu.grid(row=len(encabezados)+6, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
    boton_menu.config(font=("Arial", 14),fg="#444654")

    ventana_linea.mainloop()
        

def filtro():
    global df_imagen
    ruta_archivo = filedialog.askopenfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
    archivo=pd.read_excel(ruta_archivo)
    df_imagen=pd.DataFrame(archivo)


def menu_principal(ventana_filtros,root):
    ventana_filtros.destroy()
    root.deiconify()


def Ecuaciones(root):
    root.withdraw()  # Oculta la ventana principal
    ventana_filtros = Tk()
    ventana_filtros.title("ECUACIONES")
    ventana_filtros.configure(bg="#444654")


    button_filtro = Button(ventana_filtros, text="Seleccionar Filtro", command=lambda: filtro(), )
    button_filtro.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
    button_filtro.config(font=("Arial", 14),bg="#d9d9d9",fg="#444654")
    
    button_barras =Button(ventana_filtros, text="MODA", command=lambda: info_moda(ventana_filtros),)
    button_barras.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
    button_barras.config(font=("Arial", 14),bg="#d9d9d9",fg="#444654")
    

    button_linea = Button(ventana_filtros, text="MEDIANA", command=lambda: info_mediana(ventana_filtros))
    button_linea.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")
    button_linea.config(font=("Arial", 14),bg="#d9d9d9",fg="#444654")
    
    button_pastel = Button(ventana_filtros, text="MEDIA", command=lambda: info_media(ventana_filtros),)
    button_pastel.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")
    button_pastel.config(font=("Arial", 14),bg="#d9d9d9",fg="#444654")
    
    button_menu = Button(ventana_filtros, text="Menu Principal", command=lambda:menu_principal(ventana_filtros,root))
    button_menu.grid(row=4, column=0, padx=10, pady=5, sticky="nsew")
    button_menu.config(font=("Arial", 14),bg="#d9d9d9",fg="#444654")

    