
import sys
from time import sleep
import random
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def frases():
    with open('../frases.txt','r') as f:
        frases = f.readlines()
        frases2 = []
        for i in frases:
            frases2.append(i.strip('\n'))
        frase = random.choice(frases2)
        return frase
def tiempo():
    with open('../tiempo.txt','r') as f:
        tiempo = f.readline()
        tiempo.strip('\n')
        return int(tiempo)
def numeros():
    min, max = sys.argv[1:3]
    n = sys.argv[3]
    min = int(min)
    max= int(max)
    print(min,max,n)
    with open('../numeros.txt','r') as f:
        numeros = f.readlines()[:max+1] if min == 0 else f.readlines()[min-1:] if max == n else f.readlines()[min:max+1]
        
        numeros2 = []
        for i in numeros:
            numeros2.append(i.strip('\n'))
        return numeros2
def imagenes():
    with open('../imagenes.txt','r') as f:
        imagenes = f.readlines()
        
        imagen = random.choice(imagenes)
        return imagen

def send(contatos,n,imagen):
    print(contatos)
    driver = webdriver.Chrome(ChromeDriverManager().install()) 
    driver.get('https://web.whatsapp.com/')
    driver.maximize_window()
    driver.implicitly_wait(150)
   
    print(contatos)
    while len(contatos)>=1:
        frase3 =frases()
        sleep(8)
        a = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div[2]')
        a.click()
        sleep(4)
        a.send_keys(contatos[0])
        sleep(4)
        driver.find_element(By.XPATH,f"//span[@title='{contatos[0]}']").click()
        sleep(5)
        driver.find_element(By.XPATH,'//span[@data-testid="clip"]').click()
        sleep(5)
        driver.find_element(By.XPATH,'//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]').send_keys(imagen)
        sleep(7)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]').send_keys(frase3)
        sleep(6)
        driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div').click()
        sleep(15)
        del contatos[0]
def main():
    send(contatos=numeros(),n=tiempo(),imagen=imagenes())

main()
