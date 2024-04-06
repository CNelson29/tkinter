from tkinter import*
import sys

#configuraciones
root = Tk()
root.title("Registro unapec")
root.iconbitmap("img/icon unapec.ico")
root.geometry("1000x650")
root.resizable(0,0)
#defs
def cerrar ():
    sys.exit()

#variables
nombre = StringVar()
contra = StringVar()
#main
Registro = Label(root,text="Registro Unapec" )
Registro.place(x=450, y=50)
#empieza registro
nombre = Label(root, text="Ingrese su nombre")
nombre.place(x = 250, y= 100)
cont = Label(root, text="Ingrese su nombre")
cont.place(x = 250, y= 180)
#campos de ingresar texto
entrNombre = Entry(root, textvariable=nombre)
entrNombre.place(x= 400,y=100)
entrCont = Entry(root, textvariable=contra)
entrCont.place(x= 400,y=180)
#botones
boton1 = Button(root, text=" Exit", command=cerrar)
boton1.place(x=500,y=250)
boton2 = Button(root, text=" login")
boton2.place(x=450,y=250)

root.mainloop()
