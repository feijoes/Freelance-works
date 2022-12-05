from Lab7 import main as Lab7
from Lab9 import main as lab9
from RegresionLineal import main as RegresionLineal
types = {
    1: "trapezoidal",
    2: "simpson13",
    3: "simpson38",
    4: "regresionLineal",
    5: "RegresionPolinomial"
}


function = int(input("Elija el numero del metodo que quiere elegir\n1 Trapecio\n2 Simpson 1/3\n3 Simpson 3/8\n4 Regresion Lineal\n5 Regresion Polinomial (Saldram Regresion Cuadratica, Cubica y Hiperbolica\n"))


if function in [1,2,3]:

    Lab7(types[function])
if function == 4:
    lab9()
if function == 5:
    RegresionLineal()

    
    


