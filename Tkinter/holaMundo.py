#GUI - Graphical User Interface
#Tkinter - Tk interface
#importar le modulo de Tkinter
import tkinter as tk

#creamos un objeto usando la clase Tk
ventana = tk.Tk()

#modificamos el tamaño de la ventana (Pixeles)
ventana.geometry('600x400')
#cambiamos el nombre de la ventana
ventana.title('Hola mundo')
# Iniciamos la ventana (esta linea la ejecutamos al final )
# Si la ejecutamos antes, no se muestra los cambios anteriores
ventana.mainloop()