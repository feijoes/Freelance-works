import csv
import ast
import os

def read_produc() -> dict:
    myproductos = {}
    if os.path.exists('productos.txt'):
        with open('productos.txt','r') as f:
            prodctos = f.read().splitlines()
            
            for i in prodctos:
                i = i.replace("$","")
                producto = i.split(';')
                myproductos[producto[0]] = float(producto[1])
    return myproductos

def write_prodoc(prodocutos):
     with open('productos.txt','w') as file:
        for i,j in prodocutos.items():
            s= i+';'+str(j)
            file.write(s + '\n')
  
def read_usuarios():
    prodctos = []
    if os.path.exists('usuarios.csv'):
        with open('usuarios.csv','r') as f:
            prodctos = f.read().splitlines()
    s=[i.split(';') for i in prodctos if i ]
    for i in s:
        
        i[3] = ast.literal_eval(i[3])
   
    return s

def write_usuarios(usuarios):

    with open('usuarios.csv','w') as file:
        writer = csv.writer(file,delimiter=';')
        for i in usuarios:
            if i[0]:
                if len(i) == 1:
                    writer.writerow(i[0].split(";"))
                else:
                    writer.writerow(i)

            
