
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
        
    def get_products(self, page:int ) -> dict[str:int]:
        self.driver.get(f'https://flosamed.mx/wp-admin/edit.php?post_type=product&all_posts=1&paged={page}')
        products: list[WebElement] = self.driver.find_elements(By.XPATH,'//*[@id="the-list"]/*')
        id_products:dict[str:int] = []

        for product in products:
            
            if  "woocommerce-placeholder" in product.find_element(By.XPATH,f'//*[@id="{product.get_attribute("id")}"]/td[1]/a/img').get_attribute("class"):
                
                link_tag = product.find_element(By.XPATH,f'//*[@id="{product.get_attribute("id")}"]/td[1]/a')
                nombre = link_tag.find_element(By.XPATH,f'//*[@id="{product.get_attribute("id")}"]/td[2]/strong/a').text
                id = re.search(r'post=(\d+)', link_tag.get_attribute("href") ).group(1)
                id_products.append({"nombre": nombre, "id": id , "error" : ""})
        
        
        return id_products
    
    def find_image(self, nombre:str,id:int,path:str)-> bool:
        self.driver.get(f'https://www.google.com/search?q={nombre.replace(" ","+")}')
        try:
            self.driver.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()
            num = 1
            while True:
                self.driver.find_element(By.XPATH, f'//*[@id="islrg"]/div[1]/div[{num}]').click()
                sleep(3)
            
                URL = self.driver.find_element(By.XPATH, '//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div[1]/div[2]/div[2]/div/a/img').get_attribute("src")
                if URL.startswith("data:image"):
                    break
            picture_req = requests.get(URL,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0'})
            if picture_req.status_code == 200:
                os.makedirs(os.path.dirname(path + id), exist_ok=True)
                with open(f"{path + id}.jpg", 'wb') as f:
                    f.write(picture_req.content)
        except Exception as e:

            file_object = open('fail.txt', 'a')
# Append 'hello' at the end of file
            file_object.write(id  + "\n")
# Close the file
            file_object.close()
            return False
        return True
    
    def edit_image_product(self, post_id:int, path:str,name:str):
       
        try:
            self.driver.get(f'https://flosamed.mx/wp-admin/media-upload.php?post_id={post_id}&type=image')
            self.driver.find_element(By.XPATH,'//*[@id="async-upload"]').send_keys(os.path.dirname(__file__)+"\\"+path)
        
        
            sleep(2)
            self.driver.find_element(By.XPATH,'//*[@id="html-upload"]').click()
            self.driver.find_element(By.XPATH,'//*[@class="wp-post-thumbnail"]').click()
            self.driver.find_elements(By.XPATH,'//*[@id="save"]')[-1].click()
        except Exception as e:
            file_object = open('fail.txt', 'a')
# Append 'hello' at the end of file
            file_object.write(str(post_id) + "\n")
# Close the file
            file_object.close()
        
        

    
a = '<img width="370" height="250" src="https://flosamed.mx/wp-content/uploads/woocommerce-placeholder-370x250.png" class="woocommerce-placeholder wp-post-image" alt="Marcador" decoding="async" loading="lazy">'
test  = 'https://flosamed.mx/wp-admin/edit.php?s&post_status=all&post_type=product&action=-1&product_cat&product_type&stock_status&paged=386&action2=-1'
