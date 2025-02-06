import tkinter as tk

# Crear ventana
root = tk.Tk()
root.title("Ejemplo de Grid")
root.geometry("300x200")

# Crear etiquetas y campos de entrada con grid
tk.Label(root, text="Nombre:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
tk.Entry(root).grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Correo:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
tk.Entry(root).grid(row=1, column=1, padx=5, pady=5)

# Botón centrado en dos columnas
tk.Button(root, text="Enviar").grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()