
import sys
from time import sleep
import random
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def frases():
    with open('/frases.txt', 'r') as f:
        frases = f.readlines()
        frases2 = []
        for i in frases:
            frases2.append(i.strip('\n'))
        frase = random.choice(frases2)
        return frase

def numeros():
    min, max = sys.argv[1:3]
    n = sys.argv[3]

    min = int(min)
    max= int(max)
    with open(__file__[:-12]+"numeros.txt", 'r') as f:
        numeros = f.readlines()[:max+1] if min == 0 else f.readlines()[min-1:] if max == n else f.readlines()[min:max+1]
        numeros2 = []
        for i in numeros:
            numeros2.append(i.strip('\n'))
    d = open(__file__[:-12]+"notsend.txt", 'r')
    numeros = d.readlines()
    notnumeros = []
    for i in numeros:
        notnumeros.append(i.strip('\n'))
    d.close()
    return list(set([x for x in numeros2 if x not in notnumeros]))
def imagenes():
    with open(__file__[:-12]+'imagenes.txt', 'r') as f:
        imagenes = f.readlines()
        
        imagen = random.choice(imagenes)
        return imagen

def send(contatos,imagen):
    api ="https://web.whatsapp.com/send?phone="
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://web.whatsapp.com/")
    print(f"tiempo para scanear")
    sleep(int(sys.argv[6]))
    while len(contatos) >= 1:
        try:
            driver.get(api+contatos[0])
            sleep(int(sys.argv[5]))
            frase3 = frases()
            driver.find_element(By.XPATH, '//span[@data-testid="clip"]').click()
            sleep(10)
            driver.find_element(By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]').send_keys(imagen)
            sleep(14)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]').send_keys(frase3)
            sleep(17)
            driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div').click()
            sleep(30)
            with open(__file__[:-12]+"notsend.txt", "a") as s:
                s.write(f"{contatos[0]}\n")
            del contatos[0]
        except Exception as e:
            print(f"Bot {sys.argv[4]} no pudo enviar mensaje para {contatos[0]}")
            with open(__file__[:-12]+"error.txt", "a") as s:
                s.write(f"{contatos[0]}\n")
            del contatos[0]
            continue
    print(f"BOT {sys.argv[4]} Terminado")
    while True:
        sleep(3)
def main():
    send(contatos=numeros(),imagen=imagenes())

main()
