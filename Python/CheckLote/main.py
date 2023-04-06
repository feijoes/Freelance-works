import seleniumBot
from dotenv import load_dotenv
import os
load_dotenv()

CLAVE = os.getenv('CLAVE')
API_KEY = os.getenv("API_KEY")
with open("numeros.txt") as f:
    numeros = [x.strip() for x in f.readlines()]

numeros_validos = seleniumBot.check_numero(numeros,CLAVE,API_KEY)

with open("live.txt","a") as f:
    for i in numeros_validos:
        f.write(f"{i}\n")