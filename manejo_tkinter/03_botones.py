import tkinter as tk
from tkinter import ttk

# Craemos una ventana
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Nueva Ventana')
ventana.configure(background='#1d2d44')

# Funcion Boton1
def saludar():
    print('Saludos desde el boton 1')

# Boton1
boton1 = ttk.Button(ventana, text='Enviar', command=saludar) # NO se escribe command=saludar() porque si no queda "ejecutado" al clicar el boton


# Funcion Boton2 
def saludar(nombre):
    print(f'Saludos desde el boton 2 --> Hola {nombre}')


boton2 = ttk.Button(ventana, text='Enviar', command=lambda: saludar('Juan'))

# ------------------------------------------------

# Publicamos el componente
boton1.pack(pady=20)
boton2.pack(pady=50)
# Desplegamos
ventana.mainloop()