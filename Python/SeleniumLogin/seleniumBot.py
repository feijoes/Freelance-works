import sys
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
link,password,conta = sys.argv[1:]

mobile_emulation = { "deviceName": "iPhone SE" }
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument("--disable-plugins-discovery")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options) #sometimes you have to insert your execution path
time.sleep(random.randint(3, 10))
driver.get('https://login.aliexpress.com/')
time.sleep(random.randint(3, 10))
driver.implicitly_wait(10) 
time.sleep(random.randint(3, 10))
driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div/div/div[1]/span/span[1]/input').send_keys(conta)
driver.implicitly_wait(10)
time.sleep(random.randint(3, 10))
driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div/div/div[2]/span/span[1]/input').send_keys(password)
driver.implicitly_wait(10)
time.sleep(random.randint(3, 10))
driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div/div/button[2]').click()
time.sleep(random.randint(3, 10))
time.sleep(5)
driver.get(link)
time.sleep(random.randint(3, 10))
time.sleep(15)
time.sleep(random.randint(4, 10))
driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]/div[2]/div/div[1]').click()
time.sleep(15)
