from operator import itemgetter
from archivos import *

import os
def carrito(prodocutos,usuarios):
    os.system('cls')
    for num,i in enumerate(usuarios):
            if i:
                print(f'{num} persona {i[0]} tiene cedula {i[1]} con pais {i[2]}')
    
    while True:
        try:
            persona = int(input('porfavor seleciona el numero de la persona que le queres agregar un producto a su carrito: '))
            
            usuarios[persona]
            break
        except:
            print('numero invalido')
    print()
    for num,i in enumerate(prodocutos.items()):
            print(f'{num} producto {i[0]} cuesta {i[1]}')
            
    while True:
            try:
                datos = input('porfavor ingresar el numero del producto que queres agregar al carrito de ese usuario \n:')
                prodocutos[[x for x in prodocutos.keys()][int(datos)]]
               
                usuarios[persona][3].append([x for x in prodocutos.keys()][int(datos)])
                print(usuarios[persona])
                input()
                break
            except:
                print('numero invalido')
def inpu():
    opciones = "Menu ecommerce, opciones: \n1 Ingresar Datos \n2 Consulta de productos \n3 Modificacion de datos\n4 Eliminacion de Datos\n5 Ordenar\n6 Lista de usuarios\n7 Estadisticas\n8 Salir \n9 agregrar al carrito de un usuario:"
    while True:
        num = input(opciones)
        if num.isnumeric():
            if int(num) <= 9 and int(num) >0:
                break
            else:
                print("numero invalido")
        else:
            print("no es un numero valido")
    return int(num)

def IngresarDatos(prodocutos,usuarios):
    while True:
        os.system('cls')
        try:
            inp = int(input('1 ingresar usuario\n2 ingresar producto nuevo\n:'))
            if inp < 3 and inp > 0:
                break
        except:
            return prodocutos,usuarios
    if inp-1:
        while True:
            
            datos = input('porfavor ingresar nombre del producto y precio con un espacio entre cada infomarcion\n:').split()
            if len(datos) == 2:
                break
        prodocutos[datos[0]] = datos[1]
    else:
        while True:
            
            datos = [input('poner nombre: '),input('poner  numero de cedula: '),input('poner pais: ' )]
            if len(datos) == 3:
                break
        datos.append([])
        usuarios.append(datos)
    return prodocutos,usuarios
    


def ConsultaDatos(prodocutos,usuarios):
    os.system('cls')
    for i in prodocutos.items():
        
        if float(i[1]) > 100:
            d=10
        if  float(i[1]) <= 100:
            d=2
        if float(i[1]) >= 150:
            d=20
        if float(i[1]) >= 300:
            d=30
        
        
        print(f'producto {i[0]} cuesta {i[1]}  y esta con {d}% de desc descuento' )
    input('precione cualquier tecla para volver')
    return prodocutos,usuarios


def ModificacionDatos(prodocutos,usuarios):
   
    while True:
        os.system('cls')
        try:
            inp = int(input('1 modificar usuario\n2 modificar producto\n:'))
            if inp < 3 and inp > 0:
                break
        except:
            return prodocutos,usuarios
    if inp-1:
        for num,i in enumerate(prodocutos.items()):
            print(f'[{num}] producto {i[0]} cuesta {i[1]}')
        while True:
            try:
                datos = input('porfavor ingresar el numero del producto que queres modificar \n:')
                prodocutos[[x for x in prodocutos.keys()][int(datos)]]
                while True:
                    datos = input('porfavor ingresar nombre del producto y precio con un espacio entre cada infomarcion\n:').split()
                    if len(datos) == 2:
                        break
                prodocutos[datos[0]] = datos[1]
            except:
                print('pusiste alguna informacion no valida')
    else:
        for num,i in enumerate(usuarios):
            if i:
                print(f'[{num}] persona {i[0]} tiene cedula {i[1]} con pais {i[2]}')
        while True:
            try:
                datos = int(input('porfavor ingresar numero de la persona que queres modificar\n:'))
                usuarios[datos]
                break
            except:
                print('pusiste alguna informacion no valida')
        while True:
            info =   [input('poner nombre: '),input('poner numero cedular: '),input('poner pais: ' )]
            if len(info) == 3:
                break
        info.append([])
        usuarios[datos] = info
        
    return prodocutos,usuarios


def EliminacionDatos(prodocutos,usuarios):
    while True:
        os.system('cls')
        try:
            inp = int(input('1 eliminar usuario\n2 eliminar producto\n:'))
            if inp < 3 and inp > 0:
                break
        except:
            return prodocutos,usuarios
    if inp-1:
        for i in prodocutos.items():
            print(f'producto {i[0]} cuesta {i[1]}')
        while True:
            try:
                datos = input('porfavor ingresar el nombre del producto que queres eliminar \n:')
                if datos in prodocutos:
                    del prodocutos[datos]
                    break
            except:
                print('pusiste alguna informacion no valida')
    else:
        for num,i in enumerate(usuarios):
            if i:
                
                print(f'[{num}] persona {i[0]} tiene cedula {i[1]} con pais {i[2]}')
        while True:
            try:
                datos = int(input('porfavor ingresar numero de la persona que queres eliminar\n:'))
                del usuarios[datos]
                break
            except:
                print('pusiste alguna informacion no valida')
        
    return prodocutos,usuarios

def Ordenar(prodocutos,usuarios):
    while True:
        os.system('cls')
        try:
            inp = int(input('1 ordenar usuario\n2 ordenar producto\n:'))
            if inp < 3 and inp > 0:
                break
        except:
            return prodocutos,usuarios
    if inp-1:
        while True:
            os.system('cls')
            try:
                inp = int(input('1 ordenar producto por nombre\n2 ordenar por precio\n:'))
                if inp < 3 and inp > 0:
                    break
            except:
                return prodocutos,usuarios
            if inp-1:
                prodocutos =dict(sorted(prodocutos.items(), key=lambda item: item[1]))
            else:
                prodocutos =dict(sorted(prodocutos.items(), key=lambda item: item[0]))
    else:
        while True:
            os.system('cls')
            try:
                inp = int(input('1 ordenar usuario por nombre\n2 ordenar cedula\n:'))
                if inp < 3 and inp > 0:
                    break
            except:
                return prodocutos,usuarios
        if inp-1:
            
            usuarios = sorted(usuarios, key=itemgetter(1))
            
        else:
            usuarios = sorted(usuarios, key=itemgetter(0))
        
    return prodocutos,usuarios

def ListaU(prodocutos,usuarios):
    os.system('cls')
    for i in usuarios:
        print(f'persona {i[0]} tiene cedula {i[1]} y es de {i[2]} y los productos en sus carritos son: ', end='')
        for j in i[3]:
            print(j, end=',')
    input('precione cualquier tecla para volver')
    return prodocutos,usuarios
    

def Estadisticas(prodocutos,usuarios):
    input('precione enter para ver el producto con mayor precio y un listado de cuantidad de personas por pais')

    mayor=''
    mayorN=0
    for i,precio in prodocutos.items():
        if int(precio) >=mayorN:
            mayorN= precio
            mayor=i
    print(f'El producto mas caro es {mayor} con un precio de {mayorN}')


    paises={i[2]:0 for i in usuarios }
    for i in usuarios:
        paises[i[2]]+=1

    for i in paises.items():
        print(f'hay {i[1]} personas del pais {i[0]}')
        
    print()
    input('enter para volver')
    return prodocutos,usuarios

def fin(prodocutos,usuarios):
    write_prodoc(prodocutos)
    write_usuarios(usuarios)
    print('Gracias y vuelvas siempre...')

        
        