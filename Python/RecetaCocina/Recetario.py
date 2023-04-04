import tkinter as tk
import json
from tkinter import filedialog
from PIL import ImageTk, Image

from tkinter import messagebox


class Receta:
    
    """Se define la clase Receta"""
    
    def __init__(self, nombre, ingredientes, instrucciones, imagen, tiempoPreparacion ,tiempoCoccion , favorito=False):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.instrucciones = instrucciones
        self.imagen = imagen
        self.favorito = favorito
        self.tiempoPreparacion = tiempoPreparacion
        self.tiempoCoccion = tiempoCoccion
        
class Ingrediente:
    def __init__( self, nombre, unidadMedida, cantidad ):
        self.nombre = nombre
        self.unidadMedida = unidadMedida
        self.cantidad = cantidad
        
class Recetario:
    """Se define la clase Recetario"""
    def __init__(self):
        self.recetas = []
        

    def agregar_receta(self, receta):
        self.recetas.append(receta)

    def eliminar_receta(self, receta):
        self.recetas.remove(receta)

    def modificar_receta(self, receta, nuevo_nombre, nuevos_ingredientes, nuevas_instrucciones, nueva_imagen):
        receta.nombre = nuevo_nombre
        receta.ingredientes = nuevos_ingredientes
        receta.instrucciones = nuevas_instrucciones
        receta.imagen = nueva_imagen

    def ver_receta(self, receta):
       limpiar_formulario()
       nombre_entry.insert(0, receta.nombre)
       ingredientes_text.insert(tk.INSERT, receta.ingredientes)
       instrucciones_text.insert(tk.INSERT, receta.instrucciones)
       imagen_path.set(receta.nombre+".png")
       imagen = Image.open(receta.nombre+".png")
       imagen.thumbnail((300, 300))
       imagen = ImageTk.PhotoImage(imagen)
       imagen_label.config(image=imagen)
       imagen_label.image = imagen


def cargar_recetas():
    recetario = Recetario()
    with open("recetas.csv", "r",encoding="utf-8") as archivo:
        recetas = json.load(archivo)
        for receta in recetas["recetas"]:
            nombre = receta["nombre"]
            ingredientes = receta["ingredientes"]
            instrucciones = receta["instrucciones"]
            imagen = receta["imagen"]
            tiempoPreparacion = receta["tiempoPreparacion"]
            tiempoCoccion = receta["tiempoCoccion"]
            favorito = receta["favorito"]
            receta = Receta(nombre, ingredientes, instrucciones, imagen,tiempoPreparacion,tiempoCoccion, favorito)
            recetario.agregar_receta(receta)
    return recetario

def guardar_recetas(recetario):
            
    with open("recetas.json", "r+",encoding="utf-8") as archivo:
        json_data = json.load(archivo)
        for receta in recetario.recetas:
            recetaDict = {
                "nombre":receta.nombre, 
                "ingredientes":receta.ingredientes,
                "instruciones":receta.instrucciones,
                "imagen":receta.imagen,
                "favorito":receta.favorito,
                "tiempoPreparacion": receta.tiempoPreparacion,
                "tiempoCoccion": receta.tiempoCoccion
                }
            json_data["recetas"].append(recetaDict)
        json.dumps(json_data,archivo,ensure_ascii=False,indent=4)
            
            

def agregar_receta():
    nombre = nombre_entry.get()
    ingredientes = ingredientes_text.get("1.0", "end-1c")
    instrucciones = instrucciones_text.get("1.0", "end-1c")
    imagen = imagen_path.get()
    tiempoPreparacion
    tiempoCoccion 
    favorito = False
    
    receta = Receta(nombre, ingredientes, instrucciones, imagen, favorito)
    recetario.agregar_receta(receta)
    guardar_recetas(recetario)
    limpiar_formulario()
    actualizar_lista_recetas()

def eliminar_receta():
    indice = lista_recetas.curselection()
    if indice:
        receta = recetario.recetas[indice[0]]
    
    if not indice:
            messagebox.showwarning("Advertencia", "Selecciona una receta para eliminar.")
            return

    respuesta = messagebox.askyesno("Eliminar receta", "¿Estás seguro de que deseas eliminar esta receta?")
    if  not respuesta:
            return
    recetario.eliminar_receta(receta)
    lista_recetas.delete(indice)
    guardar_recetas(recetario)
    actualizar_lista_recetas()
    
def modificar_receta():
    seleccion = lista_recetas.curselection()
    if seleccion:
        receta = recetario.recetas[seleccion[0]]
        nuevo_nombre = nombre_entry.get()
        nuevos_ingredientes = ingredientes_text.get("1.0", "end-1c")
        nuevas_instrucciones = instrucciones_text.get("1.0", "end-1c")
        nueva_imagen = imagen_path.get()
        recetario.modificar_receta(receta, nuevo_nombre, nuevos_ingredientes, nuevas_instrucciones, nueva_imagen)
        guardar_recetas(recetario)
        limpiar_formulario()
        actualizar_lista_recetas()
        
def ver_receta():
    seleccion = lista_recetas.curselection()
    if seleccion:
        receta = recetario.recetas[seleccion[0]]
        recetario.ver_receta(receta)
    
def mostrar_recetas():
     cursor = lista_recetas.curselection()
     if cursor:
        receta = recetario.recetas[cursor[0]]
        recetario.ver_receta(receta)
def marcar_favorito():
    seleccion = lista_recetas.curselection()
    if seleccion:
        receta = recetario.recetas[seleccion[0]]
        receta.favorito = not receta.favorito
        guardar_recetas(recetario)
        actualizar_lista_recetas()

def cargar_imagen():
    ruta_imagen = filedialog.askopenfilename()
    imagen_path.set(ruta_imagen)
    imagen = Image.open(ruta_imagen)
    imagen.thumbnail((300, 300))
    imagen = ImageTk.PhotoImage(imagen)
    imagen_label.config(image=imagen)
    imagen_label.image = imagen

def actualizar_lista_recetas():
    lista_recetas.delete(0, tk.END)
    for receta in recetario.recetas:
        lista_recetas.insert(tk.END, receta.nombre)

def limpiar_formulario():
    nombre_entry.delete(0, tk.END)
    ingredientes_text.delete("1.0", tk.END)
    instrucciones_text.delete("1.0", tk.END)
    imagen_path.set("")
    imagen_label.config(image=None)
    
    



root = tk.Tk()
root.title("Recetario")


root.geometry('1480x800')

recetario = cargar_recetas()

nombre_label = tk.Label(root, text="Nombre:")
nombre_label.grid(row=0, column=4, padx=5, pady=5,  sticky="w")

nombre_entry = tk.Entry(root)
nombre_entry.grid(row=0, column=4, padx=60, pady=5, sticky="w")

ingredientes_label = tk.Label(root, text="Ingredientes:")
ingredientes_label.grid(row=1, column=4, padx=5, pady=5, sticky="nw")

ingredientes_text = tk.Text(root, height=10)
ingredientes_text.grid(row=2, column=4, padx=5, pady=5,sticky="nw")

instrucciones_label = tk.Label(root, text="Instrucciones:")
instrucciones_label.grid(row=4, column=4, padx=5, pady=5, sticky="w")

instrucciones_text = tk.Text(root, height=10)
instrucciones_text.grid(row=5, column=4, padx=5, pady=5)

imagen_label = tk.Label(root)
imagen_label.grid(row=5, column=0, padx=5, pady=5, columnspan=2)

imagen_path = tk.StringVar()
imagen_path.set("")

tiempoPreparacion_label = tk.Label(root, text="Tiempo Preparacion")
tiempoPreparacion_label.grid(row=5, column=4, padx=5, pady=5)

tiempoPreparacion_text = tk.Text(root,height=10)
tiempoPreparacion_text.grid(row=5, column=4, padx=5, pady=5)

 
tiempoCoccion_label = tk.Label(root, text="Tiempo Coccion")
tiempoCoccion_label.grid(row=5, column=4, padx=5, pady=5)

tiempoCoccion_text = tk.Text(root,height=10)
tiempoCoccion_text.grid(row=5, column=4, padx=5, pady=5)

cargar_imagen_button = tk.Button(root, text="Cargar imagen", command=cargar_imagen)
cargar_imagen_button.grid(row=10, column=0, padx=5, pady=5,sticky="s")

agregar_button = tk.Button(root, text="Agregar", command=agregar_receta)
agregar_button.grid(row=10, column=1, padx=5, pady=5)

eliminar_button = tk.Button(root, text="Eliminar", command=eliminar_receta)
eliminar_button.grid(row=10, column=2, padx=5, pady=5)

modificar_button = tk.Button(root, text="Modificar", command=modificar_receta)
modificar_button.grid(row=10, column=3, padx=5, pady=5)

ver_button = tk.Button(root, text="Ver", command=mostrar_recetas)
ver_button.grid(row=10, column=4, padx=5, pady=5)

marcar_favorito_button = tk.Button(root, text="Marcar como favorito", command=marcar_favorito)
marcar_favorito_button.grid(row=10, column=5, padx=5, pady=5)

instrucciones_label = tk.Label(root, text="Recetas:")
instrucciones_label.grid(row=0, column=0, padx=12, pady=12,sticky="w")

lista_recetas = tk.Listbox(root, width=50, height=10)
lista_recetas.grid(row=1, column=0, padx=12, pady=12, columnspan=2)
lista_recetas.bind("<<ListboxSelect>>",lambda x: mostrar_recetas())
actualizar_lista_recetas()

root.mainloop()