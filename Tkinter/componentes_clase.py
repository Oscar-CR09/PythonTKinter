import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from time import sleep

class ComponentesVentana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x400+700+300')
        self.title('Componentes')
        self.iconbitmap('Tkinter\logo.ico')
        self._crear_tabs()

    def _crear_componentes_tabulador1(self,tabulador):
        #agregar una etiqueta y un componente de entrada
        etiqueta1 = ttk.Label(tabulador, text='Nombre')
        etiqueta1.grid(row=0, column=0, sticky=tk.E)
        entrada1 = ttk.Entry(tabulador, width=30)
        entrada1.grid(row=0, column=1, padx=5, pady=5)

        def enviar():
            messagebox.showinfo('Mensaje', f'Nombr: {entrada1.get()}')

        boton1 = ttk.Button(tabulador, text='Enviar', command=enviar)
        boton1.grid(row=1, column=0, columnspan=2)
        #agregamos un boton


    def _crear_componentes_tabulador2(self,tabulador):
        contenido = 'Este es mi texto con el contenido'
        #creamos el componente de scroll
        scroll = scrolledtext.ScrolledText(
            tabulador, width=50, height=10, wrap=tk.WORD)
        scroll.insert(tk.INSERT, contenido)
        #mostramos el componente
        scroll.grid(row=0, column=0)


    def _crear_componentes_tabulador3(self,tabulador):
        #creamos una lista usando data list comprehension
        datos = [x+1 for x in range(100, 110)]
        combobox = ttk.Combobox(tabulador, width=15, values=datos)
        combobox.grid(row=0, column=0, padx=10, pady=10)
        #seleccionar un elemento pro mostrar
        combobox.current(5-1)
        #agregar un boton que opcion selecciono el usuaro

        def mostrar_valor():
            messagebox.showinfo('valor seleccionado',
                                f'valor seleccionado: {combobox.get()}')

        boton1 = ttk.Button(
            tabulador, text='mostrar valor seleccionado', command=mostrar_valor)
        boton1.grid(row=0, column=1)


    def _crear_componentes_tabulador4(self,tabulador):
        imagen = tk.PhotoImage(file='Tkinter/image.png')

        def mostrar_titulo():
            messagebox.showinfo('mas info imagen',
                                f'Nombre imagen: {imagen.cget("file")}')
        boton_imagen = ttk.Button(tabulador, image=imagen, command=mostrar_titulo)
        boton_imagen.grid(row=0, column=0)


    def _crear_componentes_tabulador5(self,tabulador):
        #creamos el componentes el de barra
        barra_progreso = ttk.Progressbar(
            tabulador, orient='horizontal', length=550)
        barra_progreso.grid(row=0, column=0, padx=10, pady=10, columnspan=4)
        #Metodos para controlar los eventos de la barra de progreso

        def ejecutar_barra():
            barra_progreso['maximum'] = 100
            for valor in range(101):
                #se manda esprar un poco antes de continuarcon la ejecucion
                sleep(0.05)
                #incrementamos la barra de progreso
                barra_progreso['value'] = valor
                #actualizar la barra de progreso
                barra_progreso.update()
                barra_progreso['value'] = 0

        def ejecutar_ciclo():
            barra_progreso.start()

        def detener():
            barra_progreso.stop()

        def detener_despues():
            esperar_ms = 1000
            self.after(esperar_ms, barra_progreso.stop)

        #botones para controlar los eventos de una barra de proggreso
        boton_inicio = ttk.Button(
            tabulador, text='ejecutar barra de progreso', command=ejecutar_barra)
        boton_inicio.grid(row=1, column=0)

        boton_ciclo = ttk.Button(
            tabulador, text='Ejecutar ciclo', command=ejecutar_ciclo)
        boton_ciclo.grid(row=1, column=1)
        boton_detener = ttk.Button(
            tabulador, text='Detener Ejecución', command=detener)
        boton_detener.grid(row=1, column=2)
        boton_despues = ttk.Button(
            tabulador, text=' Detener ejecucion despues', command=detener_despues)
        boton_despues.grid(row=1, column=3)


    def _crear_tabs(self):
        #creamos un tab control, para ello usamos la clase notebook
        control_tabulador = ttk.Notebook(self)
        #agregmos un marco (frame)para agregar dentro del tab y organizar los elementos
        tabulador1 = ttk.Frame(control_tabulador)
        #agragamos el tabulador al control de tabuladores
        control_tabulador.add(tabulador1, text='Tabulador 1')
        #mostramos el tabulador
        control_tabulador.pack(fill='both')
        #creamos los componentes del tabulador 1
        self._crear_componentes_tabulador1(tabulador1)
        #creamosun segundo tabulador
        tabulador2 = ttk.LabelFrame(control_tabulador, text='contenido')
        control_tabulador.add(tabulador2, text='Tabulador 2')
        #creamos los componentes del segundo tabulador
        self._crear_componentes_tabulador2(tabulador2)
        #creamos un tercer tabulador
        tabulador3 = ttk.Frame(control_tabulador)
        control_tabulador.add(tabulador3, text='Tabulador 3')
        #creamos los componentesdel tercer tabulador
        self._crear_componentes_tabulador3(tabulador3)
        #cuarto tabulador
        tabulador4 = ttk.LabelFrame(control_tabulador, text='imagen')
        control_tabulador.add(tabulador4, text='Tabulador 4')
        #crear los componentes del tabulador
        self._crear_componentes_tabulador4(tabulador4)
        #crear quinto tabulador
        tabulador5 = ttk.LabelFrame(control_tabulador, text='Progress bar')
        control_tabulador.add(tabulador5, text='Tabulador 5')
        #creamos los componentes del quinto tabulador
        self._crear_componentes_tabulador5(tabulador5)


if __name__ == '__main__':
    #creamos un objeto de la clase
    componente_ventana = ComponentesVentana()
    componente_ventana.mainloop()
