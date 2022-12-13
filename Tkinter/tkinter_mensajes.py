import tkinter as tk
from tkinter import ttk, messagebox

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('manejo de componentes')
ventana.iconbitmap('Tkinter\logo.ico')
#etiqueta
etiqueta1 = tk.Label(ventana, text='Aqui se mostrara el contenido de la caja de texto')
etiqueta1.grid(row=1, column=0, columnspan=2)

entrada_var1 = tk.StringVar(value='valor por default')
entrada1 = ttk.Entry(ventana, width=30)

entrada1.grid(row=0, column=0)


def enviar():

    #modificamos el texto de label
    etiqueta1.config(text=entrada1.get())
    #messagebox o cajas de mensajes 
    mensaje1=entrada1.get()
    
    if mensaje1:
        messagebox.showinfo('Mensaje informativo ', mensaje1 + 'informativo')
        messagebox.showerror('Mensaje error', mensaje1 + 'error' )
        messagebox.showwarning('Mensaje alerta', mensaje1 + 'Alerta')


boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)


ventana.mainloop()
