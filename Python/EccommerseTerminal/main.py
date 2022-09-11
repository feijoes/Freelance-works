


from functions import menu


if __name__ == "__main__":
    opciones = "Menu ecommerce, opciones \n1 Ingresar Datos \n2 Consulta de datos\n3 Modificacion de datos\n4 Eliminacion de Datos\n5 Ordenar\n6 Listar datos\n7 Estadisticas\n8 Salir"
    while True:
        num = input(opciones)
        if num.isnumeric():
            if int(num) <= 8 and int(num) >0:
                break
            else:
                print("numero invalido")
        else:
            print("no es un numero")
        menu(num)