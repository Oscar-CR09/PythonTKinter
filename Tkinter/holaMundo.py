#GUI - Graphical User Interface
#Tkinter - Tk interface
#importar le modulo de Tkinter
import tkinter as tk
#importamos el modulo del tema tkinter
from tkinter import ttk
#creamos un objeto usando la clase Tk
ventana = tk.Tk()

#modificamos el tamaño de la ventana (Pixeles)
ventana.geometry('600x400')
#cambiamos el nombre de la ventana
ventana.title('Hola mundo')
#configura el icono de la aplicacion debe de estar en la raiz o 
#o indicar la ruta 
ventana.iconbitmap('logo.ico')

#creamos un boton (widget), el objeto padre es ventana
boton1 = ttk.Button(ventana, text='Dar clik')
#utilizar el pack layout manager para mostrar el boton de la ventana
boton1.pack()

# Iniciamos la ventana (esta linea la ejecutamos al final )
# Si la ejecutamos antes, no se muestra los cambios anteriores
ventana.mainloop()