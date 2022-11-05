
i = [2,8,0,3,1,5,2,9,4,2,6,8]
palabras = ["8","intro","la","de","es","a","mejor","peor","seccion","progra","7","pancito","el"]

def descifrarMensaje(i,palabras):
    newString =""
    for numero in i:
        newString+= palabras[numero]
        newString += " "
        
    
    
    return [newString] + []

print(descifrarMensaje(i,palabras))