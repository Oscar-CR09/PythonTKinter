import tkinter as tk
from tkinter import ttk, messagebox,Menu

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('manejo de componentes')
ventana.iconbitmap('Tkinter\logo.ico')

etiqueta1 = tk.Label(ventana, text='Aqui se mostrara el contenido de la caja de texto')
etiqueta1.grid(row=1, column=0, columnspan=2)

entrada_var1 = tk.StringVar(value='valor por default')
entrada1 = ttk.Entry(ventana, width=30)

entrada1.grid(row=0, column=0)


def enviar():
    etiqueta1.config(text=entrada1.get())
    mensaje1 = entrada1.get()

    if mensaje1:
        messagebox.showinfo('Mensaje informativo ', mensaje1 + 'informativo')

def crear_menu():
    #configurar el menu principal 
    menuprincipal= Menu(ventana)
    #teaoff = false para evitar que se separe del menu del interfas
    submenu_archivo = Menu(menuprincipal, tearoff=0)
    #agregamos una nueva opcion al menu de archivo 
    submenu_archivo.add_command(label='Nuevo')
    #agregamos el submenu al menu
    menuprincipal.add_cascade(menu=submenu_archivo, label='Archivo')
    #mostramos el muenu en la ventana principal 
    ventana.config(menu=menuprincipal)

boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)

crear_menu()

ventana.mainloop()
