import tkinter as tk
from tkinter import filedialog
import os
from tkinter.scrolledtext import ScrolledText
import subprocess
import sys
ws = tk.Tk()
ws.title('Whatzapp Bot')
ws.geometry("700x600")
ws.iconbitmap('logo.ico')

pos_img = 0
images = []



frame = tk.LabelFrame(
    ws,
    text='Whatzapp Span',
    bg='#f0f0f0',
    font=(20)
)
frame.pack(expand=True, fill=tk.BOTH)

imagenes = tk.Listbox(frame,width=20, bd=3, height=5)
def ImageOpen():
        global pos_img ,imagenes,images
        filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes =[('all files', '.*'),("text files",".txt"),('image files', ('.png', '.jpg'))])
        if filename :
                images.append(filename)       
                imagenes.insert(pos_img,filename.split('/')[-1])
                pos_img += 1
tk.Button(ws, text='Imagenes', command=ImageOpen).place(x=15, y=450)
imagenes.place(x=15,y=460)



ncontactos = tk.Label(ws, text = "Numeros de contactos: 0")
def Contactos():
        filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes =[('all files', '.*'),("text files",".txt"),('image files', ('.png', '.jpg'))])
        if filename:
                with open(filename,"r") as f:
                        contactos = []
                        for i, z in enumerate(f):
                                contactos.append(z)
                file = open(os.path.join(os.pardir, "numeros.txt"), "w")
                file.writelines(contactos)
                file.close()
                ncontactos.configure(text = f"Numeros de contactos: {str(i + 1)}")
tk.Button(ws, text='Archivo de los Contactos', command=Contactos).place(x=40, y=30)
ncontactos.place(x=40,y=55)

Frases = []
num_frases = 0
Textfield = ScrolledText(ws,wrap = tk.WORD,width = 30,height = 15,font = ("Times New Roman",10))
frases = tk.Label(ws, text = "Numero de frases: 0")
frases.place(x=15,y=390)
def Frase():
        global num_frases, Textfield,Frases, frases
        num_frases +=1
        text = Textfield.get('1.0', tk.END)
        if text : 
                Textfield.delete('1.0', tk.END)
                
                with open(os.path.join(os.pardir, "frases.txt"),"a")as f:
                        
                        f.write(rf"{text}")
                frases.configure(text = f"Numeros de frases guardados: {int(num_frases)}")
                
tk.Label(ws, text = "Que enviar").place(x=15,y=85)
Textfield.place(x=15,y=110)
tk.Button(ws, text='Confirmar', command=Frase).place(x=40, y=350)


tk.Label(ws,text="Numero de bots: ").place(x=300,y=85)
input = tk.Entry(ws,width=20)
input.place(x=320,y=110)
def Enpezar():
        global ws,images, Frases,input
        
        bots = int(input.get())             
        if images:
                a = open(os.path.join(os.pardir, "imagenes.txt"),"w")
                for z in images:
                        a.write(z)
                a.close()
                
        with open("../numeros.txt","r") as f:
                for i, _ in enumerate(f):
                        pass
        n = i //bots
        l = [[0,i-n*(bots-1)]]
        count = bots - 1
        for j in range(count):
                if j == bots-1:
                        l.append([i-n+1,i])
                        continue
                l.append([i-n*count+1,i-n*(count-1)])
                count-=1
                
        print(f"numeros de bots {bots}")
        for p in l:
               subprocess.Popen(['python','./main/main.py', str(p[0]) , str(p[1]), str(i)])
        sys.exit(0)

                    
enpezar = tk.Button(ws,text="Empezar",command=Enpezar,width=20,font=("Times New Roman",20))
enpezar.place(x=300,y=500)

ws.mainloop()