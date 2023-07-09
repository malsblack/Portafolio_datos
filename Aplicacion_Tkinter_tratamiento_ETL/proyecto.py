import pandas as pd
from GRAFICAS import GRAFICAS
from ECUACIONES import ECUACIONES
from FILTRADO import FILTRADO
from tkinter import Tk, Label, Button, filedialog, messagebox, ttk, scrolledtext
import matplotlib.pyplot as plt

df=pd.read_excel("DATOS\Enero2019.xlsx")
def visualizar_datos(df):
    # Crear la ventana
    ventana_datos = Tk()
    ventana_datos.title("Datos")

    # Crear el widget Treeview para mostrar los datos
    treeview = ttk.Treeview(ventana_datos,height=30, show="headings",selectmode="extended")
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

    # Ejecutar el bucle de eventos de la ventana
    ventana_datos.mainloop()

def info():
    messagebox.showinfo("Informacion alumna","Nombre: Lemus Valencia Citlalli Danahi \n Grupo: 4GM2 \n Boleta: 2021401363")
    

# Crea la interfaz utilizando Tkinter
root = Tk()
messagebox.showinfo("Menu principal","Bienvenido al programa de análisis de ventas de la tienda de electrónica")
root.title("Análisis de Ventas")
root.configure(bg="#444654")  # Color de fondo

# Crear estilo para los botones y frames
style = ttk.Style()
style.configure("TButton",
                font=("Arial", 14),
                padding=10,
                background="#444654",  # Color de fondo del botón
                foreground="#444654")  # Color del texto del botón
style.configure("TFrame",
                background="#444654")  # Color de fondo del frame

# Etiqueta
label = Label(root, text="Menu Principal", font=("Arial bold", 18), bg="#444654", fg="white")  # Color de fondo de la etiqueta
label.pack(pady=20, padx=20)

# Frame para los botones
button_frame = ttk.Frame(root, style="TFrame")  # Estilo para el frame
button_frame.pack()

# Botones para cada opción
button1 = ttk.Button(button_frame, text="Visualizar Datos", command=lambda: visualizar_datos(df), style="TButton")
button1.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")

button2 = ttk.Button(button_frame, text="Aplicar Filtros", command=lambda: FILTRADO.aplicar_filtros(df,root), style="TButton")
button2.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")

button3 = ttk.Button(button_frame, text="Mostrar Gráfico", command=lambda: GRAFICAS.graficas(root), style="TButton")
button3.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

button4 = ttk.Button(button_frame, text="Calcular Variables", command=lambda: ECUACIONES.Ecuaciones(root), style="TButton")
button4.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")

button5 = ttk.Button(button_frame, text="Info Alumna", command=lambda: info(), style="TButton")
button5.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")

button6 = ttk.Button(button_frame, text="Salir del Programa", command=lambda: exit(), style="TButton")
button6.grid(row=2, column=1, padx=10, pady=5, sticky="nsew")

# Ajustar el tamaño de los botones
button_frame.grid_columnconfigure(0, weight=1, uniform="group")
button_frame.grid_columnconfigure(1, weight=1, uniform="group")

# Frame para la rejilla de datos
data_frame = ttk.Frame(root, style="TFrame")  # Estilo para el frame
data_frame.pack(pady=20)

root.mainloop()
