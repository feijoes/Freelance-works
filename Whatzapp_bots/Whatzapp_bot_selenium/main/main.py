
import sys
from time import sleep
import random
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

print
def frases():
    with open('../frases.txt','r') as f:
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
    print(min,max,n)
    with open("../numeros.txt",'r') as f:
        numeros = f.readlines()[:max+1] if min == 0 else f.readlines()[min-1:] if max == n else f.readlines()[min:max+1]
        
        numeros2 = []
        for i in numeros:
            numeros2.append(i.strip('\n'))
    d = open("../notsend.txt",'r')
    numeros = d.readlines()
    notnumeros = []
    for i in numeros:
        notnumeros.append(i.strip('\n'))
    d.close()
    return [x for x in numeros2 if x not in notnumeros]
def imagenes():
    with open('../imagenes.txt','r') as f:
        imagenes = f.readlines()
        
        imagen = random.choice(imagenes)
        return imagen

def send(contatos,imagen):
    print(contatos)
    driver = webdriver.Chrome(ChromeDriverManager().install()) 
    driver.get('https://web.whatsapp.com/')
    driver.maximize_window()
    driver.implicitly_wait(150)
    print(contatos)
    while len(contatos)>=1:
        try:
            frase3 =frases()
            sleep(30)
            a = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div[2]')
            a.click()
            sleep(14)
            a.send_keys(contatos[0])
            sleep(8)
            driver.find_element(By.XPATH,f"//span[@title='{contatos[0]}']").click()
            sleep(15)
            driver.find_element(By.XPATH,'//span[@data-testid="clip"]').click()
            sleep(10)
            driver.find_element(By.XPATH,'//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]').send_keys(imagen)
            sleep(14)
            driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]').send_keys(frase3)
            sleep(17)
            driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div').click()
            sleep(30)
            with open("../notsend.txt","a") as s:
                s.write(f"{contatos[0]}\n")
            del contatos[0]
        except Exception:
            with open("../notsend.txt","a") as s:
                s.write(f"{contatos[0]}\n")
            del contatos[0]
            continue
def main():
    send(contatos=numeros(),imagen=imagenes())

main()
