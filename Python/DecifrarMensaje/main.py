
i = [2,8,0,3,1,5,2,9,4,2,6,8]
palabras = ["8","intro","la","de","es","a","mejor","peor","seccion","progra","7","pancito","el","a"]


def descifrarMensaje(i,palabras):
    newString =""
    for numero in i:
        newString+= palabras[numero]
        newString += " "
    newList = []
    
    duplicates = {}
    for k in palabras:
        if palabras.count(k) > 1:
            duplicates[k] = palabras.count(k)
            
    for palabra in palabras:
        if palabra in newString: 
            if palabra in duplicates.keys():
                duplicates[palabra] -=1
                if duplicates[palabra] >= 1:
                    newList.append(palabra)
        else:
            newList.append(palabra)

    return [newString] + newList

print(descifrarMensaje(i,palabras))
