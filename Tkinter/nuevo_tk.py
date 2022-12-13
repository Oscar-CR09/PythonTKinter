import  tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('manejo de Grid')
ventana.iconbitmap('Tkinter\logo.ico')

#configurar rl grid 

ventana.rowconfigure(0,weigh=2)
ventana.rowconfigure(1,weigh=10)
ventana.columnconfigure(0,weigh=1)
ventana.columnconfigure(1,weigh=5)
# Metodo de los eventos 
def evento1():
    boton1.config(text='Boton 1 presionado')


def evento2():
    boton2.config(text='Boton 2 presionado')

def evento4():
    boton4.config(text='Boton 4 precionado', fg='blue',relief=tk.GROOVE, bg='yellow')

#definimos dos botones
boton1 = ttk.Button(ventana, text= 'Boton 1 ',command=evento1)
boton1.grid(row=0,column=0,sticky='NSWE',padx=40,pady=30,ipadx=20,ipady=50)

# n(arriba), e(derecha) s(abajo) w(izquierda) 
boton2 = ttk.Button(ventana, text='Boton 2 ', command=evento2)
boton2.grid(row=1, column=0, sticky='NSWE')

#boton 3
boton3 = ttk.Button(ventana, text='Boton 3')
boton3.grid(row=0, column=1, sticky='NSWE')

boton4 = tk.Button(ventana, text='Boton 4', command=evento4)
boton4.grid(row=1, column=1, sticky='NSWE')

ventana.mainloop()

