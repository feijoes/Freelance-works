import time
import sys
import subprocess


def modoAviao():
    pass



def main():
    with open(sys.argv[sys.argv.index('-n') + 1],'r') as f:
        contas = f.read().splitlines()
    link = sys.argv[sys.argv.index('-l') + 1]
    password = sys.argv[sys.argv.index('-p') + 1]
    num = 2
    proceso = 1
    while True:

    
        lista = contas[num-1:num]
        print(lista)
        if not lista:
            break

        comand=f"py controladorBots.py {proceso} {link} {password}"
        for i in lista:
            comand+=f' {i}'
        subprocess.run(comand)
        modoAviao()
        time.sleep(50)
        proceso+=1
        num +=1
main()