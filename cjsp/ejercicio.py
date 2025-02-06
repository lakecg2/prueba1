import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Formulario de Registro")
ventana.geometry("400x600")
ventana.config(bg="lightblue")

# Cargar y redimensionar la primera imagen
imagen1 = Image.open("GBmqMR7XYAA4_qY.jpg")
imagen1 = imagen1.resize((100, 100))  # Redimensionar si es necesario
imagen1_tk = ImageTk.PhotoImage(imagen1)

# Crear el Label con la primera imagen
label_imagen1 = tk.Label(ventana, image=imagen1_tk)

# Cargar y redimensionar la segunda imagen
imagen2 = Image.open("GBmqMR7XYAA4_qY.jpg")  # Cambia este nombre si es diferente
imagen2 = imagen2.resize((100, 100))  # Redimensionar si es necesario
imagen2_tk = ImageTk.PhotoImage(imagen2)

# Crear el Label con la segunda imagen
label_imagen2 = tk.Label(ventana, image=imagen2_tk)

# Crear el Label con el texto "ICC"
carrera = tk.Label(
    ventana,
    text="ICC",
    bg="lightblue",
    font=("Arial", 20, "bold"),
    padx=20,
    pady=10
)

# Crear el Label con el texto "DATOS"
datos = tk.Label(
    ventana,
    text="DATOS",
    bg="lightblue",
    font=("Arial", 20, "bold"),
    padx=20,
    pady=10
)

# Organizar los elementos en el grid
label_imagen1.grid(row=0, column=0, padx=10, pady=10)  # Coloca la imagen 1 en la columna 0
carrera.grid(row=0, column=1, padx=10, pady=10)        # Coloca el texto "ICC" en la columna 1
label_imagen2.grid(row=0, column=2, padx=10, pady=10)  # Coloca la imagen 2 en la columna 2
datos.grid(row=1, column=0, columnspan=3, padx=10, pady=20)  # Coloca el texto "DATOS" en la fila 1, abarcando las 3 columnas

# Configurar las columnas para un layout adecuado
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=2)  # La columna del texto puede ocupar más espacio
ventana.grid_columnconfigure(2, weight=1)

ventana.mainloop()
