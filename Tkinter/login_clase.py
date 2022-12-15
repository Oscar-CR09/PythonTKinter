import tkinter as tk
from tkinter import ttk, messagebox

class LoginVentana(tk.Tk):
    def __init__(self):
        super().__init__()

        #ventana principal
        self.geometry('300x150')
        self.title('Login')
        self.iconbitmap('Tkinter\logo.ico')
        self.resizable(0, 0)

        #configuracion del grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        self._crear_componentes()
        #definir el metodo crear componentes
    def _crear_componentes(self):

        #usuario
        usuario_etiqueta1 = tk.Label(self, text='Usuario')
        usuario_etiqueta1.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)

        entrada_valor1 = tk.StringVar(value='Nombre')
        self.usuario_entrada1 = ttk.Entry(self, width=30, textvariable=entrada_valor1)
        self.usuario_entrada1.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        #password
        password_etiqueta = tk.Label(self, text='password')
        password_etiqueta.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)

        self.password_entrada = ttk.Entry(self, show='*')
        self.password_entrada.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        #boton
        login_boton = ttk.Button(self, text='Login', command=self._login)
        login_boton.grid(row=3, column=0, columnspan=2)


    def _login(self):
        messagebox.showinfo(
            'Datos Login', f'Usuario: {self.usuario_entrada1.get()}, Password: {self.password_entrada.get()}')


#ejecutar ventana
if __name__ == '__main__':
    login_ventana = LoginVentana()
    login_ventana.mainloop()