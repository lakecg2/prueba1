import tkinter as tk
from tkinter import messagebox

# Función para mostrar diferentes tipos de messagebox
def mostrar_messagebox():
    # Mostrar un messagebox de información
    messagebox.showinfo("Información", "Este es un mensaje de información.")
    
    # Mostrar un messagebox de advertencia
    messagebox.showwarning("Advertencia", "Este es un mensaje de advertencia.")
    
    # Mostrar un messagebox de error
    messagebox.showerror("Error", "Este es un mensaje de error.")
    
    # Mostrar un messagebox de pregunta (sí/no)
    respuesta = messagebox.askyesno("Pregunta", "¿Te gusta Tkinter?")
    if respuesta:
        messagebox.showinfo("Respuesta", "¡Genial! Te gusta Tkinter.")
    else:
        messagebox.showinfo("Respuesta", "Oh, tal vez prefieras otra librería.")
    
    # Mostrar un messagebox de pregunta (ok/cancelar)
    respuesta = messagebox.askokcancel("Confirmación", "¿Deseas continuar?")
    if respuesta:
        messagebox.showinfo("Respuesta", "Has elegido continuar.")
    else:
        messagebox.showinfo("Respuesta", "Has elegido cancelar.")

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de Messagebox")

# Crear un botón para mostrar los messagebox
boton = tk.Button(root, text="Mostrar Messagebox", command=mostrar_messagebox)
boton.pack(pady=20)

# Iniciar el bucle principal de la ventana
root.mainloop()