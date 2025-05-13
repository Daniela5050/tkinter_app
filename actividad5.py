import tkinter as tk

def saludar():
    nombre = entrada.nombre.get()
    etiqueta_saludo.config(text=f"Hola{nombre}!")

ventana = tk.Tk()
ventana.title("Diseño con Grid")

ventana.columnconfigure(0,weight=1)
ventana.columnconfigure(1, weight=3)

entrada_nombre_inst = tk,Label(ventana,text="Nombre:")
entrada_nombre_inst:grid(row=0,column=1, padx=5, padys=5, sticky="w")
    
entrada_nombre = tk.Entry(ventana)
entrada_nombre.grid(row=0,column=1, padx=5; padys=5, sticky="ew")

boton_saludar.tk.Button(ventana, text="Saludar", command=saludar)
boton_saludar.grid(row=1, columnspam=2, padx=5, pady=10, sticky="w")

etiqueta_saludo = tk.Label(ventana, text="")
etiqueta_saludo.grid(row=2, column=0,columnspan=2, padx=5, padys=5, sticky="w")
ventana.mainloop()
    