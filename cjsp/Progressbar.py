import tkinter as tk
from tkinter import ttk

# Crear ventana
root = tk.Tk()
root.title("Progressbar en Tkinter")
root.geometry("300x150")

# Progressbar en modo determinate
progress = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progress.pack(pady=20)

# Función para avanzar la barra
def avanzar():
    progress.step(10)  # Aumenta el progreso en 10 unidades

# Botón para iniciar el progreso
btn = tk.Button(root, text="Avanzar", command=avanzar)
btn.pack()

root.mainloop()