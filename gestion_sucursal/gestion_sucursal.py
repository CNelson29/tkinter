import tkinter  as tk
from cliente.interfaz_app import Frame
def main():
    root = tk.Tk()
    root.title("Registro unapec")
    root.iconbitmap("img/icon unapec.ico")
    """root.geometry("1000x650")"""
    root.resizable(0,0)
    
    app = Frame(root = root)






    root.mainloop()

if __name__ == '__main__':
    main()


