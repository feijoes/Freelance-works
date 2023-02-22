
from time import sleep
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import requests
import os
chrome_options = webdriver.ChromeOptions()

# ADD commons arguments
chrome_options.add_argument("--incognito")
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument("--disable-plugins-discovery")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

class Bot():
    driver: webdriver.Chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options) 
    categorias = ["patente","ortopedia"]
    def __init__(self) -> None:
        self.driver.implicitly_wait(10)
        
    def login(self, username:str, password:str ) -> None:
        self.driver.get('https://flosamed.mx/wp-login.php')
        print(username,password)
        self.driver.find_element(By.XPATH, '//*[@id="user_login"]' ).send_keys( username )
        self.driver.find_element(By.XPATH, '//*[@id="user_pass"]' ).send_keys( password )
        self.driver.find_element(By.XPATH, '//*[@id="wp-submit"]').click()
        
    def get_products(self, pagina:int ):
        self.driver.get(f'https://flosamed.mx/wp-admin/edit.php?post_type=product&all_posts=1&paged={pagina}')
        products: list[WebElement] = self.driver.find_elements(By.XPATH,'//*[@id="the-list"]/*/td[1]/a/img')
        id_products:list[str] = []

        for product in products:
            if  "woocommerce-placeholder" in product.get_attribute("class"):
                link = product.find_element(By.XPATH,'..').get_attribute("href")
                id_products.append(re.search(r'post=(\d+)', link ).group(1))
    
        return id_products
    
    def edit_image_product(self, post_id:int, path:str="" ,URL:str="https://odontodo.mx/wp-content/uploads/2021/08/CAMPOS-BOLSA-CON-50-MEDICOM-COLORES.jpg"):
        
        picture_req = requests.get(URL,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0'})
        if picture_req.status_code == 200:
            with open("file_name.jpg", 'wb') as f:
                f.write(picture_req.content)
        
        self.driver.get(f'https://flosamed.mx/wp-admin/media-upload.php?post_id={post_id}&type=image')
        self.driver.find_element(By.XPATH,'//*[@id="plupload-upload-ui"]/p/a').click()
        self.driver.find_element(By.XPATH,'//*[@id="async-upload"]').send_keys("file_name.jpg")
        sleep(212)         

a = '<img width="370" height="250" src="https://flosamed.mx/wp-content/uploads/woocommerce-placeholder-370x250.png" class="woocommerce-placeholder wp-post-image" alt="Marcador" decoding="async" loading="lazy">'
test  = 'https://flosamed.mx/wp-admin/edit.php?s&post_status=all&post_type=product&action=-1&product_cat&product_type&stock_status&paged=386&action2=-1'
