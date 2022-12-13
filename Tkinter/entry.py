import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('manejo de componentes')
ventana.iconbitmap('Tkinter\logo.ico')
#width es la cantidad de caracteres que ocupa la caja 
#entrada1 = ttk.Entry(ventana,width=30,justify=tk.CENTER,show='*')
#state=tk.DISABLE

#definimos una variable que podemos modificar posteriomente (set), leer (get)
entrada_var1 = tk.StringVar(value='valor por default')
entrada1 = ttk.Entry(ventana, width=30, textvariable=entrada_var1)
#entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER, state=tk.NORMAL)
entrada1.grid(row=0,column=0)
#insert agrega un texto a la caja de texto
#entrada1.insert(0, 'Introduce una cadena ')
#entrada1.insert(5, '-')
#entrada1.config(state='readonly')
def enviar():
    #recuperamos la informacion a partir de la variable asociada con la caja de texto
    boton1.config(text=entrada_var1.get())
    #modificacacion utilizamos la variable de texto y el emtodo set
    entrada_var1.set('cambio...')
    #recuperarmos la informacion 
    print(entrada_var1.get())
    print(entrada1.get())
#creamos un boton
#  
boton1=ttk.Button(ventana,text='Enviar',command=enviar)
boton1.grid(row=0,column=1)



ventana.mainloop()

'''
def enviar():
    print(entrada1.get())
    boton1.config(text=entrada1.get())
    #eliminir el contenido
    #entrada1.delete(0,tk.END)
    #selecionar el texto de la caja
    entrada1.select_range(0, tk.END)
    #para hacerl efectivo la selccion del texto
    entrada1.focus()
'''