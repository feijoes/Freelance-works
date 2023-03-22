import seleniumBot
from dotenv import load_dotenv
import os
load_dotenv()

CLAVE = os.getenv('CLAVE')
with open("numeros.txt") as f:
    numeros = [x.strip() for x in f.readlines()]

seleniumBot.check_numero(numeros,CLAVE)