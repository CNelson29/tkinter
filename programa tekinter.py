from tkinter import*
from pro import *
import sys
root = Tk()
root.title("UNAPEC")#primer titulo de gestor de cafeterias 
root.geometry("1000x650")# tamano de pantalla
root.iconbitmap("icon unapec.ico")#logo unapec
root.resizable(0,0)#adaptar margen de pantalla desactivado.
texto = Label(root, text="Gestion de Cafeteria UNAPEC", font="14")
texto.place(x=390, y=10)
#defs - metodos
def salir():
    sys.exit()
def cerrar():
    menssageBox = asuestion("cerrar" , Message("estas segoro?"))
#def agregar():
    #listaProductos1.insert(END,nuevoproducto.get())
def ventanaAgregar():
    ventanaAgregar = Toplevel()
    root.withdraw()
    ventanaAgregar.deiconify()
    ventanaAgregar.title("UNAPEC")#primer titulo de gestor de cafeterias 
    ventanaAgregar.geometry("1000x650")# tamano de pantalla
    ventanaAgregar.iconbitmap("icon unapec.ico")#logo unapec
    ventanaAgregar.resizable(0,0)#adaptar margen de pantalla desactivado.
    texto1 = Label(ventanaAgregar, text="Gestion de Cafeteria UNAPEC", font="14")
    texto1.place(x=390, y=10)
    #gets
    def agregar():
        listaProductos1.insert(END,nuevoproducto1.get())
    #Productos

    productos1 = Label(ventanaAgregar, text="")
    productos1.place(x=450,y=120)

    #listado de productos

    listaProductos1 = Listbox(ventanaAgregar, width=20,height=5)
    listaProductos1.insert(0,"caramelo")
    listaProductos1.insert(1,"bolon")
    listaProductos1.insert(2,"paleta")
    listaProductos1.place(x=20,y=160)

    #eliminar productos - posibilidad
    #listaProductos.delete()
    #insertar nuevo producto

    nuevoproducto1 = Entry(ventanaAgregar,bd=10)
    boton31 = Button(ventanaAgregar, text="agregar producto", command=agregar)
    nuevoproducto1.place(x=450,y=350)
    boton31.place(x=450,y=390)

    atras = Button(ventanaAgregar,text=" atras", command=darParaAtras).place(x=120,y=20)

def darParaAtras():
    root.deiconify()
    ventanaAgregar.withdraw() 





#texto.grid(row=0 , column=1)
catalogo = Button(root, text= "Catalogo")
#catalogo.grid(row = 1, column = 0)
catalogo.place(x=20, y=40)

campus = Button(root, text= "Campus")
campus.place(x=20, y=80)

salir = Button(root, text= "Salir del programa", command=cerrar)
#salir = Button(root, text= "Salir del programa", command=root.quit)
salir = Button(root, text= "Salir del programa", command=root.quit)
salir.place(x=450, y=550)

#Menu
menuban = Menu(root)
root.config(menu=menuban)
archivoMenu = Menu(menuban)
archivoMenu.add_command(label="ver productos")
archivoMenu.add_command(label="agregar productos",command=ventanaAgregar)
archivoMenu.add_command(label="Exportar e importar")
#sucursales
sucursalesMenu = Menu(menuban)
sucursalesMenu.add_command(label="sucursales")
sucursalesMenu.add_command(label="agregar sucursal")
sucursalesMenu.add_command(label="exportar importar")
menuban.add_cascade(label="Archivo", menu=archivoMenu)
menuban.add_cascade(label="Sucursal", menu=sucursalesMenu)

#Productos

#productos = Label(root, text="")
#productos.place(x=20,y=120)

#listado de productos

#listaProductos = Listbox(root, width=20,height=5)
#listaProductos.insert(0,"caramelo")
#listaProductos.insert(1,"bolon")
#listaProductos.insert(2,"paleta")
#listaProductos.place(x=20,y=160)

#eliminar productos - posibilidad

#listaProductos.delete()

#insertar nuevo producto

#nuevoproducto = Entry(root,bd=10)
#boton3 = Button(root, text="agregar producto", command=agregar)
#nuevoproducto.place(x=20,y=350)
#boton3.place(x=20,y=390)






















root.mainloop()