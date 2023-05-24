import tkinter as tk
from tkinter import ttk 
from tkinter import filedialog
from create_files import main as Digitalizar
from search import search_word_in_files

def boton1_click():
    folder_path = filedialog.askdirectory()
    if folder_path:
        new_window = tk.Toplevel(root)
        new_window.title("New Window")
        new_window.minsize(400,400)
    
        folder_entry = tk.Entry(new_window, width=70)
        folder_entry.pack()
        tk.Button(new_window,text="confirmar", command=lambda:(Digitalizar(folder_path), tk.Label(new_window,text="process finished, close this window"))).pack()
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder_path)
        new_window.lift()
  
def show_words(window, dataframe):
    
    text_widget = tk.Text(window)
    text_widget.pack()

    # Convert the DataFrame to a string representation
    dataframe_str = dataframe.to_string(index=False)

    # Insert the DataFrame string into the Text widget
    text_widget.insert(tk.END, dataframe_str)

    # Disable editing in the Text widget
    text_widget.config(state=tk.DISABLED) 
def boton2_click():
    folder_path = filedialog.askdirectory()
    if folder_path:
        new_window = tk.Toplevel(root)
        new_window.title("New Window")
        new_window.minsize(400,400)
    
        folder_entry = tk.Entry(new_window, width=70)
        folder_entry.pack(pady=5)
        
        tk.Button(new_window,text="confirmar", command=lambda: show_words(new_window,search_word_in_files(folder_path,inputtxt.get(1.0,"end-1c").split("\n")))).pack()
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder_path)
        tk.Label(text="Palabras para buscar").pack(pady=5)
        inputtxt = tk.Text(new_window,
                   height = 5,
                   width = 20)
        inputtxt.pack()
        new_window.lift()

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