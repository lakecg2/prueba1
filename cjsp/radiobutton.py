import tkinter as tk
from tkinter import messagebox

# Función para mostrar la opción seleccionada
def mostrar_seleccion():
    seleccion = var.get()
    if seleccion == 1:
        messagebox.showinfo("Selección", "Opción 1 seleccionada")
    elif seleccion == 2:
        messagebox.showinfo("Selección", "Opción 2 seleccionada")
    elif seleccion == 3:
        messagebox.showinfo("Selección", "Opción 3 seleccionada")


root = tk.Tk()
root.title("Ejemplo de Radiobutton")

# Variable para almacenar la opción seleccionada
var = tk.IntVar()

# Crear los Radiobutton
radiobutton1 = tk.Radiobutton(root, text="Opción 1", variable=var, value=1)
radiobutton1.pack(pady=5)

radiobutton2 = tk.Radiobutton(root, text="Opción 2", variable=var, value=2)
radiobutton2.pack(pady=5)

radiobutton3 = tk.Radiobutton(root, text="Opción 3", variable=var, value=3)
radiobutton3.pack(pady=5)

# Crear un botón para mostrar la selección
boton = tk.Button(root, text="Mostrar selección", command=mostrar_seleccion)
boton.pack(pady=10)

# Iniciar el bucle principal de la ventana
root.mainloop()