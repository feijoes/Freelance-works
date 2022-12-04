import subprocess
import sys
import pathlib
Path = pathlib.Path(__file__).parent.resolve()



def spawn_program_and_die(program, exit_code=0):
    subprocess.Popen(program)
    sys.exit(exit_code)

types = {
    1: "trapezoidal",
    2: "simpson13",
    3: "simpson38",
    4: "regresionLineal",
    5: "RegresionPolinomial"
}
pythonFiles = ["Lab7.py","Lab9.py","RegresionLineal.py"]

function = int(input("Elija el numero del metodo que quiere elegir\n1 Trapecio\n2 Simpson 1/3\n3 Simpson 3/8\n4 Regresion Lineal\n5 Regresion Polinomial (Saldram Regresion Cuadratica, Cubica y Hiperbolica\n"))


if function in [1,2,3]:
    file  = pythonFiles[0]
if function == 4:
    file = pythonFiles[1]
if function == 5:
    file = pythonFiles[2]
    
    
spawn_program_and_die(['python', f"{Path}\{file}", types[function]])

