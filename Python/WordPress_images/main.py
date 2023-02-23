import seleniumBot
import os
from dotenv import load_dotenv
load_dotenv()

USERNAME = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

bot = seleniumBot.Bot()

# make login in website
bot.login( USERNAME, PASSWORD )

"""
bot.get_products(page) will return a dict of produts with that no image

    { "nombre" : "Name of the product" , "id" : "id of the product" }

"""

file_object = open('not_products.txt', 'r')

producto_not_page = [int(line.rstrip('\n')) for line in file_object.readlines()]

file_object.close()

file_object = open('fail.txt', 'r')

producto_fail = [int(line.rstrip('\n')) for line in file_object.readlines()]

file_object.close()
    
for page_id in range(1,432):
    
    
    if page_id in producto_not_page:continue
    
    key_products = bot.get_products(page=page_id)
    if not key_products:
        file_object = open('not_products.txt', 'a')
        file_object.write(str(page_id)  + "\n")
        file_object.close()
    for producto in key_products:
        
        
        if bot.find_image(nombre=producto["nombre"],path="bot/",id=producto["id"]):
            bot.edit_image_product(producto["id"],f'bot\{producto["id"]}.jpg',producto["nombre"])
  
print("programa terminado")
  


