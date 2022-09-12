
from functions import *

def main():
     prodocutos = read_produc()
     usuarios = read_usuarios()
     while True:
        os.system('cls')
        num = inpu()
        
        if num == 8:
            fin(prodocutos,usuarios)
            break
        if num == 1:
            prodocutos, usuarios=IngresarDatos( prodocutos, usuarios)
            print(usuarios)
            input()
        if num == 2:
             prodocutos, usuarios=ConsultaDatos( prodocutos, usuarios)
        if num == 3:
             prodocutos, usuarios=ModificacionDatos( prodocutos, usuarios)
        if num == 4:
             prodocutos, usuarios=EliminacionDatos( prodocutos, usuarios)
        if num == 5:
             prodocutos, usuarios=Ordenar( prodocutos, usuarios)
        if num == 6:
            prodocutos, usuarios= ListaU( prodocutos, usuarios)
        if num == 7:
             prodocutos, usuarios=Estadisticas( prodocutos, usuarios)
main()


