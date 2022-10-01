
listaDolares = []
listaYenes = []
listaEuros = []

nombre =input("escribir nombre y apellido: ")

def dolarPeso_promedio(list):
    list = [x*4200 for x in list]
    
    valor = 0
    for i in list:
        valor+=i
    if len(list) >= 1:
        valor = valor/len(list)
    else: valor = 0
    print(f'el promedio de la lista es {valor}')



def eurosPesos(list):
    list = [x*4700 for x in list]
    menor = list[0]
    mayor = 0
    for i in list:
        if i > mayor:
            mayor = i
        if menor > i:
            menor = i
    print(f'El valor mas costoso fue {mayor} y el menor {menor}')

#Dólares a pesos = 4200 pesos colombianos
#Euros a pesos = 4700 pesos colombianos
#Yenés a pesos= 7800 pesos colombianos
    
def yenes_pesos(list):
    list = [x*7800 for x in list]
    print('De mayor a menor la lista es:')
    for i in sorted(list, reverse=True):
        print(i,end=' ')
    print()




def comparacion(dolar_peso, euros_pesos, yenes_pesos):
    dolar_peso = [x*4200 for x in dolar_peso]
    euros_pesos = [x*4700 for x in euros_pesos]
    yenes_pesos = [x*7800 for x in yenes_pesos]
    mayor_recaudo = 0
    for i in [dolar_peso,euros_pesos,yenes_pesos]:
        if sum(i) > mayor_recaudo:
            mayor_recaudo = sum(i)
            index = i
    if index == dolar_peso:
        print(f"el mayor recaldo es dolares y gana {mayor_recaudo}")
    if index == euros_pesos:
        print(f"el mayor recaldo es euros y gana {mayor_recaudo}")
    if index == yenes_pesos:
        print(f"el mayor recaldo son yenes y gana {mayor_recaudo}")
    return mayor_recaudo

while True:
    moneda = input("Tipo de moneda a convertir Yenes(Y)/Euros(E)/Dolares(D): ")
    
    if moneda.upper() == "Y":
        valor = int(input("numero de Yenes a convertir: "))
        listaYenes.append(valor)
        print(f"convertiste {valor*7800}")
        
        
    if moneda.upper() == "E":
        valor = int(input("numero de Euros a convertir: "))
        listaEuros.append(valor)
        print(f"convertiste {valor*4700}")
    
    if moneda.upper() == "D":
        valor = int(input("numero de Dolares a convertir: "))
        listaDolares.append(valor)
        print(f"convertiste {valor*4200}")
    
    if input("deseas continuar ? S/N: ").upper() == "N":
        break

dolarPeso_promedio(listaDolares)
eurosPesos(listaEuros)
yenes_pesos(listaYenes)

print(comparacion(listaDolares,listaEuros,listaYenes))

print("estudiante "+ nombre)




    
    
    
    

    