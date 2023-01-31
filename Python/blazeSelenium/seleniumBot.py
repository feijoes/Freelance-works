from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import requests


# api-endpoint
URL = "http://127.0.0.1:8000"
  
# sending get request and saving the response as response object


def getDriver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--profile-directory=Default')
    chrome_options.add_argument("--disable-plugins-discovery")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')

    driver: webdriver.Chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options) 
    return driver

def login(user: str,password: str):
    driver =  getDriver()
    driver.get("https://blaze.com/pt/?modal=auth&tab=login")

    driver.find_element(By.XPATH, './/*[@id="auth-modal"]/div/form/div[1]/div/input').send_keys(user) 
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="auth-modal"]/div/form/div[2]/div/input').send_keys(password) 
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="auth-modal"]/div/form/div[4]/button').click()
    driver.close() 

def getDouble():
    driver = getDriver()
    driver.get("https://blaze.com/pt/games/double")
    while True:
        
        sleep(10)
        lastNumber = driver.find_element(By.XPATH,'//*[@id="roulette-recent"]/div/div[1]/div[1]/div/div/div').text
        requests.post(URL,json= {"text": lastNumber, "date": "2"})
    
    




