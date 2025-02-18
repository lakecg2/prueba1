import tkinter as tk
from backend import Joaquin
from tkinter import messagebox

def registrar():
    Nombre = obt_nombre.get()
    Edad = obt_edad.get()
    Sangre = obt_sangre.get()

    Joaquin(Nombre, Edad, Sangre)
    messagebox.showinfo("Registro Exitoso", f"El usuario {Nombre} quedó registrado")
    obt_nombre.delete(0, tk.END)
    obt_edad.delete(0, tk.END)
    obt_sangre.delete(0, tk.END)

ventana1 = tk.Tk()
ventana1.title("Ventana de Registro")
ventana1.geometry("500x400")

etiqueta_nom = tk.Label(ventana1, text="Nombre")
etiqueta_nom.pack(pady=8)
obt_nombre = tk.Entry(ventana1)
obt_nombre.pack(pady=8)

etiqueta_edad = tk.Label(ventana1, text="Edad")
etiqueta_edad.pack(pady=8)
obt_edad = tk.Entry(ventana1)
obt_edad.pack(pady=8)

etiqueta_sangre = tk.Label(ventana1, text="Tipo de Sangre")
etiqueta_sangre.pack(pady=8)
obt_sangre = tk.Entry(ventana1)
obt_sangre.pack(pady=8)


def mostrarlista():
    ventana2 = tk.Toplevel()
    ventana2.title("Lista de los usuarios")
    ventana2.geometry("450x450")
    listausuario = Joaquin.mostarusuarios()

    for i, usuario in enumerate(listausuario, start=1):
        etiqueta_usuario = tk.Label(ventana2, text=usuario.mostrarinfo())
        etiqueta_usuario.grid(row=i, column=0, sticky="w", padx=10, pady=5)

        def editar_usuario(indice=i):
            usuario_a_editar = listausuario[indice]
            ventana_editar = tk.Toplevel(ventana2)
            ventana_editar.title("Editar Usuario")

            nuevo_nombre = tk.Entry(ventana_editar)
            nuevo_nombre.insert(0, usuario_a_editar.nombre)
            nuevo_nombre.pack(pady=8)

            nuevo_edad = tk.Entry(ventana_editar)
            nuevo_edad.insert(0, usuario_a_editar.edad)
            nuevo_edad.pack(pady=8)

            nuevo_sangre = tk.Entry(ventana_editar)
            nuevo_sangre.insert(0, usuario_a_editar.tiposangre)
            nuevo_sangre.pack(pady=8)

            def guardar_edicion():
                nuevo_nombre_val = nuevo_nombre.get()
                nuevo_edad_val = nuevo_edad.get()
                nuevo_sangre_val = nuevo_sangre.get()

                Joaquin.editar_usuario(indice, nuevo_nombre_val, nuevo_edad_val, nuevo_sangre_val)
                ventana_editar.destroy()
                ventana2.destroy() 
                mostrarlista()

            boton_guardar = tk.Button(ventana_editar, text="Guardar", command=guardar_edicion)
            boton_guardar.pack(pady=8)

        botoneditar = tk.Button(ventana2, text="Editar", padx=10, command=editar_usuario)
        botoneditar.grid(row=i, column=1, padx=10, pady=5)

        def eliminar_usuario(indice=i):
            try:
                Joaquin.eliminar_usuario(indice)
                ventana2.destroy()
                mostrarlista()
            except IndexError:
                messagebox.showerror("Error", "No se pudo eliminar el usuario.")

        botoneliminar = tk.Button(ventana2, text="Eliminar", padx=12, command=eliminar_usuario)
        botoneliminar.grid(row=i, column=2, padx=10, pady=5)

    ventana2.mainloop()


boton1 = tk.Button(ventana1, text="Registrar", command=registrar)
boton1.pack(pady=8)

boton2 = tk.Button(ventana1, text="Mostrar lista", command=mostrarlista)
boton2.pack()

ventana1.mainloop()
