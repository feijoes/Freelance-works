


i = input("Escribir i con espacio para cada numero: ").split()
palabras = input("Escribir cada palabra con un espacio cada palabra: ").split()

def descifrarMensaje(i,palabras):
    ## Creando la Palabra
    newString =""
    for numero in i:
        newString+= palabras[numero]
        newString += " "
    newList = []

    ## Palabras no utilizadas en i    
    for palabra in palabras:
        if not palabra in newString: 
            newList.append(palabra)

    return [newString] + newList


print()
print("i=",[i])
print()
print("palabras=", palabras)
print()
print("Lista de descifrarMensaje = " , descifrarMensaje(i,palabras))
