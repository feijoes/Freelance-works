import time
import sys
import subprocess

def main():
    contas= sys.argv[4:]
    print(f'proceso numero {sys.argv[1]} comecando')
    for i in contas[:-1]:
        subprocess.Popen(f"py seleniumBot.py {sys.argv[2]} {sys.argv[3]} {i}")
    time.sleep(2)
    subprocess.run(f"py seleniumBot.py {sys.argv[2]} {sys.argv[3]} {contas[-1]}")
main()
