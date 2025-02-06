import tkinter as tk

# Crear ventana
root = tk.Tk()
root.title("Personalizar Background")
root.geometry("400x300")

# Cambiar el color de fondo de la ventana
root.config(bg="lightblue")

# Crear un label con fondo personalizado
label = tk.Label(root, text="¡Hola, Tkinter!", font=("Arial", 14), bg="lightblue", fg="white")
label.pack(pady=20)

root.mainloop()