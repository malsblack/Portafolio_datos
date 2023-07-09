import pandas as pd
from tkinter import Tk, Label, Button, filedialog, messagebox, ttk, scrolledtext
from tkinter import *
import matplotlib.pyplot as plt
df_filtrado=""

def filtrador(df,datos):
    global df_filtrado
    lista=datos.split(",")
    df_filtrado=df.filter(items=lista)
    mostrar_dataframe_filtrado(df_filtrado)
    
def filtrar_menu(ventana_filtros,df):
    global df_filtrado
    df_filtrado=df
    ventana_filtros.withdraw()
    ventana_linea = Tk()
    ventana_linea.title("Encabezados y Tipos de Datos")
    ventana_linea.configure(bg="#444654") 

    # Obtener los nombres de los encabezados
    encabezados = list(df_filtrado.columns)

    # Obtener los tipos de datos
    tipos_datos = df_filtrado.dtypes.values.tolist()

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
    etiqueta_dato_x = Label(marco_principal, text="Columnas para filtrar, separadas por coma", font=('Arial 12'))
    etiqueta_dato_x.grid(row=len(encabezados) + 1, column=0, padx=10, pady=5, sticky="nsew")
    entrada_columna_x = Entry(marco_principal)
    entrada_columna_x.grid(row=len(encabezados) + 1, column=1, padx=10, pady=5, sticky="nsew")

        # Botón para generar la gráfica
    boton_generar = Button(marco_principal, text="Filtrar",
                           command=lambda: filtrador(df_filtrado, entrada_columna_x.get()))
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

def ordenar_por_precio(df):
    global df_filtrado
    df_filtrado=df
    df_filtrado['Price Each'] = df_filtrado['Price Each'].astype(int)
    df_filtrado.groupby('Price Each')
    df_filtrado = df_filtrado.sort_values('Price Each')
    mostrar_dataframe_filtrado(df_filtrado)
    
def ordenar_por_producto(df):
    global df_filtrado
    df_filtrado=df
    df_filtrado.groupby('Product')
    df_filtrado = df_filtrado.sort_values('Product')
    mostrar_dataframe_filtrado(df_filtrado)
    
def ordenar_por_dia(df):
    global df_filtrado
    df_filtrado=df
    df_filtrado.groupby('Order Date')
    df_filtrado = df_filtrado.sort_values('Order Date')
    mostrar_dataframe_filtrado(df_filtrado)

def mostrar_dataframe_filtrado(df):
    ventana_filtrado = Tk()
    ventana_filtrado.title("Filtrado")
    ventana_filtrado.configure(bg="#444654")  # Color de fondo

    style = ttk.Style()
    style.configure("TButton",
                    font=("Arial", 12),
                    padding=10,
                    background="#444654",  # Color de fondo del botón
                    foreground="#444654")  # Color del texto del botón
    style.configure("TFrame",
                    background="#444654")  # Color de fondo del frame

    # Crear el widget Treeview para mostrar el DataFrame
    treeview = ttk.Treeview(ventana_filtrado, height=30, show="headings", selectmode="extended")
    treeview["columns"] = list(df.columns)

    # Configurar las columnas del Treeview
    for column in list(df.columns):
        treeview.column(column, width=100)
        treeview.heading(column, text=column)

    # Insertar los datos en el Treeview
    for index, row in df.iterrows():
        treeview.insert("", "end", text=index, values=list(row))

    # Empacar el Treeview en la ventana
    treeview.pack()

    ventana_filtrado.mainloop()

def guardar_dataframe():
    global df_filtrado
    if df_filtrado.empty:
        messagebox.showerror("Error", "No se ha aplicado ningún filtro.")
        return

    ruta_archivo = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
    if ruta_archivo:
        df_filtrado.to_excel(ruta_archivo, index=False)
        messagebox.showinfo("Éxito", "El DataFrame filtrado se guardó correctamente.")   

def aplicar_filtros(df,root):
    root.withdraw()  # Oculta la ventana principal
    ventana_filtros = Tk()
    ventana_filtros.title("Filtrado")
    ventana_filtros.configure(bg="#444654")


    button_agrupar_precio =Button(ventana_filtros, text="Agrupar por Precio", command=lambda: ordenar_por_precio(df))
    button_agrupar_precio.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
    button_agrupar_precio.config(font=("Arial", 14),bg="#d9d9d9",fg="#444654")

    button_agrupar_producto = Button(ventana_filtros, text="Agrupar por Producto", command=lambda: ordenar_por_producto(df))
    button_agrupar_producto.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
    button_agrupar_producto.config(font=("Arial", 14),bg="#d9d9d9",fg="#444654")

    button_agrupar_fecha = Button(ventana_filtros, text="Agrupar por Fecha", command=lambda: ordenar_por_dia(df))
    button_agrupar_fecha.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")
    button_agrupar_fecha.config(font=("Arial", 14),bg="#d9d9d9",fg="#444654")
    
    button_agrupar_fecha = Button(ventana_filtros, text="Seleccionar Datos manual", command=lambda: filtrar_menu(ventana_filtros,df))
    button_agrupar_fecha.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")
    button_agrupar_fecha.config(font=("Arial", 14),bg="#d9d9d9",fg="#444654")

    button_guardar = Button(ventana_filtros, text="Guardar DataFrame Filtrado", command=guardar_dataframe)
    button_guardar.grid(row=4, column=0, padx=10, pady=5, sticky="nsew")
    button_guardar.config(font=("Arial", 14),bg="#d9d9d9",fg="#444654")

    button_menu = Button(ventana_filtros, text="Menu Principal", command=lambda:menu_principal(ventana_filtros,root),)
    button_menu.grid(row=5, column=0, padx=10, pady=5, sticky="nsew")
    button_menu.config(font=("Arial", 14),bg="#d9d9d9",fg="#444654")

    ventana_filtros.mainloop()



    