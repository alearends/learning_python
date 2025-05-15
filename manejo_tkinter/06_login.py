import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()

# Obtener usuario y password del .env
USUARIO_CORRECTO = os.getenv("DB_USER")
PASSWORD_CORRECTO = os.getenv("APP_PASSWORD")

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Login')
ventana.configure(background='#1d2d44')

# VENTANAS Y FRAME
# Grid de la ventana
ventana.columnconfigure(0, weight=1) # va a ocupar toda la ventana
ventana.rowconfigure(0, weight=1) # va a ocupar toda la ventana

# Agregamos un frame (marco)
frame = ttk.Frame(ventana) # objeto ventana: (ventana dentro de ventana)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=3)

# Creamos un estilo
estilos = ttk.Style()
estilos.theme_use('clam')
estilos.configure(ventana, background='#1d2d44', foreground='white',
                  fieldbackground='black')
estilos.configure('TButton', background='#005f73')
estilos.map('TButton', background=[('active', '#0a9396')])

# ETIQUETAS: 
# titulo
etiqueta = ttk.Label(frame, text='Login', font=('Arial', 20))
# etiqueta.grid(row=0, column=0)
etiqueta.grid(row=0, column=0, columnspan=2)

# usuario
usuario_etiqueta = ttk.Label(frame, text='Usuario: ')
usuario_etiqueta.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

usuario_caja_texto = ttk.Entry(frame)                                   # caja de texto
usuario_caja_texto.grid(row=1, column=1, sticky=tk.E, padx=5, pady=5)

# password
password_etiqueta = ttk.Label(frame, text='Password: ')
password_etiqueta.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

password_caja_texto = ttk.Entry(frame, show='*')                        # Las estrellas es con show= *
password_caja_texto.grid(row=2, column=1, sticky=tk.E, padx=5, pady=5)

# boton
login_boton = ttk.Button(frame, text='Enviar')
login_boton.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

def validar(event):
    usuario = usuario_caja_texto.get()
    password = password_caja_texto.get()
    
    if usuario == USUARIO_CORRECTO and password == PASSWORD_CORRECTO:
        showinfo(title='Login', message='Datos correctos!')
    else:
        showerror(title='Login', message='Datos incorrectos!')

# asociar eventos al boton de login
login_boton.bind('<Return>', validar)  # presionar la tecla de enter
login_boton.bind('<Button-1>', validar) # click izquierdo del mouse

# DESPLIEGUE
# publicamos el componente
frame.grid(row=0, column=0)

ventana.mainloop()