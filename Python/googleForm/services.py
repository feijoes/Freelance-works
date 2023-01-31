from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from random import randint,choice
def getDriver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--profile-directory=Default')
    chrome_options.add_argument("--disable-plugins-discovery")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    
    bot:webdriver.Chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return bot

url = 'https://docs.google.com/forms/d/e/1FAIpQLSc1ca_-P_-Y1u56Lqg0-YWaLP3DuAY0M8oDqPjQM3k8kLljFw/viewform'


def generate_cpf():                                                        
    cpf = [randint(0, 9) for x in range(9)]                              
                                                                                
    for _ in range(2):                                                          
        val = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11      
                                                                                
        cpf.append(11 - val if val > 1 else 0)                                  
                                                                                
    return '%s%s%s.%s%s%s.%s%s%s-%s%s' % tuple(cpf)

def start():
    global bot
    bot = getDriver()
    sleep(randint(1,5))
    bot.get(url)
    sleep(randint(1,5))
    
def fields(cpf,nome,email):
    listaAsociacao = ['//*[@id="i19"]/div[3]','//*[@id="i22"]/div[3]/div','//*[@id="i25"]/div[3]/div','//*[@id="i28"]/div[3]/div','//*[@id="i31"]/div[3]/div','']
    arteCenica = ['//*[@id="i31"]/div[3]/div','//*[@id="i12"]/div[3]/div','']
    culturaDigital = ['//*[@id="i38"]/div[3]/div','//*[@id="i41"]/div[3]/div','']
    culturaEconomia =['//*[@id="i48"]/div[3]/div','//*[@id="i51"]/div[3]/div','']
    livros = ['//*[@id="i58"]/div[3]/div','//*[@id="i61"]/div[3]/div','//*[@id="i64"]/div[3]/div','']
    profisionais =['//*[@id="i84"]/div[3]/div','//*[@id="i87"]/div[3]/div','//*[@id="i90"]/div[3]/div','//*[@id="i93"]/div[3]/div','']
    todas = [listaAsociacao,arteCenica,culturaDigital,culturaEconomia,livros,profisionais]
    sleep(2)
    for i in todas:
        xpath = choice(i)
        if xpath:
            bot.find_element(By.XPATH,xpath).click()
        sleep(2)
        
    sleep(2)
    bot.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div/div[1]').click()
    sleep(2)
    bot.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input').send_keys(email)
    sleep(2)
    bot.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(nome)
    sleep(2)
    bot.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(cpf)
    sleep(2)
    
def send():
    sleep(2)
    bot.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span').click()
    sleep(6)
def close():
    bot.close()
    
