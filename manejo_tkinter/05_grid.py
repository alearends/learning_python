import tkinter as tk
from tkinter import ttk

# Craemos una ventana
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Nueva Ventana')
ventana.configure(background='#1d2d44')

# Manejo de grid (rejilla o cuadricula)
boton1 = ttk.Button(ventana, text='Boton1')
boton2 = ttk.Button(ventana, text='Boton2')
boton3 = ttk.Button(ventana, text='Boton3')

# Configurar el grid
ventana.columnconfigure(0, weight=1) # Si se quiere mas amplio weight=10
ventana.columnconfigure(1, weight=1) # Si se quiere mas amplio weight=10
ventana.columnconfigure(2, weight=1) # Si se quiere mas amplio weight=10

ventana.rowconfigure(0, weight=1) # Si se quiere mas amplio weight=10
ventana.rowconfigure(1, weight=1) # Si se quiere mas amplio weight=10
ventana.rowconfigure(2, weight=1) # Si se quiere mas amplio weight=10

# BOTONES UBICADO EN EL CENTRO DE LA REJILLA:

# Publicando de manera horizontal
# boton1.grid(row=0, column=0)
# boton2.grid(row=0, column=1)
# boton3.grid(row=0, column=2)

# Publicar de manera vertical
# boton1.grid(row=0, column=0)
# boton2.grid(row=1, column=0)
# boton3.grid(row=2, column=0)

# Publicar en diagonal
# boton1.grid(row=0, column=0)
# boton2.grid(row=1, column=1)
# boton3.grid(row=2, column=2)

# BOTONES DESCENTRADOS DENTRO DE LA REJILLA:

# Publicando de manera horizontal
# boton1.grid(row=0, column=0, sticky=tk.NSEW) # sticky: pegado al norte(arriba), S(abajo), Este(izquierda), West(derecha) 
# boton2.grid(row=0, column=1, sticky=tk.SE) # sticky: pegado al S(abajo), Este(izquierda)
# boton3.grid(row=0, column=2, sticky=tk.NW) # sticky: pegado al norte(arriba), West(derecha)  

# AGREGANDO PADDING

# Publicando de manera horizontal
boton1.grid(row=0, column=0, padx=20, pady=20, ipadx=30, ipady =30) # pad: padding externo  // ipad: padding interno (margin)
boton2.grid(row=0, column=1, sticky=tk.SE, ipadx= 20, ipady=20) # pad: padding externo  // ipad: padding interno (margin)
boton3.grid(row=0, column=2, sticky=tk.NW) # para comparar no se coloco padding -> Se ubica por default en el centro de su rejilla 


ventana.mainloop()