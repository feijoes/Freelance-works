import tkinter as tk
from tkinter import ttk 
from tkinter import filedialog



def boton1_click():
    folder_path = filedialog.askdirectory()
    if folder_path:
        new_window = tk.Toplevel(root)
        new_window.title("New Window")
        new_window.minsize(400,400)
    
        folder_entry = tk.Entry(new_window, width=70)
        folder_entry.pack()
        tk.Button(new_window,text="confirmar", command=lambda:print("jsjs")).pack()
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder_path)
        new_window.lift()
  

def boton2_click():
    print("Botón 2 presionado")

root = tk.Tk()
root.title("NOMBRE")
root.minsize(width=300, height=300)

boton1 = ttk.Button(root, text="Digitalizacion", command=boton1_click)
boton1.pack(side=tk.RIGHT, padx=20)

boton2 = ttk.Button(root, text="Buscar palabra ", command=boton2_click)
boton2.pack(side=tk.LEFT, padx=20)

etiqueta = ttk.Label(root, text="Menu")
etiqueta.pack()


root.mainloop()