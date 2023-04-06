import tkinter as tk
import json
from tkinter import filedialog
from PIL import ImageTk, Image
from random import choice
from tkinter import messagebox
from datetime import datetime

class Receta:
    
    """Se define la clase Receta"""
    
    def __init__(self, nombre, ingredientes, instrucciones, imagen, tiempoPreparacion ,tiempoCoccion, fecha , favorito=False):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.instrucciones = instrucciones
        self.imagen = imagen
        self.favorito = favorito
        self.tiempoPreparacion = tiempoPreparacion
        self.tiempoCoccion = tiempoCoccion
        self.fecha = fecha
    def __dict__(self):
        return {
            "nombre": self.nombre,
            "ingredientes": [ingrediente.__dict__ for ingrediente in self.ingredientes],
            "instrucciones": self.instrucciones,
            "imagen": self.imagen,
            "favorito": self.favorito,
            "fechaDeCreacion": self.fecha,
            "tiempoPreparacion": self.tiempoPreparacion,
            "tiempoCoccion": self.tiempoCoccion,
        }
class Ingrediente:
    def __init__( self, nombre, unidadMedida, cantidad ):
        self.nombre = nombre
        self.unidadMedida = unidadMedida
        self.cantidad = cantidad
    def __str__(self):
        return f"{self.nombre} {self.unidadMedida} {self.cantidad}"
    

        
class Recetario:
    """Se define la clase Recetario"""
    def __init__(self):
        self.recetas = []
        self.receta_del_dia = None
        

    def agregar_receta(self, receta):
        self.recetas.append(receta)

    def eliminar_receta(self, receta):
        self.recetas.remove(receta)

    def modificar_receta(self, receta, nuevo_nombre, nuevos_ingredientes, nuevas_instrucciones, nueva_imagen,nuevo_tiempoPreparacion,nuevo_tiempoCoccion,nuevo_favorito=False):
        fecha = receta.fecha
        self.recetas.remove(receta)
        nueva_receta = Receta(
            nuevo_nombre,
            nuevos_ingredientes,
            nuevas_instrucciones,
            nueva_imagen,
            nuevo_tiempoPreparacion,
            nuevo_tiempoCoccion,
            fecha,
            nuevo_favorito
        )
        self.recetas.append(nueva_receta)
        return nueva_receta

    def elegir_receta_del_dia(self):
        
        self.receta_del_dia = choice(self.recetas)
    def ver_receta(self, receta):
        limpiar_formulario()
        nombre_entry.insert(0, receta.nombre)
  
     
        ingredientes_text.insert(tk.INSERT, "\n".join([str(ingrediente) for ingrediente in receta.ingredientes]))
        instrucciones_text.insert(tk.INSERT, receta.instrucciones)
        imagen_path.set(receta.imagen)
        if receta.imagen:
            imagen = Image.open(receta.imagen)
            imagen.thumbnail((150, 150))
            imagen = ImageTk.PhotoImage(imagen)
            imagen_label.config(image=imagen)
            imagen_label.image = imagen
        tiempoPreparacion_text.insert(tk.INSERT, receta.tiempoPreparacion)
        tiempoCoccion_text.insert(tk.INSERT, receta.tiempoCoccion)
    

def IngredientesText_to_List(ingredientesText):
    ingredientesList = []
    for i in ingredientesText.split("\n"):
        nombreIngrediente, unidadMedida, cantidad =  i.split()
        ingredientesList.append(Ingrediente(nombreIngrediente,unidadMedida,cantidad))
   
    return ingredientesList


def cargar_recetas():
    recetario = Recetario()
    with open("recetas.json", "r",encoding="utf-8") as archivo:
        recetas = json.load(archivo)
        for receta in recetas["recetas"]:
            nombre = receta["nombre"]
            ingredientes = receta["ingredientes"]
            ingredientesList = []
            for ingrediente in ingredientes:
                ingredientesList.append(Ingrediente(ingrediente["nombre"],ingrediente["unidadMedida"],ingrediente["cantidad"]))
                
            instrucciones = receta["instrucciones"]
            imagen = receta["imagen"]
            tiempoPreparacion = receta["tiempoPreparacion"]
            tiempoCoccion = receta["tiempoCoccion"]
            favorito = receta["favorito"]
            
            receta = Receta(nombre, ingredientesList, instrucciones, imagen,tiempoPreparacion,tiempoCoccion, favorito)
            recetario.agregar_receta(receta)
 
    if recetario.recetas:
        recetario.elegir_receta_del_dia()

    return recetario


def guardar_recetas(recetario,deleteReceta={},updateReceta=()):

    with open("recetas.json", "r+",encoding="utf-8") as archivo:
        json_data = json.load(archivo)
        for receta in recetario.recetas:
            recetaDict = receta.__dict__()
            if not recetaDict in json_data["recetas"]:
                json_data["recetas"].append(recetaDict)
        if deleteReceta:
            json_data["recetas"].remove(deleteReceta.__dict__())
        if updateReceta:
            json_data["recetas"].remove(updateReceta.__dict__())
        archivo.seek(0) 
        archivo.write(json.dumps(json_data,ensure_ascii=False,indent=4))
        archivo.truncate()
        
            
            

def agregar_receta():
    
    nombre = nombre_entry.get()
    if not nombre:
        messagebox.showinfo ("Nombre invalido", "El nombre de la receta no puede ser vacio")
    ingredientes = ingredientes_text.get("1.0", "end-1c")
    ingredientesList = IngredientesText_to_List(ingredientes)
        
    instrucciones = instrucciones_text.get("1.0", "end-1c")
    imagen = imagen_path.get()
    tiempoPreparacion = tiempoPreparacion_text.get("1.0", "end-1c")
    tiempoCoccion = tiempoCoccion_text.get("1.0", "end-1c")
    favorito = False
    

    now = datetime.now()
    now = str(now)
    
    receta = Receta(nombre, ingredientesList, instrucciones, imagen,tiempoPreparacion,tiempoCoccion,now ,favorito)
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
    guardar_recetas(recetario,deleteReceta=receta)
    limpiar_formulario()
    actualizar_lista_recetas()
    
def modificar_receta():
    seleccion = lista_recetas.curselection()
   
    if seleccion:
        receta = recetario.recetas[seleccion[0]]
        
        nuevo_nombre = nombre_entry.get()
        nuevos_ingredientes = ingredientes_text.get("1.0", "end-1c")
        nuevos_ingredientesList = IngredientesText_to_List(nuevos_ingredientes)
        nuevas_instrucciones = instrucciones_text.get("1.0", "end-1c")
        nueva_imagen = imagen_path.get()
        nuevo_tiempoPreparacion = tiempoPreparacion_text.get("1.0", "end-1c")
        nuevo_tiempoCoccion = tiempoCoccion_text.get("1.0", "end-1c")
        recetario.modificar_receta(receta, nuevo_nombre, nuevos_ingredientesList, nuevas_instrucciones, nueva_imagen,nuevo_tiempoPreparacion,nuevo_tiempoCoccion,receta.favorito)
        guardar_recetas(recetario,updateReceta=receta)
        limpiar_formulario()
        actualizar_lista_recetas()
    
def marcar_favorito():
    seleccion = lista_recetas.curselection()
    if seleccion:
        receta = recetario.recetas[seleccion[0]]
        recetario.modificar_receta(
            receta,         
            receta.nombre,
            receta.ingredientes,           
            receta.instrucciones,            
            receta.imagen,           
            receta.tiempoPreparacion,
            receta.tiempoCoccion,
            not receta.favorito
        )
        guardar_recetas(recetario,updateReceta=receta)
        actualizar_lista_recetas()
def ver_receta():
    seleccion = lista_recetas.curselection()
    seleccion2 = receta_del_dia.curselection()
    
    if seleccion:
        receta = recetario.recetas[seleccion[0]]
    if seleccion2:
        
        receta = recetario.recetas[seleccion2[0]]
    if receta: 
        recetario.ver_receta(receta)
    
def mostrar_recetas():
    seleccion = lista_recetas.curselection()
    seleccion2 = receta_del_dia.curselection()
    receta = None
   
    if seleccion:
        receta = recetario.recetas[seleccion[0]]
    elif seleccion2:
        receta = recetario.receta_del_dia
    if receta: 
        recetario.ver_receta(receta)

def cargar_imagen():
    ruta_imagen = filedialog.askopenfilename()
    imagen_path.set(ruta_imagen)
    imagen = Image.open(ruta_imagen)
    imagen.thumbnail((150, 150))
    imagen = ImageTk.PhotoImage(imagen)
    imagen_label.config(image=imagen)
    imagen_label.image = imagen

def actualizar_lista_recetas():
    lista_recetas.delete(0, tk.END)
    for receta in recetario.recetas:
        lista_recetas.insert(tk.END, receta.nombre)
    if recetario.receta_del_dia:
        receta_del_dia.insert(tk.END, recetario.receta_del_dia.nombre)

def limpiar_formulario():
    nombre_entry.delete(0, tk.END)
    ingredientes_text.delete("1.0", tk.END)
    instrucciones_text.delete("1.0", tk.END)
    imagen_path.set("")
    imagen_label.config(image=None)
    tiempoCoccion_text.delete("1.0", tk.END)
    tiempoPreparacion_text.delete("1.0", tk.END)
    
    



root = tk.Tk()
root.title("Recetario")


root.geometry('1480x700')

recetario = cargar_recetas()

# Create a frame for the recipe form
recipe_frame = tk.Frame(root)
recipe_frame.grid(row=0, column=1, padx=10, pady=10)

# Nombre
nombre_label = tk.Label(recipe_frame, text="Nombre:")
nombre_label.grid(row=0, column=0, sticky="w")

nombre_entry = tk.Entry(recipe_frame)
nombre_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

# Ingredientes
ingredientes_label = tk.Label(recipe_frame, text="Ingredientes:")
ingredientes_label.grid(row=1, column=0, sticky="w")

ingredientes_text = tk.Text(recipe_frame, height=10)
ingredientes_text.grid(row=2, column=0, padx=5, pady=5, columnspan=2, sticky="w")

# Instrucciones
instrucciones_label = tk.Label(recipe_frame, text="Instrucciones:")
instrucciones_label.grid(row=3, column=0, sticky="w")

instrucciones_text = tk.Text(recipe_frame, height=10)
instrucciones_text.grid(row=4, column=0, padx=5, pady=5, columnspan=2, sticky="w")

# Imagen
imagen_label = tk.Label(root)
imagen_label.place(x=1050,y=20)
cargar_imagen_button = tk.Button(recipe_frame, text="Cargar imagen", command=cargar_imagen)
cargar_imagen_button.grid(row=6, column=0, padx=5, pady=5, sticky="w")
imagen_path = tk.StringVar()
imagen_path.set("")
# Tiempo de preparación y cocción
tiempoPreparacion_label = tk.Label(recipe_frame, text="Tiempo de Preparación:")
tiempoPreparacion_label.grid(row=7, column=0, padx=5, pady=5, sticky="w")

tiempoPreparacion_text = tk.Text(recipe_frame, height=1, width=10)
tiempoPreparacion_text.grid(row=7, column=1, padx=5, pady=5, sticky="w")

tiempoCoccion_label = tk.Label(recipe_frame, text="Tiempo de Cocción:")
tiempoCoccion_label.grid(row=8, column=0, padx=5, pady=5, sticky="w")

tiempoCoccion_text = tk.Text(recipe_frame, height=1, width=10)
tiempoCoccion_text.grid(row=8, column=1, padx=5, pady=5, sticky="w")


agregar_button = tk.Button(root, text="Agregar", command=agregar_receta)
agregar_button.grid(row=8, column=0, padx=5, pady=5)

eliminar_button = tk.Button(root, text="Eliminar", command=eliminar_receta)
eliminar_button.grid(row=8, column=1, padx=5, pady=5)

modificar_button = tk.Button(root, text="Modificar", command=modificar_receta)
modificar_button.grid(row=8, column=2, padx=5, pady=5)



marcar_favorito_button = tk.Button(root, text="Marcar como favorito", command=marcar_favorito)
marcar_favorito_button.grid(row=8, column=4, padx=5, pady=5)


recetas_frames = tk.Frame(root)
recetas_frames.grid(row=0,column=2)

instrucciones_label = tk.Label(recetas_frames, text="Recetas:")
instrucciones_label.grid(row=1, column=0, padx=5, pady=5)

lista_recetas = tk.Listbox(recetas_frames, width=50, height=10)
lista_recetas.grid(row=1, column=1, padx=5, pady=5)

lista_recetas.bind("<<ListboxSelect>>", lambda x: mostrar_recetas())

receta_del_dia_label = tk.Label(recetas_frames, text="Receta del dia")
receta_del_dia_label.grid(row=0, column=0, padx=5, pady=5)

receta_del_dia = tk.Listbox(recetas_frames, width=15, height=1)
receta_del_dia.grid(row=0,column=1)
receta_del_dia.bind("<<ListboxSelect>>", lambda x: mostrar_recetas())

actualizar_lista_recetas()

root.mainloop()