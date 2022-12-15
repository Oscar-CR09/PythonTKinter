import tkinter as tk
from tkinter import ttk, messagebox

#class Login(tk.Tk):
#    def __init__(self):
#        super().__init__()


#ventana principal
ventana=tk.Tk()
ventana.geometry('300x150')
ventana.title('Login')
ventana.iconbitmap('Tkinter\logo.ico')
ventana.resizable(0,0)

#configuracion del grid
ventana.columnconfigure(0,weight=1)
ventana.columnconfigure(1,weight=3)
#usuario
usuario_etiqueta1 = tk.Label(ventana, text='Usuario')
usuario_etiqueta1.grid(row=0, column=0,sticky=tk.E,padx=5,pady=5)

entrada_valor1 = tk.StringVar(value='Nombre')
usuario_entrada1 = ttk.Entry(ventana,width=30,textvariable=entrada_valor1)
usuario_entrada1.grid(row=0,column=1,sticky=tk.W,padx=5,pady=5)

#password
password_etiqueta = tk.Label(ventana,text='password')
password_etiqueta.grid(row=1,column=0,sticky=tk.E,padx=5,pady=5)

password_entrada = ttk.Entry(ventana,show='*')
password_entrada.grid(row=1,column=1,sticky=tk.W,padx=5,pady=5)

#boton 
def login():
    messagebox.showinfo('Datos Login', f'Usuario: {usuario_entrada1.get()}, Password: {password_entrada.get()}')


login_boton =ttk.Button(ventana, text='Login',command=login)
login_boton.grid(row=3,column=0,columnspan=2)



ventana.mainloop()