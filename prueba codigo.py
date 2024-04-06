import tkinter as tk
from tkinter import messagebox

def cerrar():
    confirmacion = messagebox.askquestion("Cerrar", "¿Estás seguro?", icon="warning")
    if confirmacion == "yes":
        root.destroy()  # Usa 'root' si estás cerrando la ventana principal

# Crea tu ventana principal (usa 'root' como variable)
root = tk.Tk()

# Añade tus otros widgets y diseño aquí...

# Crea el botón "Cerrar"
boton_cerrar = tk.Button(root, text="Cerrar", command=cerrar)
boton_cerrar.pack()  # O colócalo en tu diseño

# Inicia el bucle principal
root.mainloop()
